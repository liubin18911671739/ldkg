import openai
from flask import current_app


def get_chatgpt_response(prompt):
    openai.api_key = current_app.config[
        "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"
    ]

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()
    except Exception as e:
        current_app.logger.error(f"Error in get_chatgpt_response: {str(e)}")
        return "对不起,我现在无法回答您的问题。请稍后再试。"


def preprocess_query(query):
    # 在这里对用户查询进行预处理,例如去除标点符号、转换大小写等
    processed_query = query.strip().lower()
    return processed_query


def postprocess_response(response):
    # 在这里对ChatGPT生成的响应进行后处理,例如格式化、添加标点符号等
    processed_response = response.capitalize()
    return processed_response


def log_query(query, response):
    # 在这里记录用户查询和ChatGPT生成的响应,以便进行分析和改进
    current_app.logger.info(f"User Query: {query}")
    current_app.logger.info(f"ChatGPT Response: {response}")


def handle_error(error):
    # 在这里处理在与ChatGPT交互过程中可能发生的错误
    current_app.logger.error(f"Error: {str(error)}")
    return "抱歉,处理您的请求时发生了错误。请稍后再试。"
