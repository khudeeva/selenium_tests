from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_and_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    # выбрать радиокнопку с value='rd3'
    radio_button = driver.find_element(By.CSS_SELECTOR,"input[name='radioval'][value='rd3']")
    radio_button.click()

    # ждем загрузки кнопки 'submit'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']"))
    )

    # нажать на кнопку 'submit'
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submitbutton']").click()

    # ждем редирект
    WebDriverWait(driver, 10).until(
        EC.url_contains("the_form_processor")
    )

    #проверка, что находимся на нужной странице(..formprocessor.html)
    assert "the_form_processor" in driver.current_url

    # проверяем, что есть текст(radioval: rd3)
    submit_value = driver.find_element(By.ID,"_valueradioval")
    assert "rd3" in submit_value.text.strip()

    driver.quit()

    