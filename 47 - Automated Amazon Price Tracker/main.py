import requests
import smtplib
import os
from bs4 import BeautifulSoup

AMAZON_URL = 'https://www.amazon.com/Nintendo-Switch-OLED-Model-Neon-Joy/dp/B098RL6SBJ/ref=sr_1_3?crid=104RGPF0LYO6L&keywords=nintendo+switch&qid=1684319153&sprefix=ni%2Caps%2C1805&sr=8-3'

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
valid = True

price_input = ''
while valid:
    try:
        price_input = "{0:.2f}".format(float(input('How much you got for the given product? ')))
    except ValueError:
        print('Please input a valid number for the price')
        continue
    print(f"You chose ${price_input}")

    response = requests.get(AMAZON_URL, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find(class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
    price_str = price.find(class_='a-offscreen').get_text()
    price_float = "{0:.2f}".format(float(price_str.split('$')[1]))
    print(f"Product price is ${price_float}")

    product_title = soup.find(id='productTitle')
    title = product_title.get_text().strip()

    if float(price_float) < float(price_input):
        my_email = os.environ.get('EMAIL')
        password = os.environ.get('PASSWORD')

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="stevechessa@yahoo.com",
                            msg="Subject: Amazon Price Alert!\n"
                            f"{title} is now ${price_float}\n"
                            f"{AMAZON_URL}".encode('utf-8'))

        valid = False
    else:
        print("It appears that the product price isn't within the given range")
