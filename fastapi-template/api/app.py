from api.test_section import router as test_section_router
from fastapi import FastAPI

app = FastAPI(title="<Your API Name>")

app.include_router(test_section_router)
