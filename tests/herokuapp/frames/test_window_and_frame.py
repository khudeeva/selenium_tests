from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checked_nested_frames():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/windows")

    original_tab = driver.current_window_handle

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    for handle in driver.window_handles:
        if handle != original_tab:
            driver.switch_to.window(handle)
            break
    driver.get("https://the-internet.herokuapp.com/iframe")

    frame = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(frame)

    editor = driver.find_element(By.ID, "tinymce")
    editor.send_keys(Keys.CONTROL + "a")
    editor.send_keys(Keys.DELETE)
    editor.send_keys("Ksenia is here!")

    driver.switch_to.default_content()
    driver.quit()