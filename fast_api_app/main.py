from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware

from src.core.app_config import app_config
from src.routes import router as methods_router

app = FastAPI(
        title="Мой API",
        description="Документация для моего API",
        version="1.0.0",
        contact={"name": "Admin", "email": "admin@example.com"},
        license_info={"name": "License"}
    )

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="./src/core/static"), name="static")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def greet():
    return {"message": "Привет, user!"}

app.include_router(methods_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=app_config.host, port=app_config.port)





