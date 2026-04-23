from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def simple_get():
    return {"message": "Hello from FastAPI"}
@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.get("/info")
def info():
    return {"app": "devops-test",
            "version": "1.0.0",
            "port": 8000}