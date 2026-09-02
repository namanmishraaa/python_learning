from transformers import pipeline

pipe = pipeline("text-generation", model="google/gemma-3-270m-it")
messages = [
    {"role": "user", "content": "How can I integrate API with frontend?"},
]
result = pipe(messages)
print(result)