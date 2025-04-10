from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def test_select_dropdown_option():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    # выбираем "Drop Down Item 5" из списка
    dropdown = Select(driver.find_element(By.NAME, "dropdown"))
    dropdown.select_by_value("dd5")

    # ждем загрузки кнопки 'submit'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )
    # нажимаем на кнопку 'submit'
    submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']")
    submit_btn.click()

    # ждем редирект
    WebDriverWait(driver, 10).until(
        EC.url_contains("the_form_processor")
    )
    # проверяем, что находимя на странице (..the_form_processor)
    assert "the_form_processor" in driver.current_url

    # проверяем, что есть текст (dropdown: dd5)
    submit_value = driver.find_element(By.ID, "_valuedropdown")
    assert submit_value.text.strip() == "dd5"

    driver.quit()


