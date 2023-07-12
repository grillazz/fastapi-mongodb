from fastapi import APIRouter

from app_name.routers.v1.usuarios import router as usuarios

router = APIRouter()

router.include_router(usuarios, prefix="/usuarios", tags=["usuarios"])
