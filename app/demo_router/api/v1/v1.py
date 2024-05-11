from demo_router.api.v1 import demo1
from fastapi import APIRouter

v1_router = APIRouter(
    prefix="/v1"
)

v1_router.include_router(router=demo1.demo_router, prefix="/demo1")