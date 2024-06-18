from fastapi import FastAPI

from doramas_service.api import router


app = FastAPI(
    title="Doramas Service",
    version="0.0.1",
    description="Doramas service API",
    docs_url="/docs",
)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "It's a root url!"}
