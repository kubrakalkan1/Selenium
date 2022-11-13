from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

element_id= driver.find_elements('id', 'gsc-iw-id1')
print(element_id)

element_name = driver.find_elements('name', 'submit')
print(element_name)

element_xpath = driver.find_elements(By.XPATH, "//section[@class='row td-cover-block td-cover-block']/h[1]")
print(element_xpath)

element_cname = driver.find_elements(By.CLASS_NAME, "selenium-backers")
print(element_cname)

driver.close()
