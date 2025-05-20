from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(level = logging.INFO, 
format = '%(asctime)s - %(levelname)s- %(message)s')

def test_invalid_password():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    logging.info("Открыта страницв логина")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    logging.info("Введен верный username")
    driver.find_element(By.ID, "password").send_keys("Superpassword!")
    logging.info("Введен неверный пароль")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    logging.info("Нажата кнопка Login")

    try:
        error_flash = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        assert "Your password is invalid!" in error_flash.text
        logging.info("Ошибка неверного пароля отображается корреткно")
    except Exception as e:
        logging.error("Ошибка неверного пароля не отобразилась. Сохраняю скриншот")
        driver.save_screenshot("invalid_password.png")
        raise e
    finally:
        driver.quit()

