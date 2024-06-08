from celery import shared_task
from .webscrap import CoinMarketCap

@shared_task
def coins_scrap(coin, job_id):
    scraper = CoinMarketCap(coin, job_id)
    return scraper.scrape_data()
