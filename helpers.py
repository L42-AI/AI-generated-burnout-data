from typing import Optional

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

from interview_types import InterviewLog, InterviewLogToAppend

TEXT_MODEL = "gpt-4"

def create_input_prompt(prompt: str) -> InterviewLog:
    return [{"role": "user", "content": prompt}]
    
def execute_request(OpenAIClient: OpenAI, messages: InterviewLog, temperature: float) -> str:
    response = OpenAIClient.chat.completions.create(
        model=TEXT_MODEL,
        messages=messages,
        temperature=temperature,
    )
    return get_response(response)
    
def get_response(chat_completion_obj: ChatCompletion) -> str:
    response = chat_completion_obj.choices[0].message.content
    if not response:
        raise Exception("Empty response")
    return response