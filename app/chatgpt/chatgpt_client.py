import requests

class ChatGPTClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    def generate_response(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'prompt': prompt,
            'max_tokens': 100,
            'n': 1,
            'stop': None,
            'temperature': 0.7
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['text']