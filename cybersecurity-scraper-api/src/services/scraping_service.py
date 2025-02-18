from typing import List
import time
import threading

class ScrapingService:
    def __init__(self):
        self.is_scraping = False
        self.scraping_thread = None

    def start_scraping(self, interval: int, target_function):
        if not self.is_scraping:
            self.is_scraping = True
            self.scraping_thread = threading.Thread(target=self._scraping_loop, args=(interval, target_function))
            self.scraping_thread.start()

    def _scraping_loop(self, interval: int, target_function):
        while self.is_scraping:
            target_function()
            time.sleep(interval)

    def stop_scraping(self):
        self.is_scraping = False
        if self.scraping_thread is not None:
            self.scraping_thread.join()