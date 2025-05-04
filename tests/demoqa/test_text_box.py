from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# настраиваем логирование 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_text_box():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demoqa.com/text-box")
        logging.info("Открыта страница формы")

        driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("Ksenia")
        logging.info("Введено имя")

        driver.find_element(By.ID, "userEmail").send_keys("kskhud@mail.com")
        logging.info("Введен Email")

        driver.find_element(By.ID, "currentAddress").clear().send_keys("Perm")
        logging.info("Введен текущий адрес")

        
        driver.find_element(By.ID, "permanentAddress").clear().send_keys("Moscow")
        logging.info("Введен дополнительный адрес")

    
        driver.find_element(By.ID, "submit").click()
        logging.info("Форма отправлена")

        # ждем появления блока с результатом
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "output"))
        )

        # проверка текста результата
        name_text = driver.find_element(By.ID, "name").text.strip()
        email_text = driver.find_element(By.ID, "email").text.strip()
        current_address_text = driver.find_element(By.ID, "currentAddress").text.strip()
        permanent_address_text = driver.find_element(By.ID, "permanentAddress").text.strip()

        assert "Ksenia" in name_text
        assert "kskhud@mail.com" in email_text
        assert "Perm" in current_address_text
        assert "Moscow" in permanent_address_text
        logging.info("Проверка прошла успешно!")

    except Exception as e:
        logging.error(f"Ошибка при выполнении теста: {e}")
    finally:
        driver.quit()


