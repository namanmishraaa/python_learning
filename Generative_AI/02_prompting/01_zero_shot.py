from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


SYSTEM_PROMPT = """
You are supposed to provide only python code. If any other thing is asked, say I'm sorry, I can only generate python code!
"""


response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Generate me a joke",
    # The system_instruction must be inside the config parameter
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

print(response.text)