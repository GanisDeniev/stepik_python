from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    trolling_button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    trolling_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_chest = browser.find_element(By.ID, "input_value")
    x = x_chest.text
    print("Найдена переменная Х: ", x)
    result = math.log(abs(12 * math.sin(int(x))))
    print("Результат = ", result)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()