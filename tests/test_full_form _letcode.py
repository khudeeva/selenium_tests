from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_full_form_letcode():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://letcode.in/forms")

    driver.find_element(By.ID, "firstname").send_keys("Ksenia")
    driver.find_element(By.ID, "lasttname").send_keys("Khudeeva")

    email = driver.find_element(By.ID, "email")
    email.send_keys(Keys.CONTROL + "a")
    email.send_keys(Keys.DELETE)
    email.send_keys("khudeeva2000@mail.com")
    assert "khudeeva2000@mail.com" in email.get_attribute("value")

    dropdowns = driver.find_elements(By.TAG_NAME, "select")
    country_code = Select(dropdowns[0])
    country_dropdown = Select(dropdowns[1])

    country_code.select_by_value("7")
    selected_country_code = country_code.first_selected_option
    assert selected_country_code.get_attribute("value") == "7"

    phone_number = driver.find_element(By.ID, "Phno")
    phone_number.send_keys("9504540000")
    assert "9504540000" in phone_number.get_attribute("value")

    address1 = driver.find_element(By.ID, "Addl1")
    address1.send_keys("Perm")
    assert "Perm" in address1.get_attribute("value")

    address2 = driver.find_element(By.ID, "Addl2")
    address2.send_keys("Moscow")
    assert "Moscow" in address2.get_attribute("value")

    state = driver.find_element(By.CSS_SELECTOR, "input[id='state']")
    state.send_keys("None")
    assert "None" in state.get_attribute("value")

    postal_code = driver.find_element(By.CSS_SELECTOR, "input[id='postalcode']")
    postal_code.send_keys("619350")
    assert "619350" in postal_code.get_attribute("value")


    country_dropdown.select_by_value("Russian Federation")
    selected = country_dropdown.first_selected_option
    assert selected.text.strip() == "Russian Federation"

    data_birth = driver.find_element(By.CSS_SELECTOR, "input[id='Date']")
    driver.execute_script("arguments[0].value = arguments[1]", data_birth, "2000-01-24")
    assert  data_birth.get_attribute("value") == "2000-01-24"

    radio = driver.find_element(By.CSS_SELECTOR, "input[id='female']")  
    radio.click()
    assert radio.is_selected()

    checkbox = driver.find_element(By.CSS_SELECTOR, "input[type = 'checkbox']")
    if not checkbox.is_selected():
        checkbox.click()
    assert checkbox.is_selected()


    driver.quit()