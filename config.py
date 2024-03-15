import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

class Config:
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

    # Neo4j database configuration
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'password')

    # ChatGPT API configuration
    CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY', 'your-chatgpt-api-key')
    CHATGPT_API_URL = os.getenv('CHATGPT_API_URL', 'https://api.openai.com/v1/chat/completions')

    # Other configuration options
    # Add any additional configuration settings here