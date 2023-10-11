from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    value_x = x.text
    y = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    value_y = y.text

    sum_of_values = int(value_x) + int(value_y)
    
    result = str(sum_of_values)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)
   
      
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
    
    time.sleep(10)

       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

