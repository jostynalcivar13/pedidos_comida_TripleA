from fastapi import FastAPI
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo 
from pydantic import BaseModel

app = FastAPI()

class OrderData(BaseModel):
    items: list
    total: float

@app.get("/")
async def root():
    return {"message": "FaaS ETA online"}

@app.post("/eta")
async def calculate_eta(order: OrderData):
    local_zone = ZoneInfo("America/Guayaquil")

    hora = datetime.now(local_zone)
    eta = hora + timedelta(minutes=30)

    return {
        "eta": eta.isoformat()
    }
