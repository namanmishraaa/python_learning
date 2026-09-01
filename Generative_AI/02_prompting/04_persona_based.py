# Persona Based prompting

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are software engineer with 15 year i
"""

messages = [
    {
          "role": "system",
          "content": SYSTEM_PROMPT
    },
    {
          "role": "user", 
          "content":"Help me with understanding the working of DFS"
    }
]


response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
)