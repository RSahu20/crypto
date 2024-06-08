import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://coinmarketcap.com/currencies/bitcoin/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # Extracting price
        price_elem = soup.find('span', class_='sc-d1ede7e3-0 fsQm base-text')
        price = price_elem.text.strip() if price_elem else "N/A"
        # exit()
        # Extracting market cap
        market_cap_elem = soup.find('div', class_='statsValue')
        market_cap = market_cap_elem.text.strip() if market_cap_elem else "N/A"

        # Extracting volume
        volume_elem = soup.find_all('div', class_='statsValue')
        volume = volume_elem[2].text.strip() if len(volume_elem) > 2 else "N/A"

        # Extracting circulating supply
        circulating_supply_elem = soup.find('div', class_='maxSupplyValue')
        circulating_supply = circulating_supply_elem.text.strip() if circulating_supply_elem else "N/A"

        # Print the scraped data
        print(f"Price: {price}")
        print(f"Market Cap: {market_cap}")
        print(f"Volume (24h): {volume}")
        print(f"Circulating Supply: {circulating_supply}")

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
