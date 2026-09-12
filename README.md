# Initial FastAPI App for GitHub Codespaces

This repository is a small FastAPI project created to explore GitHub Codespaces and Visual Studio Code in a cloud development environment.

## Overview

The app exposes a simple Hello World route at `/` and a calculator endpoint at `/calc`.

```http
GET /calc?a=4&operator=%2B&b=2
```

It accepts an integer `a`, an operator (`+`, `-`, `*`, `/`), and an integer `b`, then returns a JSON payload like:

```json
{
  "a": 4,
  "operator": "+",
  "b": 2,
  "result": 6
}
```

The project is designed as an initial FastAPI app for learning how to develop, test, and run an API in a GitHub Codespace.

## Local usage

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the app with:

```bash
uvicorn main:app --reload
```

Then open the docs at:

http://127.0.0.1:8000/docs

## Testing

A small regression test checks the calculator route and the division-by-zero guard using `pytest`.

This branch is the passenger workspace branch for the initial FastAPI Codespaces exploration.
