import json


def convert_to_json(data):
    """
    将数据转换为JSON格式
    :param data: 要转换的数据
    :return: JSON格式的数据
    """
    json_data = json.dumps(data)
    return json_data


def prepare_graph_data(nodes, edges):
    """
    准备用于可视化的图数据
    :param nodes: 节点列表,每个节点为一个字典,包含节点的属性
    :param edges: 边列表,每个边为一个字典,包含起始节点、目标节点和边的属性
    :return: 用于可视化的图数据字典
    """
    graph_data = {"nodes": nodes, "edges": edges}
    return graph_data


def prepare_bar_chart_data(labels, values):
    """
    准备用于条形图的数据
    :param labels: 条形图的标签列表
    :param values: 条形图的值列表
    :return: 用于条形图的数据字典
    """
    bar_chart_data = {"labels": labels, "values": values}
    return bar_chart_data


def prepare_pie_chart_data(labels, values):
    """
    准备用于饼图的数据
    :param labels: 饼图的标签列表
    :param values: 饼图的值列表
    :return: 用于饼图的数据字典
    """
    pie_chart_data = {"labels": labels, "values": values}
    return pie_chart_data


def prepare_line_chart_data(labels, series):
    """
    准备用于折线图的数据
    :param labels: 折线图的标签列表
    :param series: 折线图的系列数据列表,每个系列为一个字典,包含系列名称和对应的值列表
    :return: 用于折线图的数据字典
    """
    line_chart_data = {"labels": labels, "series": series}
    return line_chart_data


def prepare_scatter_plot_data(x_values, y_values):
    """
    准备用于散点图的数据
    :param x_values: 散点图的x坐标值列表
    :param y_values: 散点图的y坐标值列表
    :return: 用于散点图的数据字典
    """
    scatter_plot_data = {"x_values": x_values, "y_values": y_values}
    return scatter_plot_data
