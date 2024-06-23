from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")


def buy_upgrades():
    store_list = []
    prize_list = []
    price_list = []

    store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    for upgrade in store:
        store_list.append(upgrade.text.strip())

    store_list = [i for i in store_list if i]
    money = driver.find_element(by=By.ID, value="money")
    budget = int(money.text)

    for value in store_list:
        split_value = value.split(' - ')
        prize_list.append(split_value[0])
        price_list.append(int(split_value[1].replace(",", "")))

    budgeted_list = [price for price in price_list if budget > price]

    try:
        maximum_value = max(budgeted_list)
        index = budgeted_list.index(maximum_value)
        prize = driver.find_element(by=By.ID, value=f"buy{prize_list[index]}")
        prize.click()
    except ValueError:
        pass


def cookie_click_timer():
    should_continue = True
    timeout = time.time() + 60*5
    upgrade_timer = time.time() + 5

    while should_continue:
        cookie.click()
        if time.time() > upgrade_timer:
            buy_upgrades()
            upgrade_timer += 5
        if time.time() > timeout:
            cps = driver.find_element(by=By.ID, value="cps")
            print(cps.text)
            should_continue = False


cookie_click_timer()
