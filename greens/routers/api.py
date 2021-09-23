from fastapi import APIRouter

from greens.routers.v1.vegs import router as vegs_api

router = APIRouter()

router.include_router(vegs_api, prefix="/vegs", tags=["vegetables"])
