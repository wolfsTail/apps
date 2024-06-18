from fastapi import APIRouter, Depends, HTTPException, status

from doramas_service.service.doramas_servcie import DoramasService
from doramas_service.utils.depends import get_doramas_service_with_mockuow
from doramas_service.utils.converter import pydantic_model_to_dict, dict_to_pydantic_model
from doramas_service.schemas import DoramaFromDB, DoramaToCreate, DoramaToUpdate


router = APIRouter(prefix="/doramas", tags=["doramas"])


@router.get("/")
async def get_all_doramas(
    service: DoramasService = Depends(get_doramas_service_with_mockuow)
    ) -> list[DoramaFromDB]:
    data_with_dicts = await service.all()
    data_with_pydantic_models = []
    for key in data_with_dicts:
        data_with_pydantic_models.append(dict_to_pydantic_model(
            model=DoramaFromDB, model_dict=data_with_dicts[key]
        ))
    return data_with_pydantic_models    

@router.get("/{id}")
async def get_dorama_by_id(
    id: int, service: DoramasService = Depends(get_doramas_service_with_mockuow)
    ) -> DoramaFromDB:
    try:
        current = await service.get(id=id)
        current_model = dict_to_pydantic_model(
            model=DoramaFromDB, model_dict=current
        )
        return current_model
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dorama not found")

@router.post("/")
async def add_dorama(
    dorama: DoramaToCreate, service: DoramasService = Depends(get_doramas_service_with_mockuow)
    ) -> dict:
    added_dorama = await service.create(dorama=pydantic_model_to_dict(dorama))
    added_dorama = dict_to_pydantic_model(model=DoramaFromDB, model_dict=added_dorama)
    context = {
        "message": "Dorama added successfully",
        "dorama": added_dorama
    }
    return context

@router.patch("/{id}")
async def update_dorama(
    id: int, dorama: DoramaToUpdate, service: DoramasService = Depends(get_doramas_service_with_mockuow)
    ) -> dict:
    try:
        updated_dorama = await service.update(item_id=id, item=pydantic_model_to_dict(dorama))
        updated_dorama = dict_to_pydantic_model(model=DoramaFromDB, model_dict=updated_dorama)
        context = {
            "message": "Dorama updated successfully",
            "dorama": updated_dorama
        }
        return context
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dorama not found")

@router.delete("/{id}")
async def delete_dorama(
    id: int, service: DoramasService = Depends(get_doramas_service_with_mockuow)
    ) -> dict:
    try:
        await service.delete(item_id=id)
        context = {
            "message": f"Dorama with {id} deleted successfully",
        }
        return context
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deleted dorama not found")
