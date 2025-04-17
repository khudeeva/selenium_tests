import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    filename="test_log.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
def test_prompt_dismiss_negative_log():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    logging.info("Открыта страница JavaScript Alerts")

    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    logging.info("Нажата кнопка Click for JS Prompt")

    alert = driver.switch_to.alert
    alert.send_keys("Негативный тест")
    alert.dismiss()
    logging.info("Введен тест, нажато Cancel")

    try:
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )
        assert result.text.strip() == "You entered: null"
        logging.info("Сообщение не появилось, так и должно быть")
    except Exception as e:
        logging.error("Сообщение появилось! Сохраняю скриншот")
        driver.save_screenshot("result.png")
        raise e
    finally:
        driver.quit()