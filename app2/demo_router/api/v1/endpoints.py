from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

demo_router = APIRouter(tags=["Health Check"])

@demo_router.get("/health")
async def health_check():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="Demo app 2 running"
    )