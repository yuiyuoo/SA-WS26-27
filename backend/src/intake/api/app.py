from fastapi import FastAPI

app = FastAPI(title="Intake")

@app.get("/")
def home()->dict[str,str]:
    return {"home": "ok "}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}