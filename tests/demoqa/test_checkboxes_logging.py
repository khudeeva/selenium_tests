from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s'
)
def test_checkboxes_logging():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    logging.info("Открыта страница Checkboxes")

    checkbox2 = driver.find_elements(By.CSS_SELECTOR,"input[type=checkbox]")[1]
    if not checkbox2.is_selected():
        logging.info("Кликаем на checkbox2")
        checkbox2.click()
    

    assert checkbox2.is_selected()
    logging.info("Проверка, что checkbox2 выбран")

    driver.quit()

