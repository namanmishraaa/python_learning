from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434/"
)

@app.post("/chat")
def chat(
        message: str = Body(..., description="Your message here")
):

    respone = client.chat(model="llama3.1:8b",
                messages=[
                    {
                        "role":"user",""
                        "content":message
                    }
                ])

    return {
        "respone" : respone.message.content
    }