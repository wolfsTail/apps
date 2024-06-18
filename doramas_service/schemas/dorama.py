from pydantic import BaseModel, ConfigDict


class BaseDorama(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    year: int
    genres: list[str] | None
    casts: list[str] | None

class DoramaToCreate(BaseDorama):
    pass

class DoramaFromDB(BaseDorama):
    id: int

class DoramaToUpdate(BaseDorama):
    title: str | None
    year: int | None
