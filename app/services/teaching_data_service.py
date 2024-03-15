from app.database import neo4j_client

class TeachingDataService:
    def __init__(self):
        self.neo4j_client = neo4j_client

    def get_teaching_data(self):
        query = """
        MATCH (c:Course)-[:TAUGHT_BY]->(p:Professor)
        OPTIONAL MATCH (c)-[:HAS_PREREQUISITE]->(pre:Course)
        RETURN c.code AS course_code, c.name AS course_name, p.name AS professor_name,
               collect(pre.code) AS prerequisite_codes
        """
        results = self.neo4j_client.execute_query(query)
        return self._process_teaching_data(results)

    def _process_teaching_data(self, results):
        processed_data = []
        for record in results:
            course_code = record["course_code"]
            course_name = record["course_name"]
            professor_name = record["professor_name"]
            prerequisite_codes = record["prerequisite_codes"]

            course_data = {
                "code": course_code,
                "name": course_name,
                "professor": professor_name,
                "prerequisites": prerequisite_codes
            }
            processed_data.append(course_data)

        return processed_data