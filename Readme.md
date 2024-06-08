
# Crypto Scraper

This project provides a web scraper for cryptocurrency data from CoinMarketCap. It allows users to start scraping data for specific cryptocurrencies and view the scraping status.

## Key Features

- **Input Crypto Coins**: Users can input the names of cryptocurrencies they want to scrape data for.
- **Parallel Scraping**: The scraping process is performed using Celery in parallel to improve efficiency.
- **Comprehensive Data**: Provides various data about the cryptocurrency, including price, price change, market cap, volume, and other relevant information.
- **Database Storage**: Scraped data is saved in the database for future reference and analysis.

## Installation


1. Clone the repository:



![Alt text](home.png)

## Testing
<h2> API responses </h2>

<h3> Authentication </h3>

<b>User Registration</b> 
```json
{
 "token": {
"refresh": "ey.JhbGc101JIUzI1NilsInR5cCI6IkpXVCJ9.eyJ0b2t1b190eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzgwNDYwMywiaWF0IjoxNzEzNzE4MjAzLCJqdGk101I4MTA1MjVhZTJhN2Q0Yjg5ODYzMzQ3ZGFmYzU5Zjc4ZiIsInVzZXJfaWQ10jd9.Ygzn3pYBgZ0FNLV5j4U33_n10_qu1JUFwkigtUQN93k",
"access":
"ey.Jhbüc101JIUzI1NiIsInR5cCI6IkpXVC39.eyJ8b2t1b190eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzIwNjAzLC3pYXQ10jE3MTM3MTgyMDMsImp@a5161jFjMDc2Nzhh0WF1MzRhZjRhZjJk0GY1ZThmNjg0MTg5IiwidXNlc19pZCI6N38. X43R13XTxvpKTkR3eMNLaPxgaL152VgBfDG5FcMEq5g"

"msg": "Registration Success"
 }
}
```

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Testing](#testing)

## Installation

1. Clone the repository:
git clone <https://github.com/RSahu20/crypto>

2. Navigate to the project directory:
   
```bash
crypto/
├── crypto/
│ ├── init.py
│ ├── settings.py
│ ├── celery.py
│ ├── urls.py
│ └── wsgi.py
├── scraper/
├── requirements.txt
└── manage.py

```

3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4. Apply database migrations:
``` bash
python manage.py makemigrations
python manage.py migrate

```

## API Endpoints

List of API endpoints with brief descriptions, request methods, and example requests/responses.

| URL | Method    | Description                |
| :-------- | :------- | :------------------------- |
| `/api/taskmanager/start_scraping` | `POST` | **Initiates the scraping process for specific cryptocurrencies.** 
| `/api/taskmanager/scraping_status/<job_id>`      | `GET` | **Retrieves the status of the scraping process** |

|



## Database
Set up database for Mysql
``` bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Database Name',
        'USER': 'root',
        'PASSWORD': 'PASSWORD',
        'HOST':'localhost,
        'PORT':'3306',
    }
}
```







