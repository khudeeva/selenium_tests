import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    filename="test_log.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
def test_prompt_with_logging():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    logging.info("Открыта страница Java Script Alerts")

    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    logging.info("Нажата кнопка 'Click for JS Prompt'")
    
    alert = driver.switch_to.alert
    alert.send_keys("Тестовое сообщение")
    alert.accept()
    logging.info("В alert введено сообщение")

    try:
        result = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "result"))
        )
        assert result.text.strip() ==  "You entered: Тестовое сообщение"
        logging.info("Тестовое сообщение успешно найдено!")
    except Exception as e:
        logging.error("Тестовое сообщение не найдно! Сохраняю скриншот")
        driver.save_screenshot("error_text_msg.png")
        raise e
    finally:
        driver.quit()
    