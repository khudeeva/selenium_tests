from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def test_nested_frame_bottom_text():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    #переключаемся во фрейм, который не вложен, на том же уровне, что и frame-top
    driver.switch_to.frame("frame-bottom")
    # проверяем, что его текст 'BOTTOM'
    bottom_frame = driver.find_element(By.TAG_NAME, "body")
    assert bottom_frame.text.strip() == "BOTTOM"
    # возвращаемся на основную страницу
    driver.switch_to.default_content()
    driver.quit()    
