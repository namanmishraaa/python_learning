from transformers import pipeline

pipe = pipeline("text-generation", model="google/gemma-3-270m-it")
messages = [
    {"role": "user", "content": "Write a code for DFS and BFS in python and ELI5"},
]
result = pipe(messages)
print("result :-", result[0].get("generated_text")[1].get("content"))

"""
How does output looks like :- 

[
    {
        'generated_text': [
            {'role': 'user', 'content': 'How can I integrate API with frontend?'}, 
            {'role': 'assistant', 
             'content': "Integrating APIs with frontend involves several steps, from designing the API to implementing the frontend. Here's a breakdown of the process, covering key considerations and best practices:\n\n**1. Understanding the API's Purpose and Requirements:**\n\n*   **What is the API endpoint?** What data does it provide? What functionalities does it offer?\n*   **What are the key requirements of the API?**  Are there specific data types, formats, or functionalities you need to support?  Do you need to handle authentication, authorization, rate limiting, or other constraints?\n*   **What is the expected response format?**  What kind of data will be returned?  What are the expected response times?\n*   **What are the API's limitations?**  Are there any limitations on the amount of data you can process, the complexity of the API, or the number of requests you can make?\n*   **Who is the target audience?**  Who will be using the API?  What are their needs and expectations?  This will influence the design of the API's interface and documentation.\n\n**2. Design the API:**\n\n*   **API Design Document:**  A detailed document outlining the API's structure,"
             }
        ]
    }
]
"""