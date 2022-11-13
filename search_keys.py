from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get("http://python.org");

element_name = driver.find_element(By.NAME, 'submit')
search.clear();
search.send_keys("pycon");
search.send_keys(Keys.RETURN);
time.sleep(4)

driver.close();
