def format_news_data(news_item):
    # Function to format news data into a standardized structure
    return {
        "title": news_item.get("title"),
        "link": news_item.get("link"),
        "published_date": news_item.get("published_date"),
        "source": news_item.get("source"),
    }

def handle_scraping_exception(exception):
    # Function to handle exceptions that occur during scraping
    print(f"An error occurred: {exception}")
    return {"error": str(exception)}