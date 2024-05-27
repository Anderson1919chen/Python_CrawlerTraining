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

search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys("比特幣")
search.send_keys(Keys.RETURN)
time.sleep(2)

titles = driver.find_elements(By.XPATH, "//h3")
for title in titles:
    print(title.text)# 取得標籤內部的文字

driver.get("https://www.dcard.tw/f")
search = driver.find_element(By.NAME, "query")
time.sleep(2)
search.send_keys("比特幣")
time.sleep(2)
search.send_keys(Keys.RETURN) #會被Dcard擋


time.sleep(5)
driver.quit()
