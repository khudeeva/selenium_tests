from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_checkboxes_click():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")[0]

    if not checkbox1.is_selected():
        checkbox1.click()

    driver.quit()


