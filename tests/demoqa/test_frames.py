from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_frames():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/frames")

    # frame 1
    frame1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(frame1)
    text_frame1 = driver.find_element(By.TAG_NAME, "h1")
    text1 =  text_frame1.text.strip()
    
    # выход из фрейма
    driver.switch_to.default_content()

    #frame 2
    frame2 = driver.find_element(By.ID, "frame2")
    driver.switch_to.frame(frame2)
    text_frame2 = driver.find_element(By.TAG_NAME, "h1")
    text2 =  text_frame2.text.strip()

    assert text1 == text2
    driver.quit()