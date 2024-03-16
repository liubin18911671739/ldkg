import os
from py2neo import Graph


class Neo4jUtils:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4jname")
        password = os.getenv("NEO4J_PASSWORD", "neo4jpwd")

        self.graph = self.create_graph(uri, user, password)

    def create_graph(self, uri, user, password):
        try:
            graph = Graph(uri, auth=(user, password))
            return graph
        except Exception as e:
            print(f"Failed to create a connection to the graph: {e}")
            raise


# Get the graph instance
utils = Neo4jUtils()
graph = utils.graph

try:
    # Query all nodes
    nodes = graph.run("MATCH (n) RETURN n").data()

    # Print all nodes
    print("Nodes:")
    print("\n".join([str(node["n"]) for node in nodes]))

    # Query all relationships
    relationships = graph.run("MATCH ()-[r]->() RETURN r").data()

    # Print all relationships
    print("\nRelationships:")
    print("\n".join([str(relationship["r"]) for relationship in relationships]))

except Exception as e:
    print(f"Failed to query the graph: {e}")
    raise
