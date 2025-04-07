from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# вход с корректным паролем и проверка welcome-сообщения
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# вводим имя пользователя
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# вводим корректный пароль
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# нажимаем на кнопку логина
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# читаем сообщение об успешном входе
success_message = driver.find_element(By.ID, "flash")
print("Результат:", success_message.text.strip())

time.sleep(4)
driver.quit()

# вход с неверным паролем и проверка ошибки
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# вводим имя пользователя
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# вводим пароль
password = driver.find_element(By.ID, "password")
password.send_keys("wrongPassword")

# нажимает на кнопку логина
login_button = driver.find_element(By.CSS_SELECTOR, "button[type ='submit']")
login_button.click()

# читаем сообщение об ошибке:
error_message = driver.find_element(By.ID, "flash")
print("Результат:", error_message.text.strip())

time.sleep(3)
driver.quit()