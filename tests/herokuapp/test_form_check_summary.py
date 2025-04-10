from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_form_check_summary():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

# вводим username и password
    driver.find_element(By.NAME, "username").send_keys("form_checker")
    driver.find_element(By.NAME, "password").send_keys("qwerty")

# очищаем textarea, вводим 'проверка вывода'
    textarea = driver.find_element(By.NAME, "comments")
    textarea.clear()
    textarea.send_keys("проверка вывода")

# выбираем Radio 3
    radio = driver.find_element(By.CSS_SELECTOR, "input[name='radioval'][value='rd3']") 
    radio.click()

# выбираем Drop Down Item 2
    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd2")

# нажимаем на кнопку 'submit'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']").click()

# ждем редиректа
    WebDriverWait(driver, 10).until(
        EC.url_contains("the_form_processor")
    )
    assert "the_form_processor" in driver.current_url

# проверка результатов
    assert driver.find_element(By.ID, "_valueusername").text.strip() == "form_checker"
    assert driver.find_element(By.ID, "_valuepassword").text.strip() == "qwerty"
    assert driver.find_element(By.ID, "_valuecomments").text.strip() == "проверка вывода"
    assert driver.find_element(By.ID, "_valueradioval").text.strip() == "rd3"
    assert driver.find_element(By.ID, "_valuedropdown").text.strip() == "dd2"

    driver.quit()