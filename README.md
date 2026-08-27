# Python Learning

This repository is for learning and practicing Python through small, focused examples. Each example explores a language feature, standard-library module, or common programming concept that can be run and modified while learning.

## Topics

- Python practice examples in `main.py`
- Threading and concurrent programming
- Multiprocessing
- The Global Interpreter Lock (GIL)
- Thread and process synchronization with locks
- Communication with process queues and shared values
- Asynchronous programming with `asyncio`

## Project Structure

```text
12_thread_concurency/  Threading and multiprocessing examples
13_asyncio/            Async programming examples
main.py                Main practice file
```

## Getting Started

The project requires Python 3.12 or newer. Create and activate a virtual environment, install the dependencies, and run an example:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -e .
python 13_asyncio/01_asyncio.py
```

You can run any example directly with Python and experiment with the code as you learn.
