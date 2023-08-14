import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class SignUpTests(object):
    def __init__(self, driver:webdriver.Chrome) -> None:
        self.driver:webdriver.Chrome = driver

    def reg_start(self):
        register = self.driver.find_element(By.XPATH, "/html/body/div[@class='master-wrapper-page']//div[@class='header-links']/ul//a[@href='/register?returnUrl=%2F']")
        register.click()
        time.sleep(3)

    def gender(self):
        gender = self.driver.find_element(By.XPATH, "/html//input[@id='gender-male']")
        gender.click()
        time.sleep(0.7)

    def first_name(self):
        first_name = self.driver.find_element(By.XPATH, "/html//input[@id='FirstName']")
        first_name.send_keys("Rashed")
        time.sleep(0.7)

    def last_name(self):
        last_name = self.driver.find_element(By.XPATH, "/html//input[@id='LastName']")
        last_name.send_keys("Odeh")
        time.sleep(0.7)

    def day_date(self):
        day_date = self.driver.find_element(By.XPATH, "/html/body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-column-wrapper']//form[@action='/register?returnurl=%2F']//select[@name='DateOfBirthDay']")
        hover = ActionChains(self).move_to_element(day_date)
        select = Select(day_date)
        select.select_by_value("7")
        time.sleep(0.7)
    def month_date(self):
        month_date = self.driver.find_element(By.XPATH, "/html/body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-column-wrapper']//form[@action='/register?returnurl=%2F']//select[@name='DateOfBirthMonth']")
        hover = ActionChains(self).move_to_element(month_date)
        select = Select(month_date)
        select.select_by_value("9")
        time.sleep(0.7)
    def year_date(self):
        year_date = self.driver.find_element(By.XPATH, "/html/body/div[@class='master-wrapper-page']/div[@class='master-wrapper-content']/div[@class='master-column-wrapper']//form[@action='/register?returnurl=%2F']//select[@name='DateOfBirthYear']")
        hover = ActionChains(self).move_to_element(year_date)
        select = Select(year_date)
        select.select_by_value("1997")
        time.sleep(0.7)

    def email(self):
        email = self.driver.find_element(By.XPATH, "/html//input[@id='Email']")
        email.send_keys("Odeh.rash@gmail.com")
        time.sleep(0.7)

    def newsteller(self):
        sub = self.driver.find_element(By.XPATH, "/html//input[@id='Newsletter']")
        sub.click()
        time.sleep(0.7)

    def newpass(self):
        password = self.driver.find_element(By.XPATH, "/html//input[@id='Password']")
        password.send_keys("rashed123")
        time.sleep(0.7)
        pass_rep = self.driver.find_element(By.XPATH, "/html//input[@id='ConfirmPassword']")
        pass_rep.send_keys("rashed123")
        time.sleep(0.7)

    def reg_conf(self):
        reg_button = self.driver.find_element(By.XPATH, "/html//button[@id='register-button']")
        reg_button.click()
        time.sleep(7)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com")
    time.sleep(3)