import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


link = driver.get("https://suninjuly.github.io/registration2.html")
try:

    name = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    surname = driver.find_element(
        By.XPATH, '//input[@placeholder="Input your last name"]'
    ).send_keys("Petrov")
    email = driver.find_element(
        By.XPATH, '//input[@placeholder="Input your email"]'
    ).send_keys("1111@2222.33")
    button = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    driver.quit()
