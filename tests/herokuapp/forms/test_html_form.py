from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

def test_html_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    checkbox1 = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]
    if not checkbox1.is_selected():
        checkbox1.click()
    assert checkbox1.is_selected()

    radio2 = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd2']")
    radio2.click()
    assert radio2.is_selected()

    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd3")
    selected = dropdown.first_selected_option
    assert selected.text == "Drop Down Item 3"
   

    driver.quit()

