from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_window_switching():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

    original_tab = driver.current_window_handle

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) >1)
    
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
    
    new_text = driver.find_element(By.TAG_NAME, "h3")
    assert new_text.text.strip() == "New Window"
    
    driver.switch_to.window(original_tab)
    original_text = driver.find_element(By.TAG_NAME, "h3")
    assert original_text.text.strip() == "Opening a new window"

    driver.quit()