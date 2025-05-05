from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_button_impressive():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/radio-button")

    driver.find_element(By.XPATH, "//label[text()='Impressive']").click()

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-success"))
    )
    assert result.text.strip() == "Impressive"

    driver.quit()
