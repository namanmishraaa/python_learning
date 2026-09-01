# Persona Based prompting

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """

"""

response = client.chat.completions.create(

)