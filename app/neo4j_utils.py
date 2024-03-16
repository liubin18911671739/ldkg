from py2neo import Graph


def create_graph(uri, user, password):
    """
    创建Neo4j图数据库连接
    :param uri: Neo4j服务器的URI
    :param user: 用户名
    :param password: 密码
    :return: Graph对象
    """
    graph = Graph(uri, auth=(user, password))
    return graph


def run_query(graph, query, parameters=None):
    """
    在Neo4j图数据库中执行Cypher查询
    :param graph: Graph对象
    :param query: Cypher查询语句
    :param parameters: 查询参数(可选)
    :return: 查询结果
    """
    result = graph.run(query, parameters=parameters)
    return result


def create_node(graph, label, properties):
    """
    在Neo4j图数据库中创建节点
    :param graph: Graph对象
    :param label: 节点标签
    :param properties: 节点属性(字典类型)
    :return: 创建的节点
    """
    node = graph.create(properties)[0]
    node.add_label(label)
    return node


def create_relationship(graph, node1, node2, relationship_type, properties=None):
    """
    在Neo4j图数据库中创建关系
    :param graph: Graph对象
    :param node1: 起始节点
    :param node2: 目标节点
    :param relationship_type: 关系类型
    :param properties: 关系属性(字典类型,可选)
    :return: 创建的关系
    """
    relationship = graph.create((node1, relationship_type, node2, properties))
    return relationship


def delete_node(graph, node):
    """
    从Neo4j图数据库中删除节点
    :param graph: Graph对象
    :param node: 要删除的节点
    """
    graph.delete(node)


def delete_relationship(graph, relationship):
    """
    从Neo4j图数据库中删除关系
    :param graph: Graph对象
    :param relationship: 要删除的关系
    """
    graph.separate(relationship)
