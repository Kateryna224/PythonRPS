from fastapi import FastAPI
from routers import game, items  

app = FastAPI()

# Подключаем роутеры
app.include_router(game.router, prefix="/game", tags=["Game"])
app.include_router(items.router, prefix="/items", tags=["Items"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
