import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from src.limiter import limiter
from src.config import settings
from src.routes.routes import router


app = FastAPI(title="PlotWave API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [settings.LOCAL_URL, settings.PRODUCTION_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api")

@app.get("/")
@limiter.limit("5/minute")
async def root(request: Request):
    return {"message": "Welcome to PlotWave API. Visit /docs for Swagger UI."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

