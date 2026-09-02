import time
# from google import genai # There are some error with gemini using openai instead
from openai import OpenAI
from pydantic import BaseModel
from typing import Literal
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries suing chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enought PLAN had been done, finally you can give an OUTPUT.

    Rules:
    - Stictly follwo the give JSON output format.
    - Only run one step at a time.
    - The swqucen of steps in START (Where user give an input), PLAN (That can be multiple times) 
    and finally OUTPUT (Which is going to the diplayed to the user).

    OUTPUT JSON Format:
    {
     "step": "START" | "PLAN" | "OUTPUT",
     "content":"string"
    }


    Example :

    START: Hey, can you solve 2+3*5/10
    PLAN: {"step": "PLAN", "content" : "User is interested in math problem"}
    PLAN: {"step": "PLAN", "content" : "Looking at the problem, we should sovle this using BODMAS method"}  
    PLAN: {"step": "PLAN", "content" : "Yes, BODMAS is the correct thing to be done here."}
    PLAN: {"step": "PLAN", "content" : "First we multiply 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content" : "Now the new equation is 2+ 15 / 10"}
    PLAN: {"step": "PLAN", "content" : "We must perform division of 15 / 10 which is 1.5"}
    PLAN: {"step": "PLAN", "content" : "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content" : Now we must add 2 + 1.5 which is 3.5"}
    OUTPUT: Here is the output of 2+3*5/10=3.5


"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user", 
        "content": "Hey, can you write a code in javascript that can take n number of arguments and add all the numbers as fast as possible with caching."
    }
]


# 1. Initialize 'data' to None so it exists even if the loop fails
data = None 

print("--- Starting Chain of Thought Process ---")

while True:
    try:
        # Call the model with the FULL history (messages)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        
        # Parse the JSON response
        response_text = response.choices[0].message.content.strip()
        data = json.loads(response_text)
        print(f"{data['content']}")

        # Add the AI's response to the history so it remembers what it planned
        messages.append({
            "role": "assistant",
            "content": json.dumps(data)
        })

        # Check if we should stop
        if data['step'] == "OUTPUT":
            print("\nFinal Result Received!")
            break

        # # Wait to avoid 429 Rate Limit errors
        # print("...waiting 10 seconds for next step...")
        # time.sleep(30)

    except Exception as e:
        print(f"An error occurred: {e}")
        break

print("\n--- FINAL OUTPUT ---")
if data:
    print(data.get("content", "No content found"))