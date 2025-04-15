from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_full_form_review():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

# вводим username и password
    driver.find_element(By.NAME, "username").send_keys("selenium_user")
    driver.find_element(By.NAME, "password").send_keys("superpass")

# очищаем и заполняем textarea
    textarea = driver.find_element(By.NAME, "comments")
    textarea.clear()
    textarea.send_keys("форма для закрепления")

# выбираем чекбокс 1 и 3
    checkbox1 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='cb1']")
    checkbox3 = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][value='cb3']")
    if not checkbox1.is_selected():
        checkbox1.click()
    if not checkbox3.is_selected():
        checkbox3.click()

# выбираем радио 2
    radio = driver.find_element(By. CSS_SELECTOR, "input[name='radioval'][value='rd2']")
    radio.click()

# выбрать Drop Down Item 3
    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd3")

# нажать на кнопку 'submit'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']").click()

# ждем редиректа
    WebDriverWait(driver, 10).until(
        EC.url_contains("the_form_processor")
    )
    assert "the_form_processor" in driver.current_url

# проверка результата
    assert driver.find_element(By.ID, "_valueusername").text.strip() == "selenium_user"
    assert driver.find_element(By.ID, "_valuepassword").text.strip() == "superpass"
    assert driver.find_element(By.ID, "_valuecomments").text.strip() == "форма для закрепления"
    assert driver.find_element(By.ID, "_valuecheckboxes0").text.strip() == "cb1"
    assert driver.find_element(By.ID, "_valuecheckboxes1").text.strip() == "cb3"
    assert driver.find_element(By.ID, "_valueradioval").text.strip() == "rd2"
    assert driver.find_element(By.ID, "_valuedropdown").text.strip() == "dd3"

    driver.quit()