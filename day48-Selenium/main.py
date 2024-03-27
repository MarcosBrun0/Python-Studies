from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
# #class="a-price-whole" the price class in amazon site
#
# price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print("The price is:", price.text)
# driver.quit()
#

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar)
# button = driver.find_element(By.ID, value="submit")
# documentation_link = driver.find_element(By.CSS_SELECTOR, value="documentation-widget a")
#Xpath is a easy way to find css elements
#//*[@id="site-map"]/div[2]/div/ul/li[3]/a

# Githib_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(Githib_link.get_attribute("href"))
#
#
event_times = driver''.find_elements(By.CSS_SELECTOR,value=".event-widget time")
for time in event_times:
    print(time.text)
driver.quit()