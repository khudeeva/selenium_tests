from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checked_windows():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/iframe")

    frame = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(frame)

    editor = driver.find_element(By.ID, "tinymce")
    editor.send_keys(Keys.CONTROL + "a")
    editor.send_keys(Keys.DELETE)
    editor.send_keys("QA")

    driver.switch_to.default_content()
    heading = driver.find_element(By.TAG_NAME, "h3")
    assert heading.text.strip() == "An iFrame containing the TinyMCE WYSIWYG Editor"

    driver.quit()