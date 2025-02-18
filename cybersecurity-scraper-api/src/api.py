from fastapi import FastAPI
from controllers.news_controller import NewsController

app = FastAPI()

news_controller = NewsController()

@app.get("/news/latest")
async def get_latest_news():
    return await news_controller.get_latest_news()

@app.get("/news/category/{category}")
async def get_news_by_category(category: str):
    return await news_controller.get_news_by_category(category)