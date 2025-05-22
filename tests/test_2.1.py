from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_chest = browser.find_element(By.ID, "input_value")
    x = x_chest.text
    print("Найдена переменная Х: ", x)
    result = math.log(abs(12 * math.sin(int(x))))
    print("Результат = ", result)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radiobutton_robot = browser.find_element(By.CSS_SELECTOR, "input[value='robots']")
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)

    #time.sleep(2)
    field.send_keys(result)
    #time.sleep(1)
    checkbox.click()
    #time.sleep(1)
    radiobutton_robot.click()
    #time.sleep(1)
    submit.click()

finally:
    time.sleep(10)
    browser.quit()