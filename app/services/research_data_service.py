from app.database import neo4j_client

class ResearchDataService:
    def __init__(self):
        self.neo4j_client = neo4j_client

    def get_research_data(self):
        query = """
        MATCH (p:Paper)-[r:AUTHORED_BY]->(a:Author)
        RETURN p.title AS paper_title, a.name AS author_name
        """
        results = self.neo4j_client.execute_query(query)
        return self._process_research_data(results)

    def _process_research_data(self, results):
        processed_data = []
        for record in results:
            paper_title = record["paper_title"]
            author_name = record["author_name"]
            processed_data.append({
                "paper_title": paper_title,
                "author_name": author_name
            })
        return processed_data