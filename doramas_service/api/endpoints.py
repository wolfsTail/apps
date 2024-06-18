from fastapi import APIRouter, Depends

from doramas_service.service.doramas_servcie import DoramasService
from doramas_service.utils.depends import get_doramas_service_with_mockuow


router = APIRouter(prefix="/doramas")


@router.get("/")
async def get_all_doramas(service: DoramasService = Depends(get_doramas_service_with_mockuow)):
    return await service.all()
