from fastapi import APIRouter
from typing import List, Dict

router = APIRouter()

class NewsController:
    @router.get("/news/latest", response_model=List[Dict])
    async def get_latest_news(self):
        """
        Fetch the latest news related to cyber threats.
        """
        # Logic to fetch latest news will be implemented here
        # Example logic to fetch latest news
        latest_news = [
            {"title": "New Cyber Threat Emerges", "description": "A new cyber threat has been identified..."},
            {"title": "Cybersecurity Tips", "description": "Here are some tips to stay safe online..."}
        ]
        return latest_news
        pass

    @router.get("/news/category/{category}", response_model=List[Dict])
    async def get_news_by_category(self, category: str):
        """
        Fetch news related to a specific category of cyber threats.
        """
        # Logic to fetch news by category will be implemented here
        # Example logic to fetch news by category
        news_by_category = [
            {"title": "New Cyber Threat Emerges", "description": "A new cyber threat has been identified..."},
            {"title": "Cybersecurity Tips", "description": "Here are some tips to stay safe online..."}
        ]
        pass

# Include the router in the main API application in api.py
# from src.controllers.news_controller import router as news_router
# app.include_router(news_router)