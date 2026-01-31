from fastapi import FastAPI, HTTPException

app = FastAPI(title="v05.03 Calculadora API")

@app.get("/")
def root():
    return {
        "message": "v05.03 API de Calculadora no ar",
        "operations": ["soma", "subtracao", "multiplicacao", "divisao"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}


@app.get("/soma3")
def soma3(a: float, b: float, c: float):
    return {"resultado": a + b + c}

@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divisao")
def divisao(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Divisao por zero nao permitida")
    return {"resultado": a / b}
