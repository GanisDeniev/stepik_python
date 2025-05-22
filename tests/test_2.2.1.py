from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in field:
        element.send_keys("jija")
    
    file_path = file_path = os.path.join(current_dir, 'zalupa.txt') 
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()


finally:
    time.sleep(5)
    browser.quit()