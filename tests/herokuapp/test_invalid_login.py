from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# вход с корректным паролем и проверка welcome-сообщения
def test_login_valid():
    # создаем драйвер
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    # вводим имя пользователя
    username = driver.find_element(By.ID, "username").send_keys("tomsmith")

    # вводим неверный пароль
    password = driver.find_element(By.ID, "password").send_keys("wrongPassword")
    
    # ждем пока кнопка станет кликабельной и нажимаем
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # ждем, что остались на Login(не было редиректа)
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )

    # ждем появления текста ошибки
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "Your password is invalid!")
    )
    # читаем сообщение об ошибке:
    error_message = driver.find_element(By.ID, "flash")
    assert "Your password is invalid!" in error_message.text

    
    driver.quit()