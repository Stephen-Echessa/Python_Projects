from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles_number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# articles_number.click()

source = driver.find_element(by=By.LINK_TEXT, value="View source")
source.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
