import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from HomePageTests.sign_up import SignUpTests

driver = webdriver.Chrome()
driver.get ("https://demo.nopcommerce.com")
time.sleep(3)

sign_up = SignUpTests(driver)

sign_up.reg_start()

sign_up.last_name()