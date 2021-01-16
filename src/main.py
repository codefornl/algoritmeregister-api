from fastapi import FastAPI, Request, Response
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from .config import settings, database
from .routers import algorithm, organisation, process
app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Algoritmeregister-api",
        version="0.0.1",
        description="This is the API for Algoritmeregister",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = database.SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS_CSV.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers moved to individual files in the ./routers folder
app.include_router(algorithm.router)
app.include_router(organisation.router)
app.include_router(process.router)

app.openapi = custom_openapi