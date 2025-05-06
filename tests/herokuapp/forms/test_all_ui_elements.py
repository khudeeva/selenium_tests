from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_all_ui_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("1")
    
    selected =  dropdown.first_selected_option
    assert selected.text.strip() == "Option 1"
    assert selected.get_attribute("value") == "1"

# radio
    driver.get("https://demoqa.com/radio-button")
    button = driver.find_element(By.XPATH, "//label[text()='Yes']")
    button.click()

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-success"))
    )
    assert result.text.strip() == "Yes"

# checkbox
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox2 =driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[1]
    if not checkbox2.is_selected():
        checkbox2.click()

# alert
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
    alert = driver.switch_to.alert
    alert.send_keys("Ksenia")
    alert.accept()

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )
    assert result.text.strip() == "You entered: Ksenia"
    driver.quit()




