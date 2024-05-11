from demo_router.api.v1.v1 import v1_router
from fastapi import FastAPI

app = FastAPI(
    title="K8S App Test"
)

app.include_router(v1_router)