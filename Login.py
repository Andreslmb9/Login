from asyncio import Event
import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

delay = 3

driver=webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/") 
driver.maximize_window ()
time.sleep(1)
MK = driver.find_element(By.XPATH, "//*[@id='btn-make-appointment']")
MK.click ()
time.sleep(3)
usr= driver.find_element(By.XPATH, "//*[@id='txt-username']").send_keys ('John Doe')
#time.sleep(3)
usr= driver.find_element(By.XPATH, "//*[@id='txt-password']").send_keys ('ThisIsNotAPassword')
time.sleep(3)
btnlogin = driver.find_element(By.XPATH, "//*[@id='btn-login']")
btnlogin.click ()
time.sleep(3)

driver.close()


