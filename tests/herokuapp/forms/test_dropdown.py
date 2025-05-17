from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_dropdown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")
    
    selected = dropdown.first_selected_option
    assert selected.text.strip() == "Option 2"
    assert selected.get_attribute("value") == "2"

    driver.quit()