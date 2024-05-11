from fastapi import FastAPI
from core.config import settings
from demo_router.api.v1.endpoints import demo_router as demo_router_v1

app = FastAPI(
    title=settings.SERVICE_NAME
)

app.include_router(router=demo_router_v1)

