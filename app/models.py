from py2neo import Graph

graph = Graph("neo4j://localhost:7687", auth=("neo4j", "password"))


def execute_query(query):
    """
    Executes Cypher query in Neo4j
    """
    try:
        results = graph.run(query).data()
        return results
    except Exception as e:
        log_error("Error executing query", e)
        return []


def format_results(results, fields):
    """
    Formats the results obtained from Neo4j
    """
    formatted_results = []
    for result in results:
        formatted_result = {field: result[field] for field in fields}
        formatted_results.append(formatted_result)

    return formatted_results


def perform_search(query):
    results = execute_query(
        f"MATCH (n) WHERE n.title =~ '.*{query}.*' OR n.content =~ '.*{query}.*' RETURN n"
    )
    # Process and format the search results
    formatted_results = []
    for result in results:
        node = result["n"]
        formatted_result = {
            "title": node["title"],
            "snippet": node["content"][:100] + "...",
            "url": f"/detail/{node['id']}",
        }
        formatted_results.append(formatted_result)

    return formatted_results


def get_research_data():
    results = execute_query(
        """
        MATCH (p:Project)-[:BELONGS_TO]->(r:Researcher)
        RETURN p, r
        """
    )
    return format_results(results, ["p", "r"])


def get_teaching_data():
    results = execute_query(
        """
        MATCH (c:Course)-[:TAUGHT_BY]->(i:Instructor)
        RETURN c, i
        """
    )
    return format_results(results, ["c", "i"])


def log_error(message, exception):
    """
    Logs errors
    :param message: Custom error message
    :param exception: The exception that was raised
    """
    print(f"{message}: {str(exception)}")
