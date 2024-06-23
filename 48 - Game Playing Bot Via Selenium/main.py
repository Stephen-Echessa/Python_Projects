from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()

# driver.get("https://www.standardmedia.co.ke/")
# smartphone = driver.find_element(by=By.CLASS_NAME, value="links")
# print(smartphone.text)

driver.get("https://www.python.org/")
event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_description = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_description[n].text
    }

print(events)
driver.quit()
