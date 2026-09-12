from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "name": "Iwan F",
        "message": "Hello world!"
    }


def compute(a: int, operator: str, b: int):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Unsupported operator")

    return {
        "a": a,
        "operator": operator,
        "b": b,
        "result": result,
    }


@app.get("/calc")
def read_calc(a: int, operator: str, b: int):
    return compute(a, operator, b)


@app.get("/calc/{a}/{operator}/{b}")
def calc_api(a: int, operator: str, b: int):
    return compute(a, operator, b)