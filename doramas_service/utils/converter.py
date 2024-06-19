from pydantic import BaseModel


def pydantic_model_to_dict(model: BaseModel) -> dict:
    return model.model_dump()

def dict_to_pydantic_model(model: BaseModel,model_dict: dict) -> BaseModel:
    return model(**model_dict)

def dicts_to_list_of_pydantic_models(model: BaseModel, model_dicts: dict[dict]) -> list[BaseModel]:
    list_with_pydantic_models = []
    for key in model_dicts:
        list_with_pydantic_models.append(dict_to_pydantic_model(
            model=model, model_dict=model_dicts[key]
        ))
    return list_with_pydantic_models
