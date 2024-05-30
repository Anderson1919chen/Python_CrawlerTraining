# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os
import wget

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
s = Service(executable_path=r"C:/Users/User/Desktop/edgedriver1/msedgedriver.exe")
driver = webdriver.Edge(options=option,service=s)

# 登入ig
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
time.sleep(5)

# 在google上搜尋cat並儲存圖片
driver.get("https://google.com")
search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.clear()
keyword = "cat"
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

pictrue = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div'))
)
pictrue.click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "YQ4gaf"))
)
img = driver.find_element(By.CLASS_NAME, "YQ4gaf")

actions = ActionChains(driver)
actions.click(img)
#actions.context_click(on_element=None)
# 創建資料夾儲存下載的圖片
#path = "C:/Users/User/Desktop/selenium_tutorial"
#path = os.path.join(keyword)
#os.mkdir(path)

#count = 0
#for img in imgs:
    #save_as = os.path.join(path, keyword + str(count) + ".jpg")
    #print(img.get_attribute("src"))
    #wget.download(img.get_attribute("src"), save_as)
    #count  += 1

time.sleep(5)
driver.quit()


