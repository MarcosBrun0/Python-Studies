from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

#find element in page
a_counter = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(a_counter.text)



driver.quit()