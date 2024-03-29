import openai
import os


class ChatGPT:

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.initialize_chatgpt()

    def initialize_chatgpt(self):
        """
        初始化ChatGPT API
        """
        openai.api_key = self.api_key

    def generate_response(
        self, prompt, model="gpt-3.5-turbo", max_tokens=1024, temperature=0.7
    ):
        """
        使用ChatGPT生成响应
        :param prompt: 输入的提示文本
        :param model: 使用的语言模型(默认为"gpt-3.5-turbo")
        :param max_tokens: 生成的最大令牌数(默认为1024)
        :param temperature: 控制生成文本的创造性和多样性(默认为0.7)
        :return: 生成的响应文本
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=temperature,
            )
            message = response.choices[0].message["content"].strip()
            return message
        except Exception as e:
            print(f"Error generating ChatGPT response: {str(e)}")
            return None


chatgpt = ChatGPT()

prompt = "What is the capital of France?"
response = chatgpt.generate_response(prompt)
print(response)
