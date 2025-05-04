from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

def test_practice_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/automation-practice-form")

    # ищем поле для ввода first Name
    driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='firstName']").send_keys("Ksenia")

    # ищем поле для ввода Last Name
    driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='lastName']").send_keys("Khudeeva")

    # ищем поле для ввода Email
    driver.find_element(By.ID, "userEmail").send_keys("kskhud@mail.com")

    # выбираем gender
    driver.find_element(By.XPATH, "//label[text()='Female']").click()

    # вводим в поле ввода mobile Number
    mobile = driver.find_element(By.ID, "userNumber")
    mobile.clear()
    mobile.send_keys("+79802345677")
    
    # кликнем на кнопку Submit
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()


    driver.quit()