from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_and_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    radio2 = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd2']")
    assert radio2.is_selected()

    radio3 = driver.find_element(By.CSS_SELECTOR,"input[name='radioval'][value='rd3']" )
    if not radio3.is_selected():
        radio3.click()
    assert radio3.is_selected()

    driver.quit()