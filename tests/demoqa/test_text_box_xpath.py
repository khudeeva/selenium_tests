from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
def test_text_box_xpath():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/text-box")

    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Ksenia")
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("kskhud@mail.com")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@id='output']"))
    )

    name_text = driver.find_element(By.XPATH, "//p[@id='name']").text.strip()
    email_text = driver.find_element(By.XPATH, "//p[@id='email']").text.strip()

    assert "Ksenia" in name_text
    assert "kskhud@mail.com" in email_text

    driver.quit()