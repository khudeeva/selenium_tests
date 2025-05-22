from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
def test_login_with_screenshot():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    logging.info("Открыта страница логина")

    driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("tomtomtom")
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("anotherpassword")
    logging.info("Введены неверные данные")
    driver.save_screenshot("login_inputs.png")
    logging.info("Поле логина найдено и заполнено")
    driver.quit()
