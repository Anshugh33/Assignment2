#incorrect password 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.saucedemo.com/") 
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("problem_user")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.XPATH,"//input[@id='error-messege-container']")
time.sleep(7)

