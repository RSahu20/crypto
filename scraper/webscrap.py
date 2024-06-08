from django.shortcuts import render
from celery import shared_task
import requests
from bs4 import BeautifulSoup
import re
from .models import *


class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self, coin, job_id):
        self.coin = coin
        self.url = f"{self.BASE_URL}{coin}/"
        self.job_id = job_id

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def scrape_data(self):
        try:
            page_content = self.fetch_page()
            soup = BeautifulSoup(page_content, 'html.parser')
            price = soup.find('span', class_='sc-d1ede7e3-0 fsQm base-text').text
            price_change = soup.select_one('#section-coin-overview > div:nth-of-type(2) > div > div > p').text
            market_capital = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(1) > div:nth-of-type(1) > dd').text
            market_capital_rank = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(1) > div:nth-of-type(2) > div > span').text
            volume = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(2) > div:nth-of-type(1) > dd').text
            volume_rank = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(2) > div:nth-of-type(2) > div > span').text
            volume_change = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(3) > div > dd').text
            circulating_supply = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(4) > div > dd').text
            total_supply = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(5) > div > dd').text
            diluted_market_cap = soup.select_one('#section-coin-stats > div > dl > div:nth-of-type(7) > div > dd').text
            cont_name = soup.select_one('section:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div > div > a > span:nth-of-type(1)').text
            cont_address = soup.select_one('section:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > a')['href']

            price1 = float(re.sub(r'[^0-9.]', '', price))
            price_change1 = float(re.sub(r'[^0-9.]', '', price_change.split('%')[-2]))
            market_capital1 = market_capital.split('$')[-1]
            market_capital_rank1 = int(re.sub(r'[^0-9.]', '', market_capital_rank))
            volume1 = float(re.sub(r'[^0-9.]', '', volume.split('$')[-1]))
            volume_rank1 = int(re.sub(r'[^0-9.]', '', volume_rank))
            volume_change1 = float(re.sub(r'[^0-9.]', '', volume_change))
            circulating_supply1 = circulating_supply.split(' ')[-2]
            total_supply1 = total_supply.split(' ')[-2]
            diluted_market_cap1 = re.sub(r'[^0-9.]', '', diluted_market_cap)
                
            scrap = Scrapping_Details.objects.create(
                job_obj=self.job_id, coin=self.coin, price=price1, price_change=price_change1,
                market_cap=market_capital1, market_cap_rank=market_capital_rank1, volume=volume1,
                volume_rank=volume_rank1, volume_change=volume_change1, circulating_supply=circulating_supply1,
                total_supply=total_supply1, diluted_market_cap=diluted_market_cap1
            )
                
            Contracts.objects.create(
                scraping_details=scrap, name=cont_name, address=cont_address.split('/')[-1]
            )

            official_links_element = soup.select_one('section:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div')
            links = official_links_element.find_all('a')
            for link in links:
                href = link['href']
                text = link.text
                Official_Links.objects.create(scraping_details=scrap, name=text, link=href)

            socials_element = soup.select_one('section:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(3) > div:nth-of-type(2) > div')
            links1 = socials_element.find_all('a')
            for link1 in links1:
                href = link1['href']
                text = link1.text
                Socials.objects.create(scraping_details=scrap, name=text, link=href)

        except Exception as e:
            scrap = Scrapping_Details.objects.create(job_obj=self.job_id, coin=self.coin)

        data = {'id': self.job_id.job_id}
        return data
