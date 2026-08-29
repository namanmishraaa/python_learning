# Python Learning

This repository is for learning and practicing Python through small, focused examples. Each example explores a language feature, standard-library module, or common programming concept that can be run and modified while learning.

## Topics

- Python fundamentals and practice examples in `main.py`
- Threading and concurrent programming
- Multiprocessing and process communication
- The Global Interpreter Lock (GIL)
- Thread and process synchronization with locks
- Race conditions and deadlocks
- Daemon and non-daemon threads
- Background workers
- Asynchronous programming with `asyncio`
- Running blocking functions in async code with `ThreadPoolExecutor`
- Comparing asyncio, multithreading, and multiprocessing

## Project Structure

```text
12_thread_concurency/  Threading and multiprocessing examples
13_asyncio/            Asyncio, threads, processes, and synchronization examples
main.py                Main practice file
```

## Asyncio Practice

The [asyncio README](13_asyncio/README.md) contains a detailed guide to asynchronous programming, the event loop, coroutines, tasks, `asyncio` APIs, blocking code, and the differences between asyncio, multithreading, and multiprocessing.

Recent exercises in `13_asyncio/` include:

- `01_asyncio_one.py` - running a coroutine with `asyncio.run()`
- `02_async_two.py` - running multiple coroutines with `asyncio.gather()`
- `03_async_three.py` - making concurrent HTTP requests with `aiohttp`
- `04_thread_async.py` - running blocking work with `ThreadPoolExecutor`
- `05_process_asyn.py` - combining async code with a process executor
- `06_bgworker.py` - creating an asynchronous background worker
- `07_daemon.py` and `08_non_deamon.py` - daemon and non-daemon thread behavior
- `09_race_condition.py` - observing a race condition
- `10_deadlock.py` - observing a deadlock caused by opposite lock order

## Getting Started

The project requires Python 3.12 or newer. Create and activate a virtual environment, install the dependencies, and run an example:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -e .
python 13_asyncio/01_asyncio_one.py
```

You can run any example directly with Python and experiment with the code as you learn. If you use `uv`, run an example from the repository root with:

```bash
uv sync
uv run 13_asyncio/03_async_three.py
```

## Git Ignore Rules

Python bytecode cache directories are excluded from commits through [.gitignore](.gitignore), including every `__pycache__/` directory in the project.
