from selenium import webdriver 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests



option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

s = Service(executable_path=r"C:/Users/User/Desktop/selenium_tutorial/msedgedriver.exe")

driver = webdriver.Edge(options=option,service=s)

driver.get("HTTPS://google.com")

#titles = driver.find_elements_by_class_name("board-nuser") 沒有這個方法

search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)

#search = driver.find_element(By.NAME, "query")
#search.send_keys("比特幣")
#search.send_keys(Keys.RETURN) #會被Dcard擋


#time.sleep(5)
#driver.quit()
