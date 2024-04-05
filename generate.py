import os

from typing import Optional, List, Dict

from openai import OpenAI

from pprint import pprint

from interview_persona import InterviewPersona
import pandas as pd

from helpers import create_input_prompt, execute_request
    
def monological_text(OpenAIClient: OpenAI, prompt: str) -> str:
    return execute_request(OpenAIClient, create_input_prompt(prompt), 0.0)
    
def dialogical_text(OpenAIClient: OpenAI, interview_log: List[Dict]) -> str:
    return execute_request(OpenAIClient, interview_log, 0.7)

def get_interview_file_name(name: str) -> str:
    """
    Checks for presence of interview persona files and returns a new file name to avoid overwriting
    """

    file_name = f"interview_{name}"

    i = 0
    while os.path.exists(file_name):
        i += 1
        file_name = f"interview_{name}_{i}"

    return file_name + ".csv"


def get_questions(interview_log: List[Dict]) -> List[str]:
    return [log["content"] for log in interview_log if log["role"] == "user"]
    
def display_questions(interview_log: List[Dict]) -> None:
    print('=====================')
    for i, question in enumerate(get_questions(interview_log)):
        print()
        print(i+1, question)
        print()
    print('=====================')

def segment_questions(interview_log: List[Dict], question_number: int) -> List[Dict]:
    """
    This number is the number of question that will be asked
    """

    questions = get_questions(interview_log)

    if question_number == len(questions) + 1:
        return interview_log, None
    
    question_to_cut = questions[question_number]

    selection = {"system", "assistant"}
    for i, interactions in enumerate(interview_log):
        if interactions["role"] in selection:
            continue

        if interactions["content"] == question_to_cut:
            return interview_log[:i-2], interview_log[i-2:]

class Interview:
    def __init__(self, OpenAIClient: OpenAI):
        self.OpenAIClient = OpenAIClient

        self.wordcount = 6000 # Default wordcount for the interview

        self.interview_persona: Optional[InterviewPersona] = None
        self.interview_log: List[Dict] = [] # Log of the interview
        self.interview_log_to_add: Optional[List[Dict]] = None

    def with_persona(self, interview_persona: InterviewPersona) -> str:
        self.interview_persona = interview_persona
        self.file_name = get_interview_file_name(self.interview_persona.name)
        self.log("system", f"You are {self.interview_persona.value}, who is being interviewed by a student for their Bachelor Research Project.")

    def log(self, role: str, content: str) -> None:
        self.interview_log.append(
            {
                "role": role,
                "content": content
            }
        )

    def start(self) -> str:
        if not self.interview_persona:
            raise Exception("Interview persona is not set, please use the 'with_persona' method to set the persona and try again.")
        
        self.run_interview()

    def run_interview(self):
        try:
            # While the wordcount is not 0, keep asking questions
            while self.wordcount > 0:

                if not self.interview_log[-1]["role"] == "user":
                    
                    question = self.get_question()
                    if question == 'quit':
                        break

                # Get the answer from the AI
                answer = self.get_answer()
                
                # Decrease the wordcount by the number of words in the answer
                self.wordcount -= len(question.split())
                self.wordcount -= len(answer.split())

                # Visualize the answer
                print("=====================================")
                print(answer)
                print(self.wordcount)
                print("=====================================")
        except:
            pass
        finally:
            self.end()

    def get_question(self) -> str:
        question = input("\nNext Question (type 'quit' to exit): ")

        if question == 'quit':
            return question

        # Append the question to the interview log
        self.log("user", question)

        return question

    def get_answer(self) -> str:
        answer = dialogical_text(self.OpenAIClient, self.interview_log)
        self.log("assistant", answer)
        return answer

    def end(self) -> None:
        if self.interview_log_to_add:
            self.interview_log += self.interview_log_to_add
        interview_df = pd.DataFrame(self.interview_log)
        interview_df.to_csv(self.file_name, index=False)
        print(f"Interview log saved as '{self.file_name}'")

    def load_interview(self, interview_file: str) -> None:
        self.interview_log = pd.read_csv(interview_file).to_dict(orient="records")
        self.file_name = interview_file

    def continue_interview(self, interview_file: str) -> None:
        self.load_interview(interview_file)

        display_questions(self.interview_log)

        self.interview_log, self.interview_log_to_add = segment_questions(
            interview_log=self.interview_log,
            question_number=int(input("At what question would you like to continue? "))
            )

        self.run_interview()
