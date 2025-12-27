from fastapi import FastAPI
import os

app = FastAPI(title="GuardianAI ML Service", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy", "message": "GuardianAI ML Service is running"}

@app.get("/")
def root():
    return {"message": "GuardianAI ML Service", "docs": "/docs"}

@app.post("/fraud-check")
def fraud_check(data: dict):
    return {
        "transaction_id": data.get("transaction_id", "test"),
        "risk_score": 15.0,
        "action": "ALLOW",
        "message": "Service deployed successfully"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))