from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def test_nested_frame_left_text():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/nested_frames")

# переключаемся во фрейм
    driver.switch_to.frame("frame-top")
# переключаемся во вложенный фрейм 'frame-left'
    driver.switch_to.frame("frame-left")
# проверяем, что его текст 'LEFT' (из Body)
    left_frame = driver.find_element(By.TAG_NAME, "body")
    assert left_frame.text.strip() == "LEFT"
# возвращаемся на основную страницу
    driver.switch_to.default_content()

    driver.quit()