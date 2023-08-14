import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()

driver.get ("https://demo.nopcommerce.com/")
time.sleep (5)

x = driver.find_element(By.XPATH, "/html//select[@id='customerCurrency']")
hover = ActionChains(driver).move_to_element(x)
select = Select(x)
select.select_by_value("https://demo.nopcommerce.com/changecurrency/6?returnUrl=%2F")
time.sleep (5)