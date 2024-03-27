from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, Config
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

url ="https://www.linkedin.com/jobs/search/?currentJobId=3839568256&distance=25&f_AL=true&f_E=1%2C2&f_WT=2&geoId=106057199&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"


driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)
time.sleep(1)
signInButton = driver.find_element(By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
time.sleep(1)
signInButton.click()
emailEntry = driver.find_element(By.XPATH,value='//*[@id="username"]')
emailEntry.send_keys(Config.email)
PassEntry = driver.find_element(By.XPATH,value='//*[@id="password"]')
PassEntry.send_keys(Config.password_linkedin)
signInButton = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signInButton.click()




