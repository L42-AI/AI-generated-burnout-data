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

def main():
    OpenAIClient = OpenAI(api_key=os.getenv('API_KEY'))

    for prompt in monological_prompts:
        print(generate.monological_text(OpenAIClient, prompt))
    
    interview = generate.Interview(OpenAIClient)

    interview.with_persona(InterviewPersona.PERSON)

    interview.start()

if __name__ == "__main__":
    main()