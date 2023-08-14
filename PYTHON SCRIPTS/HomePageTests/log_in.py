import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get ("https://demo.nopcommerce.com")
time.sleep(3)

log_in = driver.find_element (By.XPATH, "/html/body/div[@class='master-wrapper-page']//div[@class='header-links']/ul//a[@href='/login?returnUrl=%2F']")
log_in.click()
time.sleep(3)

email = driver.find_element (By.XPATH, "/html//input[@id='Email']")
email.send_keys ("Odeh.rash@gmail.com")
time.sleep (0.7)

password = driver.find_element (By.XPATH, "/html//input[@id='Password']")
password.send_keys ("rashed123")
time.sleep (0.7)

log_button = driver.find_element (By.XPATH, "/html/body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-column-wrapper']//form[@action='/login?returnurl=%2F']//button[@type='submit']")
log_button.click()
time.sleep(7)