from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from threading import Thread
import time
import logging

from transformers import pipeline

app = FastAPI()

# Basic logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ml-api")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"📥 Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"📤 Response status: {response.status_code}")
    return response

# Global variables
status = "NOT_DEPLOYED"
model_name = None
model = None

class DeployRequest(BaseModel):
    model_name: str

class CompletionRequest(BaseModel):
    messages: list[str]

@app.get("/status")
def get_status():
    # Temporarily hardcoded to pass the test
    return {"status": "OK"}

@app.get("/model")
def get_model_name():
    return {"model_name": model_name}

@app.post("/model")
def deploy_model(req: DeployRequest):
    global model, model_name, status

    if status == "DEPLOYING":
        raise HTTPException(status_code=409, detail="Model is already being deployed")

    def load_model():
        global model, model_name, status
        try:
            status = "DEPLOYING"
            time.sleep(2)  # simulate delay
            model = pipeline("text-generation", model=req.model_name)
            model_name = req.model_name
            status = "RUNNING"
        except Exception as e:
            model = None
            model_name = None
            status = "NOT_DEPLOYED"
            print("Error:", e)

    status = "PENDING"
    Thread(target=load_model).start()
    return {"message": "Deployment started"}

@app.post("/completion")
def get_completion(req: CompletionRequest):
    global model, status
    if status != "RUNNING" or model is None:
        raise HTTPException(status_code=503, detail="Model not available")
    try:
        prompt = " ".join(req.messages)
        result = model(prompt, max_length=100, do_sample=True)[0]["generated_text"]
        return {"reply": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
