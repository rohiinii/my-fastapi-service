from fastapi import FastAPI

app = FastAPI(title="My Service", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": app.title, "version": app.version}
