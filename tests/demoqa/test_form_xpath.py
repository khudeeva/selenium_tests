from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_form_xpath():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Ksenia")
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("kskhud@mail.com")
    driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Perm")
    driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Moscow")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']" ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='output']"))
    )

    name_text = driver.find_element(By.XPATH, "//p[@id='name']").text.strip()
    email_text = driver.find_element(By.XPATH, "//p[@id='email']").text.strip()
    current_address_text = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text.strip()
    permanent_address_text = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text.strip()

    print(name_text)
    print(email_text)
    print(current_address_text)
    print(permanent_address_text)

    driver.quit()

