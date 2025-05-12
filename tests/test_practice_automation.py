from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_practice_automation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("student")
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("logged-in-successfully")
    )
    assert "logged-in-successfully" in driver.current_url
    driver.quit()
