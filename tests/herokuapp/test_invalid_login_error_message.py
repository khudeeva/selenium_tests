from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login_error_message():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    # вводим верный логин и неверный пароль
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # ждем появления сообщения
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "Your password is invalid!")
    )


    # проверяем сообщение об ошибке
    error_message = driver.find_element(By.ID, "flash")
    assert "Your password is invalid!" in error_message.text.strip()

  
    driver.quit()
