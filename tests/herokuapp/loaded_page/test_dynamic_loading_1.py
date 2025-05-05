from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_dynamic_loading():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    #Нажать на кнопку Start
    button =  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    button.click()
    # ждем появления текста
    text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!")
    )
    # проверяем текст
    text = driver.find_element(By.ID, "finish")
    assert  "Hello World!" in text.text.strip()


    driver.quit()
    
