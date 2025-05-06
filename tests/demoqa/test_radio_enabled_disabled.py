from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_enabled_disabled():
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/radio-button")

    yes_radio = driver.find_element(By.CSS_SELECTOR, "input[id='yesRadio']")
    assert yes_radio.is_enabled()

    
    no_radio = driver.find_element(By.CSS_SELECTOR, "input[id='noRadio']")
    assert not no_radio.is_enabled()
    driver.quit()
