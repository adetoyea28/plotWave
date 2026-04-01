from fastapi import APIRouter, Request
from src.limiter import limiter
from src.services.processor import processFunction

router = APIRouter()

@router.get('/health')
async def healthCheck():
    return {
        "msg": "healthy"
    }


@router.post('/solve-function')
@limiter.limit("25/minute")
async def solveFunction(request: Request, function: str = 'x^2', start: int = -10, stop: int = 10, interval: int = 1):
    data = processFunction(function, start, stop, interval)
    return {
        "status": "success",
        "data": data[0],
        "y_max": data[1],
        "y_min": data[2]
    }