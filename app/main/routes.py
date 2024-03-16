from flask import Blueprint, render_template, request, jsonify
from app.models import perform_search, get_research_data, get_teaching_data
from utils import get_chatgpt_response
from app.visualization_utils import prepare_graph_data, convert_to_json

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    results = perform_search(query)

    if results:
        # 如果在数据库中找到了匹配的结果,使用ChatGPT生成回答
        prompt = f"根据以下搜索结果回答问题'{query}':\n{results}"
        answer = get_chatgpt_response(prompt)
    else:
        # 如果数据库中没有找到匹配的结果,直接使用ChatGPT进行查询
        answer = get_chatgpt_response(query)

    return jsonify({"answer": answer})


@main.route("/research")
def research():
    research_data = get_research_data()

    # 准备科研数据可视化所需的数据
    nodes = []
    edges = []
    for data in research_data:
        project_node = {
            "id": data["project_id"],
            "label": data["project_name"],
            "type": "project",
        }
        researcher_node = {
            "id": data["researcher_id"],
            "label": data["researcher_name"],
            "type": "researcher",
        }
        nodes.append(project_node)
        nodes.append(researcher_node)

        edge = {"source": data["project_id"], "target": data["researcher_id"]}
        edges.append(edge)

    graph_data = prepare_graph_data(nodes, edges)
    graph_json = convert_to_json(graph_data)

    return render_template("research.html", graph_data=graph_json)


@main.route("/teaching")
def teaching():
    teaching_data = get_teaching_data()

    # 准备教学数据可视化所需的数据
    nodes = []
    edges = []
    for data in teaching_data:
        course_node = {
            "id": data["course_id"],
            "label": data["course_name"],
            "type": "course",
        }
        instructor_node = {
            "id": data["instructor_id"],
            "label": data["instructor_name"],
            "type": "instructor",
        }
        nodes.append(course_node)
        nodes.append(instructor_node)

        edge = {"source": data["course_id"], "target": data["instructor_id"]}
        edges.append(edge)

    graph_data = prepare_graph_data(nodes, edges)
    graph_json = convert_to_json(graph_data)

    return render_template("teaching.html", graph_data=graph_json)
