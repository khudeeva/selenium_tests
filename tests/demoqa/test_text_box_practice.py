from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_text_box_practice():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.CSS_SELECTOR, "input[id='userName']").send_keys("Ksenia")
    driver.find_element(By.ID, "userEmail").send_keys("kskhud@mail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("Perm")
    driver.find_element(By.ID, "permanentAddress").send_keys("Moscow")
    
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "output"))
    )
    name_text = driver.find_element(By.ID, "name").text.strip()
    email_text = driver.find_element(By.ID, "email").text.strip()
    current_address = driver.find_element(By.XPATH, "//div[@id='output']//p[@id='currentAddress']").text.strip()
    permanent_address = driver.find_element(By.XPATH, "//div[@id='output']//p[@id='permanentAddress']").text.strip()
    

    assert "Ksenia" in name_text
    assert "kskhud@mail.com" in email_text
    assert "Perm" in current_address
    assert "Moscow" in permanent_address

    driver.quit()