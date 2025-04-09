from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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

    # ждем появление нужного текста
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "You logged into a secure area!")
    )

    # читаем сообщение об успешном входе
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text

    driver.quit()