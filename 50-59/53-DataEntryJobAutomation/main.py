from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, Config
from DataCollect import link_list,address_list,price_list


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/s8JqSsg6XU4VkWLn7")


adressXpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
priceXpath ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
linkXpath ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'


for n in range(len(price_list)):
    time.sleep(0.4)
    address = driver.find_element(By.XPATH,value=adressXpath)
    price = driver.find_element(By.XPATH,value=priceXpath)
    link = driver.find_element(By.XPATH,value=linkXpath)
    sendbutton = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(address_list[n])
    price.send_keys(price_list[n])
    link.send_keys(link_list[n])
    time.sleep(0.5)
    sendbutton.click()
    time.sleep(0.4)
    newentry = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    newentry.click()
    time.sleep(0.4)

driver.quit()

