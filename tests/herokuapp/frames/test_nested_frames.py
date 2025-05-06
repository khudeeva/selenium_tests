from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_nested_frames():
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    driver.switch_to.frame("frame-top")
    driver.switch_to.frame("frame-middle")
    text_middle = driver.find_element(By.ID, "content")
    assert text_middle.text.strip() == "MIDDLE"

    driver.switch_to.default_content()

    driver.switch_to.frame("frame-bottom")
    text_bottom = driver.find_element(By.TAG_NAME, "body")
    assert text_bottom.text.strip() == "BOTTOM"
    
    driver.switch_to.default_content()
    driver.quit()