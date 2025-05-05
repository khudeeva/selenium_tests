from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_checkboxes_summary():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    if not checkbox1.is_selected():
        checkbox1.click()
    assert checkbox1.is_selected()

    assert checkbox2.is_selected()

    driver.quit()

 