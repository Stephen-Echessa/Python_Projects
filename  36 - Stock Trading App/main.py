import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}

news_parameters = {
    "q":COMPANY_NAME,
    "from":"2022-10-27",
    "sort_by":"popularity",
    "apiKey":NEWS_API_KEY
}

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
client = Client(ACCOUNT_SID, AUTH_TOKEN)


## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in stock_data.items()]
yesterday_stock = float(data_list[0]["4. close"])
print(yesterday_stock)
day_before_stock = float(data_list[1]["4. close"])
print(day_before_stock)
stock_difference = yesterday_stock - day_before_stock
percentage = round((stock_difference / day_before_stock) * 100)
print(f"{percentage}%")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
response = requests.get(NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
news_alerts = response.json()["articles"]
for news in news_alerts[:3]:
    title = news["title"]
    author = news["author"]
    description = news["description"]
    print(f"Title: {title}\nAuthor: {author}\nDescription: {description}\n\n")

    if percentage > 0:
        message = client.messages.create(
            body=f"TSLA: 🔺{percentage}%\nHeadline:{title}\nBrief:{description}\n",
            from_='+19295773684',
            to='+254782530870'
        )
    else:
        message = client.messages.create(
            body=f"TSLA: 🔻{percentage}%\nHeadline:{title}\nBrief:{description}\n",
            from_='+19295773684',
            to='+254782530870'
        )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

