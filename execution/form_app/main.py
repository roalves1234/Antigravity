from fastapi import FastAPI
from execution.form_app.controllers.form_controller import router as form_router

app = FastAPI(title="Web Form API")

app.include_router(form_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("execution.form_app.main:app", host="0.0.0.0", port=8000, reload=True)
