from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    value_x = x.text   
    result = calc(value_x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(result)

    browser.execute_script("window.scrollBy(0, 150);")
   
    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio.click()
   
      
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    
    time.sleep(10)

       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

