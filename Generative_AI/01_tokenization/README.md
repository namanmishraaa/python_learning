# Tokenization with `tiktoken`

This example demonstrates how text is converted into model-oriented token IDs and how token IDs can be decoded back into text. Tokenization is the boundary between human-readable text and the numerical input representation used by language models.

## Architecture

```mermaid
flowchart LR
    T[Input text\nHey there! My name is Naman Mishra]
    E[tiktoken encoder\nGPT-4o encoding]
    I[Token IDs\ninteger sequence]
    D[Decoder]
    O[Decoded text]

    T --> E --> I
    I --> D --> O
```

## Runtime Flow

```mermaid
sequenceDiagram
    participant P as main.py
    participant K as tiktoken

    P->>K: encoding_for_model("gpt-4o")
    K-->>P: Encoder
    P->>K: encode(text)
    K-->>P: Token IDs
    P->>K: decode(hard-coded token IDs)
    K-->>P: Text
    P-->>P: Print tokens and decoded text
```

1. `encoding_for_model("gpt-4o")` selects the tokenizer associated with the model family.
2. `encode(text)` converts the sample sentence into integers.
3. `decode(token_ids)` reconstructs text from a token sequence.
4. The script prints both results.

## Run

From this directory:

```powershell
python main.py
```

No API key, network service, or model server is required. The tokenizer runs locally through the `tiktoken` package.

## Key Concepts

- A token may be a complete word, part of a word, punctuation, whitespace, or another text fragment.
- Token counts affect context-window usage, latency, and API cost.
- Encoding is not always character-based or word-based.
- Use the tokenizer associated with the target model when estimating prompt size.
- Decoding arbitrary token IDs may produce unexpected text or fail if IDs are invalid for the encoding.

## Revision Notes

```text
Text -> encode -> token IDs -> model input
Token IDs -> decode -> text
```

The current script uses a fixed sentence for encoding and a separate hard-coded token list for decoding; the decoded list is not generated from the sentence in the same run.

## Possible Extensions

- Print the token count with `len(tokens)`.
- Compare tokenization across model encodings.
- Measure how punctuation, whitespace, and non-English text affect token counts.
- Add a helper that estimates the token budget of a prompt before sending it to an API.
