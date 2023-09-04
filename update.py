import logging
import time

from base import Crawler
from settings import CONFIG

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)


crawler = Crawler()

if __name__ == "__main__":
    while True:
        try:
            crawler.crawl_page(f"{CONFIG.CHILLTO123_TVSHOWS_PAGE}/")
            crawler.crawl_page(f"{CONFIG.CHILLTO123_MOVIES_PAGE}/")
        except Exception as e:
            pass
        time.sleep(CONFIG.WAIT_BETWEEN_LATEST)