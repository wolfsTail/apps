from pydantic import BaseModel


def pydantic_model_to_dict(model: BaseModel) -> dict:
    return model.model_dump()
