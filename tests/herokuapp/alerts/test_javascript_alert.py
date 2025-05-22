from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def test_javascript_alert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    logging.info("Открыта страница с алертами")

    driver.find_element(By.CSS_SELECTOR, "button[onclick = 'jsAlert()']").click()
    alert = driver.switch_to.alert
    logging.info("Переключаемся на алерт")
    alert.accept()
    logging.info("Алерт принят")

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    logging.info("Ждем появления результата")
    assert "You successfully clicked an alert" in result.text.strip()
    logging.info("Сранвиваем текст с результатом")
    driver.save_screenshot("successfully_result.png")
    logging.info("Делаем скриншот результата")
    driver.quit()
