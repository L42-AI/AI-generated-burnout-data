import os
from dotenv import load_dotenv

from openai import OpenAI

import generate
from repr import MonologicalData
from SQL import SQLWorker
from interview_persona import InterviewPersona
from monological_prompts import monological_prompts

# Load environment variables
# This include the API key to acces OpenAI services
load_dotenv('.env')

OpenAIClient = OpenAI(api_key=os.getenv('API_KEY'))

def monological():
    SQL = SQLWorker()

    for prompt in monological_prompts:
        if SQL.in_db(prompt):
            print(f"Prompt '{prompt}' already in database")
            continue
        
        SQL.add(MonologicalData(prompt=prompt, response=generate.monological_text(OpenAIClient, prompt)))

def dialogical():
    interview = generate.Interview(OpenAIClient)

    interview.with_persona(InterviewPersona.PERSON)

    interview.start()

def resume_interview():

    interview = generate.Interview(OpenAIClient)
    interview.continue_interview('interview_PERSON.csv')

if __name__ == "__main__":
    resume_interview()