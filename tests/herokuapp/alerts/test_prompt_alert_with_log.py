import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

logging.basicConfig(
    filename="test_log.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
def test_prompt_alert_with_log():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    logging.info("Открыта страница JavaScript Alerts")

    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    logging.info("Нажата кнопка Click for JS Prompt")

    alert = driver.switch_to.alert
    alert.send_keys("Автотест")
    alert.accept()
    logging.info("В alert введено сообщение")

    try:
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert message.text.strip() == "You entered: Автотест"
        logging.info("Успешно найдено сообщение")
    except Exception as e:
        logging.error("Сообщение не найдено. Сохраняю скриншот.")
        driver.save_screenshot("message.png")
        raise e
    finally:
        driver.quit()


