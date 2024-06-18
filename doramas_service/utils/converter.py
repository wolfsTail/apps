from pydantic import BaseModel


def pydantic_model_to_dict(model: BaseModel) -> dict:
    return model.model_dump()

def dict_to_pydantic_model(model: BaseModel,model_dict: dict) -> BaseModel:
    return model(**model_dict)
