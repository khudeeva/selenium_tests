import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логов
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_invalid_login_with_logging_and_screenshot():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    logging.info("Открыта страница логина")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    logging.info("Введён неверный логин")

    driver.find_element(By.ID, "password").send_keys("wrongpass")
    logging.info("Введён неверный пароль")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    logging.info("Нажата кнопка входа")

    try:
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        assert "НЕПРАВИЛЬНЫЙ ТЕКСТ" in error.text
        logging.info("Ошибка отображается корректно")

    except Exception as e:
        logging.error("Ошибка не отобразилась. Сохраняю скриншот.")
        driver.save_screenshot("login_error.png")
        raise e

    driver.quit()
