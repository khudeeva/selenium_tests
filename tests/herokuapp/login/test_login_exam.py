from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_exam():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("secure")
    )
    assert "secure" in driver.current_url

    flash = driver.find_element(By.ID, "flash").text.strip()
    assert "You logged into a secure area!" in flash

    driver.quit()

