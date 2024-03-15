from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, app=None):
        self.app = app
        self.driver = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('NEO4J_URI', 'bolt://localhost:7687')
        app.config.setdefault('NEO4J_USERNAME', 'neo4j')
        app.config.setdefault('NEO4J_PASSWORD', 'password')

        @app.teardown_appcontext
        def close_db(error):
            if hasattr(self, 'driver'):
                self.driver.close()

    def get_db(self):
        if not self.driver:
            self.driver = GraphDatabase.driver(
                self.app.config['NEO4J_URI'],
                auth=(self.app.config['NEO4J_USERNAME'], self.app.config['NEO4J_PASSWORD'])
            )
        return self.driver

    def close(self):
        if self.driver:
            self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.get_db().session() as session:
            result = session.run(query, parameters)
            return [record for record in result]