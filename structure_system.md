```
project_name/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── neo4j_utils.py
│   ├── chatgpt_utils.py
│   ├── visualization_utils.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── utils.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   ├── visualization.js
│   │   │   └── main.js
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── search.html
│       ├── result.html
│       └── visualization.html
├── config.py
├── requirements.txt
├── run.py
├── Dockerfile
└── README.md
```

以下是每个文件的内容:

**app/**init**.py**

```python
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from neo4j import GraphDatabase

# Initialize Flask app
app = Flask(__name__)

# Configure the app based on the environment
env = 'development'  # or 'production'
app.config.from_object(config[env])

# Initialize Flask-Bootstrap
bootstrap = Bootstrap(app)

# Connect to Neo4j database
driver = GraphDatabase.driver(app.config['NEO4J_URI'], auth=(app.config['NEO4J_USER'], app.config['NEO4J_PASSWORD']))

# Import and register blueprints
from app.main import main_bp
app.register_blueprint(main_bp)

# Import utilities
from app import neo4j_utils, chatgpt_utils, visualization_utils
```

**app/models.py**

```python
# 在这里定义数据模型(如果需要)
```

**app/neo4j_utils.py**

```python
# 在这里定义与 Neo4j 数据库交互的实用程序函数
```

**app/chatgpt_utils.py**

```python
# 在这里定义与 ChatGPT 集成相关的实用程序函数
```

**app/visualization_utils.py**

```python
# 在这里定义知识图谱可视化相关的实用程序函数
```

**app/main/**init**.py**

```python
from flask import Blueprint

main_bp = Blueprint('main', __name__, template_folder='templates')

from app.main import routes
```

**app/main/routes.py**

```python
from flask import render_template, request
from app.main import main_bp
from app import neo4j_utils, chatgpt_utils, visualization_utils

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    # 处理搜索表单提交
    if request.method == 'POST':
        query = request.form['query']
        # 执行查询和处理逻辑
        # ...

    return render_template('index.html')

@main_bp.route('/search', methods=['GET', 'POST'])
def search():
    # 处理搜索表单提交
    # ...

    return render_template('search.html')

@main_bp.route('/result', methods=['GET'])
def result():
    # 展示搜索结果
    # ...

    return render_template('result.html')

@main_bp.route('/visualization', methods=['GET'])
def visualization():
    # 展示知识图谱可视化
    # ...

    return render_template('visualization.html')
```

**app/main/forms.py**

```python
# 在这里定义表单(如果需要)
```

**app/main/utils.py**

```python
# 在这里定义与主要功能相关的实用程序函数
```

**app/templates/base.html**

```html
<!-- 基础模板 -->
```

**app/templates/index.html**

```html
<!-- 主页模板 -->
```

**app/templates/search.html**

```html
<!-- 搜索页面模板 -->
```

**app/templates/result.html**

```html
<!-- 搜索结果页面模板 -->
```

**app/templates/visualization.html**

```html
<!-- 知识图谱可视化页面模板 -->
```

**config.py**

```python
# 配置文件, 包含应用程序配置设置
```

**requirements.txt**

```
# 列出项目依赖项
```

**run.py**

```python
from app import app

if __name__ == '__main__':
    app.run(debug=True)
```

**Dockerfile**

```dockerfile
# Dockerfile 用于构建 Docker 映像
```

**README.md**

```markdown
# 项目说明和文档
```
