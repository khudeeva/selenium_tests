from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def test_nested_frames_middle_text():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/nested_frames")

# переключаемся во внешний фрейм
    driver.switch_to.frame("frame-top")
# переключаемся во вложенный фрейм
    driver.switch_to.frame("frame-middle")
# проверяем, что его текст 'MIDDLE'
    middle_frame = driver.find_element(By.ID, "content")
    assert middle_frame.text.strip() == "MIDDLE"
#возвращаемся к основной странице
    driver.switch_to.default_content()

    driver.quit()


