from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from core.config import settings
import httpx

demo_router = APIRouter(tags=["Health Check"])

@demo_router.get("/health")
async def health_check():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"Demo app 2 running. Secret is : {settings.APP2_SECRET_KEY}"
    )

@demo_router.get("/health/app1")
async def health_check_app1():
    """This endpoint will check the status of App1
    which is running in another namespace i.e. other than the
    namespace of App2
    """
    try:
        app1_health_check_url = f"{settings.APP1_HOST}/health"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url=app1_health_check_url)
            if resp.status_code in [200]:
                return JSONResponse(
                        status_code=status.HTTP_200_OK,
                        content=f"Demo app 1 running."
                    ) 
        return JSONResponse(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=f"Some error occured!"
                    )
    except Exception as e:
        return JSONResponse(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=f"Some error occured! - {e}"
                    )