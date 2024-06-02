from fastapi import FastAPI
from app.api import endpoints
from fastapi.responses import RedirectResponse

app = FastAPI()
app = FastAPI(title="Agentic Reports (v0.01)")

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

app.include_router(endpoints.router)
