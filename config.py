import os


class Config:
    def __init__(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
        self.NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
        self.NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
        self.NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


# The child classes will need to call the parent constructor:
class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.DEBUG = True


class TestingConfig(Config):
    def __init__(self):
        super().__init__()
        self.TESTING = True


class ProductionConfig(Config):
    pass  # Will use only the base config
