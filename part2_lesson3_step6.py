from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()

    new_window_name = browser.window_handles[1]
    new_window = browser.switch_to.window(new_window_name)

    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    value = x.text 
    result = calc(value)

    input_answer = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input_answer.send_keys(result)

     
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
   
    
    time.sleep(10)

       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

