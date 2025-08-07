from fastapi import FastAPI, Request, HTTPException
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pydantic import BaseModel
import logging
import time
import uuid
from config.logging_config import setup_graylog_logger

app = FastAPI(title="FaaS ETA Service")

logger = setup_graylog_logger("faas-eta")

class OrderData(BaseModel):
    items: list
    total: float
    
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    logger.info("Request started", extra={
        'event': 'request_start',
        'method': request.method,
        'path': request.url.path,
        'client_ip': request.client.host,
        'request_id': request_id
    })
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    
    logger.info("Request completed", extra={
        'event': 'request_end',
        'method': request.method,
        'path': request.url.path,
        'status_code': response.status_code,
        'duration_ms': round(duration * 1000, 2),
        'request_id': request_id
    })
    
    return response

@app.get("/")
async def root():
    logger.info("Health check accessed", extra={
        'event': 'health_check',
        'endpoint': '/'
    })
    return {"message": "FaaS ETA online"}

@app.post("/eta")
async def calculate_eta(order: OrderData):
    try:
        logger.info("Calculating ETA", extra={
            'event': 'eta_calculation_start',
            'endpoint': '/eta',
            'items_count': len(order.items),
            'order_total': order.total
        })
        
        local_zone = ZoneInfo("America/Guayaquil")
        hora = datetime.now(local_zone)
        eta = hora + timedelta(minutes=30)
        
        result = {"eta": eta.isoformat()}
        
        logger.info("ETA calculated successfully", extra={
            'event': 'eta_calculation_success',
            'endpoint': '/eta',
            'eta': result["eta"],
            'calculation_time': hora.isoformat()
        })
        
        return result
        
    except Exception as e:
        logger.error("Error calculating ETA", extra={
            'event': 'eta_calculation_error',
            'endpoint': '/eta',
            'error': str(e),
            'error_type': type(e).__name__
        })
        raise HTTPException(status_code=500, detail="Error calculating ETA")

