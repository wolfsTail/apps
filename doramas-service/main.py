from fastapi import FastAPI


app = FastAPI(
    title="Doramas Service",
    version="0.0.1",
    description="Doramas service API",
    docs_url="/docs",
)


@app.get("/")
async def root():
    return {"message": "It's a root url!"}
