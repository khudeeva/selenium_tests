from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test_new_tab():
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/browser-windows")
    original_tab = driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR, "button[id='tabButton']").click()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles)>1)

    for handle in driver.window_handles:
        if handle!= original_tab:
            driver.switch_to.window(handle)
            break
    heading = driver.find_element(By.CLASS_NAME, "main-header")
    assert heading.text.strip() == "This is a sample page"

    driver.switch_to.window(original_tab)
    text_center = driver.find_element(By.TAG_NAME, "h1")
    assert text_center.text.strip() == "Browser Windows"
    assert "browser-windows" in driver.current_url
    driver.quit()




