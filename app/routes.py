from flask import Blueprint, render_template, request, jsonify
from app.controllers.search_controller import search_controller
from app.controllers.research_data_controller import research_data_controller
from app.controllers.teaching_data_controller import teaching_data_controller

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('search.html')

@main_bp.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    results = search_controller.search(query)
    return jsonify(results)

@main_bp.route('/research-data', methods=['GET'])
def research_data():
    data = research_data_controller.get_research_data()
    return render_template('research_data.html', data=data)

@main_bp.route('/teaching-data', methods=['GET'])
def teaching_data():
    data = teaching_data_controller.get_teaching_data()
    return render_template('teaching_data.html', data=data)