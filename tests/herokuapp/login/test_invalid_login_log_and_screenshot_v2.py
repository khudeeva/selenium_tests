import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# настройка логов
logging.basicConfig(
    filename="test_log.log",
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_invalid_login_log_and_screenshot_v2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    logging.info("Открыта страница логина")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    logging.info("Введен корректный username")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    logging.info("Введен некорреткный password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    logging.info("Нажата кнопка 'Login'")
    
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        assert "Your password is invalid!" in error_message.text
        logging.info("Сообщение об ошибке успешно найдено")
    except Exception as e:
        logging.error("Ошибка не отобразилась или текст не совпал! Сохраняю скриншот.")
        driver.save_screenshot("invalid_login.png")
        raise e

    finally:
        driver.quit()