# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time
import requests

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
s = Service(executable_path=r"C:/Users/User/Desktop/edgedriver1/msedgedriver.exe")
driver = webdriver.Edge(options=option,service=s)

driver.get("https://www.instagram.com/?hl=zh-tw")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
username.send_keys("anderson1233211234567@gmail.com")
password.send_keys("andersonsmalljay1234")
login.click()




