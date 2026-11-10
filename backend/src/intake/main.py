import uvicorn
def main() -> None:
    uvicorn.run("intake.api.app:app", host="127.0.0.1", port=8000, reload=True)