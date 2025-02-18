# Cybersecurity Scraper API

This project is a FastAPI application that continuously scrapes data from dynamic websites to provide up-to-date news and information about cyber threats and cybersecurity.

## Project Structure

```
cybersecurity-scraper-api
├── src
│   ├── api.py               # Entry point of the FastAPI application
│   ├── scraper.py           # Main logic for scraping data from dynamic websites
│   ├── controllers
│   │   └── news_controller.py # Handles API requests related to news and cyber threats
│   ├── services
│   │   └── scraping_service.py # Manages scraping tasks
│   └── utils
│       └── helpers.py       # Utility functions for various tasks
├── requirements.txt          # Lists project dependencies
├── README.md                 # Documentation for the project
└── .env                      # Environment variables for sensitive information
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cybersecurity-scraper-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your environment variables in the `.env` file.

## Usage

To run the FastAPI application, execute the following command:
```
uvicorn src.api:app --reload
```

## API Endpoints

- **GET /news/latest**: Fetch the latest news about cyber threats.
- **GET /news/category/{category}**: Fetch news articles filtered by category.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.