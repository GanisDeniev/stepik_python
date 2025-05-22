from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "#num1.nowrap")
    b = browser.find_element(By.CSS_SELECTOR, "#num2.nowrap")
    result = int(a.text) + int(b.text)
    print(int(a.text), " + ", int(b.text), " = ", result)

    select = Select(browser.find_element(By.ID, "dropdown"))
    value = select.select_by_visible_text(str(result))
    time.sleep(1)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()