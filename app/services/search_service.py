from app.database import neo4j_client
from app.chatgpt import chatgpt_client

class SearchService:
    def __init__(self):
        self.neo4j_client = neo4j_client
        self.chatgpt_client = chatgpt_client

    def search(self, query):
        # Search in the Neo4j database
        neo4j_results = self._search_neo4j(query)

        if neo4j_results:
            # Process and return the Neo4j search results
            processed_results = self._process_neo4j_results(neo4j_results)
            return processed_results
        else:
            # If no results found in Neo4j, use ChatGPT to generate a response
            chatgpt_response = self._generate_chatgpt_response(query)
            return chatgpt_response

    def _search_neo4j(self, query):
        # Perform the search query in the Neo4j database
        cypher_query = f"""
        MATCH (n)
        WHERE n.name =~ '(?i).*{query}.*' OR n.description =~ '(?i).*{query}.*'
        RETURN n
        """
        results = self.neo4j_client.execute_query(cypher_query)
        return results

    def _process_neo4j_results(self, results):
        # Process the Neo4j search results and return them in a formatted way
        processed_results = []
        for record in results:
            node = record["n"]
            processed_results.append({
                "id": node.id,
                "name": node.get("name"),
                "description": node.get("description")
            })
        return processed_results

    def _generate_chatgpt_response(self, query):
        # Generate a response using ChatGPT
        prompt = f"Query: {query}\nResponse:"
        response = self.chatgpt_client.generate_response(prompt)
        return response