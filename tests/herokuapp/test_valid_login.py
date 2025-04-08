from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# вход с корректным паролем и проверка welcome-сообщения
def test_login_valid():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    # вводим имя пользователя
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    # вводим корректный пароль
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    # нажимаем на кнопку логина
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # читаем сообщение об успешном входе
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text

    time.sleep(4)
    driver.quit()