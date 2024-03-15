- [融合大语言模型和深度学习的多模态知识图谱 展示平台](#融合大语言模型和深度学习的多模态知识图谱-展示平台)
  - [开发环境](#开发环境)
  - [使用库](#使用库)
  - [system structure](#system-structure)

# 融合大语言模型和深度学习的多模态知识图谱 展示平台

https://github.com/liubin18911671739/ldkg.git

## 开发环境

语言： python3.10
web 框架： flask
UI: jinja2
版本控制 ：git
开发工具：vscode, pycharm
数据库：neo4j, sqlite3
图谱可视化：Cypher

开发协助：prompts, XML
文档：markdown

部署：Docker

## 使用库

jinja2
flask


## system structure

+---------------------------+
|         Front-end         |
+---------------------------+
|  +-----------------------+ |
|  |  User Interface (UI)  | |
|  +-----------------------+ |
|  |  - Search Page        | |
|  |  - Research Data Page | |
|  |  - Teaching Data Page | |
|  +-----------------------+ |
|                            |
|  +-----------------------+ |
|  |  UI Components        | |
|  +-----------------------+ |
|  |  - Search Bar         | |
|  |  - Result Display     | |
|  |  - Data Visualization | |
|  +-----------------------+ |
+----------------------------+
           |     |
           |     |
           |     |
+----------------------------+
|         Back-end          |
+----------------------------+
|  +-----------------------+ |
|  |  Flask Application    | |
|  +-----------------------+ |
|  |  - Routes             | |
|  |  - Controllers        | |
|  |  - Services           | |
|  +-----------------------+ |
|                            |
|  +-----------------------+ |
|  |  Database (Neo4j)     | |
|  +-----------------------+ |
|  |  - Data Models        | |
|  |  - Cypher Queries     | |
|  +-----------------------+ |
|                            |
|  +-----------------------+ |
|  |  ChatGPT Integration  | |
|  +-----------------------+ |
|  |  - API Client         | |
|  |  - Response Handling  | |
|  +-----------------------+ |
+----------------------------+

