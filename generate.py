from typing import Optional, List, Dict

from openai import OpenAI

from uuid import uuid4

from interview_persona import InterviewPersona

from helpers import create_input_prompt, execute_request
    
def monological_text(OpenAIClient: OpenAI, prompt: str) -> str:
    return execute_request(OpenAIClient, create_input_prompt(prompt), 0.0)
    
def dialogical_text(OpenAIClient: OpenAI, interview_log: List[Dict]) -> str:
    return execute_request(OpenAIClient, interview_log, 0.7)

class Interview:
    def __init__(self, OpenAIClient: OpenAI):
        self.OpenAIClient = OpenAIClient

        self.interview_id = uuid4() # Unique identifier for the interview
        self.wordcount = 6000 # Default wordcount for the interview

        self.interview_persona: Optional[InterviewPersona] = None
        self.interview_log: List[Dict] = [] # Log of the interview


    def with_persona(self, interview_persona: InterviewPersona) -> str:
        self.interview_persona = interview_persona
        self.log("system", f"You are {interview_persona.value}, who is being interviewed by a student for their Bachelor Research Project.")

    def log(self, role: str, content: str) -> None:
        self.interview_log.append(
            {
                "role": role,
                "content": content
            }
        )

        self.save_log()

    def start(self) -> str:
        if not self.interview_persona:
            raise Exception("Interview persona is not set, please use the 'with_persona' method to set the persona and try again.")
        
        # While the wordcount is not 0, keep asking questions
        while self.wordcount > 0:

            # Prompt the user for a question
            question = input("Next Question: ")

            # Append the question to the interview log
            self.log("user", question)

            # Get the answer from the AI
            answer = dialogical_text(self.OpenAIClient, self.interview_log)
            
            # Append the answer to the interview log
            self.log("assistant", answer)
            
            # Decrease the wordcount by the number of words in the answer
            self.wordcount -= len(answer.split())

            # Visualize the answer
            print(answer)

    def save_log(self):
        NotImplemented
        