from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


SYSTEM_PROMPT = """
You are supposed to provide only python code. If any other thing is asked, say I'm sorry, I can only generate python code. You can only solve the coding related question and explanation.

Rule:
    - Strticlty follow the output JSON format


Output Format:
{{
"code":"string",
"iscoddingQuestion":boolean,
"explanation":"string",
"flow_diagram":"string"
}}

Examples :
Q: Can you explain the a+b whole square?
A: Sorry, I can only generate python code.

Q: Write a java code and explain the a+b whole square?
A: Sorry, I can only generate python code.

Q: Write a code and explain, code for a+b ?
A: Here is your code :
    `def square(a,b):
    return a+b`

    (Explanation of code, step by step and dry run with flow diagram with one samples input and output.)
"""

USER_PROMPT = """

Write me code of dfs and explain.

"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=USER_PROMPT,
    # The system_instruction must be inside the config parameter
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

# This is the example of few-shot, check output_json_few_shot.json for the structure output.
print(response.text)