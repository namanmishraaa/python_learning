# Agentic AI Examples

This folder contains an agent experiment centered on a weather tool. The implementation lives in the nested `weather_agent` folder and demonstrates how an LLM can plan, call an external function, receive the tool result, and produce a final answer.

## Folder Architecture

```mermaid
flowchart TD
    A[05_agentic_AI]
    B[weather_agent]
    C[main.py\nBasic Responses API example]
    D[agent.py\nTool-using agent loop]
    E[agent_output.py\nPydantic output schema]
    F[output_result.txt\nCaptured sample]

    A --> B
    B --> C
    B --> D
    B --> E
    B --> F
```

## Agent Architecture

```mermaid
flowchart LR
    U[User request]
    A[Agent loop\nagent.py]
    O[OpenAI gpt-4o-mini]
    S[Structured step\nSTART / PLAN / TOOL_CALL / OUTPUT]
    W[get_weather tool]
    X[wttr.in HTTP service]
    R[Weather result]
    F[Final response]

    U --> A --> O --> S
    S -->|TOOL_CALL| W --> X --> R --> A
    S -->|OUTPUT| F
```

## Two Learning Paths

| File | Purpose |
| --- | --- |
| `weather_agent/main.py` | Basic OpenAI Responses API call. It reads one message and prints `output_text`. |
| `weather_agent/agent.py` | Full structured agent loop with planning and the `get_weather` tool. |
| `weather_agent/agent_output.py` | Pydantic schema used to parse the model's step output. |
| `weather_agent/output_result.txt` | Captured sample output for revision. |

## Tool-Calling Lifecycle

```mermaid
sequenceDiagram
    participant U as User
    participant A as Agent
    participant O as OpenAI
    participant W as get_weather
    participant T as wttr.in

    U->>A: Ask about weather
    A->>O: System prompt, user request, schema
    O-->>A: START or PLAN
    A->>O: Continue with message history
    O-->>A: TOOL_CALL with city
    A->>W: Execute get_weather(city)
    W->>T: GET weather endpoint
    T-->>W: Conditions and temperature
    W-->>A: Tool result
    A->>O: Append TOOL_RESULT
    O-->>A: OUTPUT
    A-->>U: Print final response
```

## Agent State Model

```mermaid
stateDiagram-v2
    [*] --> START
    START --> PLAN
    PLAN --> PLAN: More planning
    PLAN --> TOOL_CALL: External data needed
    TOOL_CALL --> TOOL_RESULT: Tool executes
    TOOL_RESULT --> PLAN
    PLAN --> OUTPUT: Enough information
    OUTPUT --> [*]
```

## Run

Create an OpenAI API key in the environment or `.env` file expected by the OpenAI SDK. Run from the nested folder:

```powershell
cd weather_agent
python main.py
```

This runs the basic Responses API example. To run the tool-using agent:

```powershell
python agent.py
```

Enter a request such as:

```text
What is the weather in Delhi?
```

The agent may call `https://wttr.in/<city>?format=%C+%t` to fetch the current result.

## Key Design Ideas

- An agent is a model-driven loop, not just one model call.
- Structured output gives the application a predictable step contract.
- Tools extend the model with actions or data it cannot provide reliably by itself.
- Tool results must be added back to the conversation before the final response.
- The application, not the model, executes the Python tool.

## Current Limitations

- The tool call is selected from model text and parsed with `json.loads`.
- Network errors, timeouts, invalid cities, and non-JSON model output are handled only by the broad exception path.
- There is no maximum iteration count, so a production agent needs a loop guard.
- `get_weather` uses a public service and should not be treated as a guaranteed production data source.
- The system prompt contains several spelling mistakes and duplicated step labels, but the intended state flow is clear.

## Possible Extensions

- Add a maximum number of agent turns.
- Add explicit tool schemas and provider-native tool calling.
- Validate city input and set an HTTP timeout.
- Return structured final answers with source and retrieval time.
- Add logging, retries, and tests for each state transition.
