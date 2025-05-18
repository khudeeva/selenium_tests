from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checked_windows():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

    original_tab = driver.current_window_handle

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    for handle in driver.window_handles:
        if handle !=original_tab:
            driver.switch_to.window(handle)
            break
    text_example = driver.find_element(By.TAG_NAME, "h3")
    assert text_example.text.strip() == "New Window"

    driver.switch_to.window(original_tab)
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text.strip() == "Opening a new window"

    driver.quit()



