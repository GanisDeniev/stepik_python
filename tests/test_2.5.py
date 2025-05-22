from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:

    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_chest = browser.find_element(By.ID, "input_value")
    x = x_chest.text
    print("Найдена переменная Х: ", x)
    result = math.log(abs(12 * math.sin(int(x))))
    print("Результат = ", result)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button#solve")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()