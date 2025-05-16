from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def test_login_invalid_data():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    logging.info("Открыта страница логина")

    driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("tomsmith")
    logging.info("Введен верный логин")
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("SuperSecret!")
    logging.info("Введен неверный пароль")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    logging.info("Нажата кнопка входа")
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "flash"), "Your password is invalid!")
        )
        error_message = driver.find_element(By.ID, "flash")
        assert "Your password is invalid!" in error_message.text.strip()
        logging.info("Ошибка отображается корреткно")
    
    except Exception as e:
        logging.error("Ошибка не отображается, сохраняю скриншот")
        driver.save_screenshot("login_invalid_data.png")
        raise e
    driver.quit()
    logging.info("Тест завершён")
