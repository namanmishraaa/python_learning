# Prompt Formatting Styles - Complete Learning Guide

Prompt formatting is crucial for effective communication with language models. Different models and frameworks support different formatting conventions. This guide covers the most popular prompt formats with detailed explanations and practical examples.

---

## Table of Contents
1. [Alpaca Format](#alpaca-format)
2. [ChatML Schema](#chatml-schema)
3. [Inst Format (Mistral)](#inst-format-mistral)
4. [OpenAI Chat Completion Format](#openai-chat-completion-format)
5. [Claude Format](#claude-format)
6. [LLaMA 2 Format](#llama-2-format)
7. [Zephyr Format](#zephyr-format)
8. [Comparison Table](#comparison-table)

---

## Alpaca Format

### Overview
The Alpaca format is based on the Stanford Alpaca model and uses a simple, structured template for instruction-following tasks. It's widely used for fine-tuning open-source models.

### Structure
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:
{response}
```

### Key Characteristics
- Explicit section headers (Instruction, Input, Response)
- Clear separation between different parts
- Optional input (can be empty)
- Simple and easy to understand

### Example 1: Translation Task
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Translate the following text from English to French.

### Input:
Hello, how are you today?

### Response:
Bonjour, comment allez-vous aujourd'hui?
```

### Example 2: Question Answering
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Answer the following question based on the provided context.

### Input:
Context: The Eiffel Tower was built in 1889 for the World's Fair.
Question: When was the Eiffel Tower built?

### Response:
The Eiffel Tower was built in 1889 for the World's Fair.
```

### Example 3: Code Generation
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Write Python code to calculate the factorial of a number.

### Input:
Number: 5

### Response:
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
```

### Python Example Implementation
```python
def format_alpaca_prompt(instruction, input_text="", response=""):
    """Format prompt in Alpaca style"""
    prompt = "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n"
    
    prompt += f"### Instruction:\n{instruction}\n\n"
    
    if input_text:
        prompt += f"### Input:\n{input_text}\n\n"
    
    prompt += "### Response:\n"
    
    if response:
        prompt += response
    
    return prompt

# Usage
prompt = format_alpaca_prompt(
    instruction="Translate to Spanish",
    input_text="Good morning",
    response="Buenos días"
)
print(prompt)
```

---

## ChatML Schema

### Overview
ChatML (Chat Markup Language) is a format developed by OpenAI for multi-turn conversations. It's used in models like GPT-3.5-turbo and provides a clear way to structure conversations with multiple participants.

### Structure
```
<|im_start|>system
{system_message}
<|im_end|>
<|im_start|>user
{user_message}
<|im_end|>
<|im_start|>assistant
{assistant_message}
<|im_end|>
```

### Key Characteristics
- Uses special XML-like tokens: `<|im_start|>` and `<|im_end|>`
- Role-based (system, user, assistant)
- Supports multi-turn conversations
- Standard format for OpenAI APIs

### Example 1: Simple Question-Answer
```
<|im_start|>system
You are a helpful assistant.
<|im_end|>
<|im_start|>user
What is the capital of France?
<|im_end|>
<|im_start|>assistant
The capital of France is Paris. It is located in the north-central part of the country and is known for its iconic landmarks such as the Eiffel Tower.
<|im_end|>
```

### Example 2: Multi-turn Conversation
```
<|im_start|>system
You are an expert Python programmer.
<|im_end|>
<|im_start|>user
How do I read a file in Python?
<|im_end|>
<|im_start|>assistant
You can read a file in Python using the `open()` function. Here's a basic example:

```python
with open('file.txt', 'r') as f:
    content = f.read()
```
<|im_end|>
<|im_start|>user
What does the `with` statement do?
<|im_end|>
<|im_start|>assistant
The `with` statement ensures that the file is properly closed after reading, even if an error occurs. It's a context manager that handles resource management automatically.
<|im_end|>
```

### Example 3: System Prompt with Instructions
```
<|im_start|>system
You are a JSON formatter. Convert user input into valid JSON format. Always validate your output. Return only valid JSON, no explanations.
<|im_end|>
<|im_start|>user
Name: John, Age: 30, City: New York
<|im_end|>
<|im_start|>assistant
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
<|im_end|>
```

### Python Example Implementation
```python
def format_chatml_message(role, content):
    """Format a single ChatML message"""
    return f"<|im_start|>{role}\n{content}\n<|im_end|>"

def format_chatml_conversation(messages, system_prompt=None):
    """Format a complete ChatML conversation"""
    conversation = ""
    
    if system_prompt:
        conversation += format_chatml_message("system", system_prompt) + "\n"
    
    for msg in messages:
        conversation += format_chatml_message(msg['role'], msg['content']) + "\n"
    
    return conversation

# Usage
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."}
]

prompt = format_chatml_conversation(messages, system_prompt="You are helpful.")
print(prompt)
```

---

## Inst Format (Mistral)

### Overview
The Inst format is used by Mistral AI models. It's similar to Alpaca but with a more concise syntax using `[INST]` and `[/INST]` markers.

### Structure
```
[INST] {instruction} [/INST] {response}
```

For system prompts:
```
[INST] <<SYS>>
{system_message}
<</SYS>>

{instruction} [/INST] {response}
```

### Key Characteristics
- Compact and concise markers
- Supports optional system prompts
- Efficient token usage
- Used by Mistral 7B, Mistral 8x7B, and other Mistral models

### Example 1: Simple Instruction
```
[INST] What is machine learning? [/INST] Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.
```

### Example 2: With System Prompt
```
[INST] <<SYS>>
You are a concise Python expert. Provide short, direct answers.
<</SYS>>

Write a function to check if a number is prime. [/INST] 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Example 3: Multi-turn with System Prompt
```
[INST] <<SYS>>
You are a data analysis expert.
<</SYS>>

What are the main types of data? [/INST] The main types of data are:
1. Numerical (integers, floats)
2. Categorical (labels, categories)
3. Ordinal (ranked categories)
4. Text/String
5. Boolean (True/False)

[INST] How do I handle missing values? [/INST] Common approaches to handle missing values:
1. Deletion (remove rows/columns)
2. Imputation (fill with mean, median, mode)
3. Prediction (use ML to predict missing values)
4. Forward/backward fill (for time series)
```

### Example 4: Code Review Task
```
[INST] <<SYS>>
You are a senior code reviewer. Be constructive and suggest improvements.
<</SYS>>

Review this code:
```python
data = [1,2,3,4,5]
sum = 0
for i in data:
    sum = sum + i
print(sum)
```
[/INST] This code works but could be improved:

1. **Use built-in sum()**: `total = sum(data)` is more Pythonic
2. **Avoid shadowing built-ins**: Don't use `sum` as variable name
3. **Better variable names**: Use `numbers` or `values` instead of `data`

Improved version:
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
```
```

### Python Example Implementation
```python
def format_inst_prompt(instruction, response="", system_prompt=None):
    """Format prompt in Inst (Mistral) style"""
    prompt = ""
    
    if system_prompt:
        prompt += f"[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n"
    else:
        prompt += "[INST] "
    
    prompt += f"{instruction} [/INST]"
    
    if response:
        prompt += f" {response}"
    
    return prompt

# Usage
prompt = format_inst_prompt(
    instruction="What is AI?",
    system_prompt="You are a tech expert",
    response="Artificial Intelligence is the simulation of human intelligence."
)
print(prompt)
```

---

## OpenAI Chat Completion Format

### Overview
This is the standard format used by OpenAI's Chat Completion API. It's the de facto standard for modern LLMs.

### Structure
```python
{
    "messages": [
        {"role": "system", "content": "system_prompt"},
        {"role": "user", "content": "user_message"},
        {"role": "assistant", "content": "assistant_message"}
    ],
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 150
}
```

### Key Characteristics
- JSON format
- Role-based structure (system, user, assistant, function)
- Standard API format
- Supports function calling
- Widely compatible

### Example 1: Simple Query
```python
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    "model": "gpt-3.5-turbo",
    "temperature": 0.7
}
```

### Example 2: Multi-turn Conversation
```python
{
    "messages": [
        {"role": "system", "content": "You are a Python coding tutor."},
        {"role": "user", "content": "How do decorators work in Python?"},
        {"role": "assistant", "content": "Decorators are functions that modify the behavior of other functions..."},
        {"role": "user", "content": "Can you show me an example?"},
        {"role": "assistant", "content": "Sure! Here's a simple example..."}
    ],
    "model": "gpt-4",
    "temperature": 0.5
}
```

### Example 3: With Function Calling
```python
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant that can call functions."},
        {"role": "user", "content": "What's the weather in Paris?"}
    ],
    "model": "gpt-4",
    "functions": [
        {
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }
    ]
}
```

### Python Example Implementation
```python
import json
import openai

def format_openai_messages(messages, system_prompt=None):
    """Format messages for OpenAI API"""
    formatted = []
    
    if system_prompt:
        formatted.append({"role": "system", "content": system_prompt})
    
    for msg in messages:
        formatted.append({
            "role": msg.get("role", "user"),
            "content": msg.get("content", "")
        })
    
    return formatted

# Usage
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."}
]

formatted = format_openai_messages(messages, system_prompt="Be helpful.")
print(json.dumps(formatted, indent=2))
```

---

## Claude Format

### Overview
Anthropic's Claude uses a specific format for conversations. It's similar to ChatML but with slight differences in how it handles system prompts and multi-turn conversations.

### Structure
```
Human: {user_message}
Assistant: {assistant_message}
Human: {next_user_message}
Assistant: {next_assistant_message}
```

With system prompt:
```
System: {system_prompt}