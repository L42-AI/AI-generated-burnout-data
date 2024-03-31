from typing import List, Dict, Optional

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

TEXT_MODEL = "gpt-4"

def create_input_prompt(prompt: str) -> List[Dict]:
    return [{"role": "user", "content": prompt}]
    
def execute_request(OpenAIClient: OpenAI, messages: List[Dict], temperature: float) -> Optional[str]:
    try:
        response = OpenAIClient.chat.completions.create(
            model=TEXT_MODEL,
            messages=messages,
            temperature=temperature,
        )
        return get_response(response)

    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return None
    
def get_response(chat_completion_obj: ChatCompletion) -> str:
    return chat_completion_obj.choices[0].message.content