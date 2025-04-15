from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_select_radio_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(" https://testpages.herokuapp.com/styled/basic-html-form-test.html")

# выбираем радиокнопку с value='rd2'
    radio_button = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd2']")
    radio_button.click()

# проверяем, что выбрана радиокнопка2
    assert radio_button.is_selected()

    driver.quit()