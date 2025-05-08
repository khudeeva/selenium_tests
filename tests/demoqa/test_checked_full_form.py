from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checked_full_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # checkbox
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox2 = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[1]
    if not checkbox2.is_selected():
        checkbox2.click()
    assert checkbox2.is_selected()

    # radio
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[text()='Impressive']").click()
    impressive_radio = driver.find_element(By.CSS_SELECTOR, "input[id='impressiveRadio']")
    assert impressive_radio.is_enabled()
    text_success = driver.find_element(By.CLASS_NAME, "text-success")
    assert text_success.text.strip()=="Impressive"

    # dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")
    selected = dropdown.first_selected_option
    assert selected.text.strip() == "Option 2"
    driver.quit()

