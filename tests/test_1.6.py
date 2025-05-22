from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #name_field = browser.find_element(By.CSS_SELECTOR, ".first.form-control")
    #surname_field = browser.find_element(By.CSS_SELECTOR, ".second.form-control")
    #email_field = browser.find_element(By.CSS_SELECTOR, ".third.form-control")

    #name_field.send_keys("Нюхай")
    #time.sleep(2)
    #surname_field.send_keys("Бебру")
    #time.sleep(2)
    #email_field.send_keys("jija@mail.ru")
    #time.sleep(2)

    required_fields = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in required_fields:
        element.send_keys("bebra")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    try:
        assert "Congratulations! You have successfully registered!" == welcome_text, "Лох, не работает"
        print("Зайбыс, работает")
    except AssertionError as e:
        print(e)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()