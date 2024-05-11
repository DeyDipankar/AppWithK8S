from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

demo_router = APIRouter()

@demo_router.get("/healthcheck")
async def health_check():
    return JSONResponse(
        status_code=status. HTTP_200_OK,
        content="Demo Router 1 running.."
    )