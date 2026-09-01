import json
from datetime import datetime

# API Response from OpenAI ChatCompletion
response = {
    "id": "chatcmpl-EIdK4lASAKX7waEsqCbPqdL2nlkVO",
    "object": "chat.completion",
    "created": datetime.fromtimestamp(1788109768).isoformat(),
    "model": "gpt-4o-mini-2024-07-18",
    "service_tier": "default",
    "system_fingerprint": "fp_ae245680e8",
    "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": None,
        "annotations": [],
        "audio": None,
        "function_call": None,
        "tool_calls": None
    },
    "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 9,
        "total_tokens": 18,
        "completion_tokens_details": {
            "reasoning_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0,
            "audio_tokens": 0,
            "text_tokens": None
        },
        "prompt_tokens_details": {
            "audio_tokens": 0,
            "cached_tokens": 0,
            "cache_write_tokens": None,
            "image_tokens": None,
            "text_tokens": None
        },
        "compute_units": None
    },
    "finish_reason": "stop",
    "metadata": None,
    "moderation": None
}

# Pretty print the response
print(json.dumps(response, indent=2))