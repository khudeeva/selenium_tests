from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_dropdown_select():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")

    selected = dropdown.first_selected_option
    assert selected.text.strip() == "Option 2"

    driver.quit()