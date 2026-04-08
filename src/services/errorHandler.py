from fastapi import Request
from fastapi.responses import JSONResponse


async def global_Zero_Division_Handler(request: Request, exc: ZeroDivisionError):
    return JSONResponse(status_code=400, content={
        "status": "error",
        "message": "Division by Zero Detected"
    })


async def global_Value_Error_Handler(request: Request, exc: ValueError):
    if "math domain error" in str(exc):
        return JSONResponse(status_code=400, content={
            "status": "error",
            "message": "Math error: check your equation and range for invalid or nuanced operations like taking the square root of a negative number"
        })
    
    raise exc


async def global_type_error_handler(request: Request, exc: TypeError):
    if "complex" in str(exc):
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": "Math error: calculation resulted in complex numbers which cannot be compared or plotted."
                }
            )
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})