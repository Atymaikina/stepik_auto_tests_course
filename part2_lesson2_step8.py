from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os


try:
    link = " https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys('Test')
  
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Test')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('Test')

    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")

    file_button.send_keys(file_path)
      
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
    time.sleep(10)

       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

