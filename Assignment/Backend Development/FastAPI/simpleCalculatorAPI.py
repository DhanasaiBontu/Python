from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract")
async def subtract(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply")
async def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide")
async def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Denominator cannot be zero"
        )
    return {"result": a / b}