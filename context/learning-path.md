# Learning Path — Python Coding Curriculum

This maps every concept Zach will learn, organised into phases. Each phase builds on the last. Every concept is taught through the stock portfolio optimiser project — no detached exercises.

---

## Phase 1: Foundations (Lessons 1–5)

**Goal:** Get a working Python environment, understand basic syntax, and fetch stock data.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 1 | Terminal basics, Python installation, what is a REPL, running a .py file | Run `python main.py` and see "Hello World" |
| 2 | Virtual environments (venv), pip, requirements.txt, why isolation matters | Create venv, install yfinance & pandas |
| 3 | Variables, data types (str, int, float, bool), print(), f-strings, comments | Store a ticker name, print formatted output |
| 4 | Lists, indexing, slicing, for loops, len(), range() | Store multiple tickers, loop through them |
| 5 | Functions (def, parameters, return), scope, docstrings | Write `fetch_prices(ticker, start_date)` function |

**Concepts covered:** terminal, REPL, scripts, venv, pip, variables, types, strings, lists, loops, functions

---

## Phase 2: Working with Data (Lessons 6–10)

**Goal:** Fetch, process, and understand stock data using pandas.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 6 | Dictionaries, tuples, sets — when to use each | Map ticker → price data |
| 7 | Imports, modules, standard library, third-party packages | Organise code into modules |
| 8 | pandas Series & DataFrame basics, .head(), .tail(), indexing | Work with price DataFrames |
| 9 | pandas operations: .pct_change(), .mean(), .std(), .corr(), .cov() | Calculate daily returns, volatility, correlation |
| 10 | File I/O: reading/writing CSV, JSON. pathlib for paths | Save/load cached price data |

**Concepts covered:** dicts, tuples, sets, imports, modules, pandas, file I/O, pathlib

---

## Phase 3: Core Logic & OOP (Lessons 11–16)

**Goal:** Build the optimiser engine using classes and numpy.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 11 | numpy arrays, vectorised operations, dot product, matrix math | Calculate portfolio return & risk with numpy |
| 12 | Conditionals (if/elif/else), comparison operators, truthiness | Validate inputs (e.g. weights sum to 1) |
| 13 | Error handling: try/except/finally, raising exceptions, custom exceptions | Handle bad tickers, network errors |
| 14 | Classes & OOP: __init__, self, methods, attributes | Create `Portfolio` and `Asset` classes |
| 15 | OOP continued: inheritance, @property, __repr__, __str__ | Add `OptimisedPortfolio` subclass |
| 16 | List comprehensions, dict comprehensions, generator expressions | Clean up loops into Pythonic one-liners |

**Concepts covered:** numpy, conditionals, error handling, OOP, classes, inheritance, comprehensions

---

## Phase 4: The Efficient Frontier (Lessons 17–21)

**Goal:** Implement Monte Carlo simulation and scipy optimisation.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 17 | Random number generation, Monte Carlo simulation concept | Generate 10,000 random portfolios |
| 18 | scipy.optimize.minimize, constraints, bounds | Find the minimum variance portfolio |
| 19 | The Efficient Frontier: theory and implementation | Trace the efficient frontier curve |
| 20 | Sharpe Ratio, risk-free rate, Capital Market Line | Find the max Sharpe ratio portfolio |
| 21 | matplotlib & plotly: scatter plots, lines, annotations | Plot the efficient frontier with key portfolios marked |

**Concepts covered:** Monte Carlo, scipy optimisation, constraints, Sharpe ratio, matplotlib, plotly

---

## Phase 5: Performance & Concurrency (Lessons 22–26)

**Goal:** Make it fast with multithreading, multiprocessing, and async.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 22 | Timing code, profiling, Big-O notation basics | Benchmark the current optimiser |
| 23 | Threading: Thread, ThreadPoolExecutor, GIL explained | Parallel data fetching for multiple tickers |
| 24 | Multiprocessing: Process, Pool, ProcessPoolExecutor | Parallel Monte Carlo simulations across CPU cores |
| 25 | concurrent.futures: map, as_completed, future objects | Unified interface for thread/process pools |
| 26 | async/await, asyncio, aiohttp (optional advanced) | Async data fetching |

**Concepts covered:** profiling, Big-O, threading, GIL, multiprocessing, concurrent.futures, async

---

## Phase 6: Production Quality (Lessons 27–32)

**Goal:** Make the code professional, testable, and deployable.

| Lesson | Concepts Taught | Project Milestone |
|--------|----------------|-------------------|
| 27 | Type hints, mypy, why types matter | Add type annotations to all functions |
| 28 | Testing: pytest, unit tests, fixtures, mocking | Test the optimiser logic |
| 29 | CLI design: argparse or click | Run from terminal: `python -m portfolio AAPL GOOGL MSFT` |
| 30 | Logging: logging module vs print(), log levels | Replace prints with proper logging |
| 31 | Project packaging: __main__.py, pyproject.toml, entry points | Install as a proper package |
| 32 | Decorators, context managers, advanced Pythonic patterns | Add @timer decorator, use `with` for file handling |

**Concepts covered:** type hints, testing, CLI, logging, packaging, decorators, context managers

---

## Phase 7: Stretch Goals (Lessons 33+)

| Topic | What It Teaches |
|-------|----------------|
| Caching with Redis or shelve | Persistence, key-value stores |
| Web dashboard with Streamlit | Web frameworks, reactive UI |
| Database storage with SQLite | SQL, ORM (SQLAlchemy) |
| REST API with FastAPI | HTTP, APIs, request/response |
| Docker containerisation | Containers, deployment |
| CI/CD with GitHub Actions | Automation, testing pipelines |
| Machine learning portfolio models | scikit-learn, ML basics |

---

## Progress Tracking

Each lesson should be marked as complete once Zach:
1. Understands the concept (can explain it back)
2. Has written working code using it
3. Code is committed to git

Current lesson: **Lesson 5 — Functions (in progress)**

---

_This curriculum is flexible. If Zach grasps concepts quickly, lessons can be combined. If something needs more time, a lesson can be split across sessions._
