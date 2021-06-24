from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from passwords import USERNAME, PASSWORD
import time

username = USERNAME
password = PASSWORD


driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get("https://dvoru.com/user")

driver.find_element_by_id("login").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

time.sleep(2)

driver.find_element_by_id("btn-login").click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a/span').click()
