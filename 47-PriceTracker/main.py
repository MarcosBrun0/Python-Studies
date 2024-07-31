import requests
from bs4 import BeautifulSoup
import  smtplib


#change this link for the product in amazon you want to track
product_url = "https://www.amazon.com.br/Novo-Kindle-lan%C3%A7amento-2022-armazenamento/dp/B09SWV1FSS/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1IKMEC04AA2GY&dib=eyJ2IjoiMSJ9.UdJtm3bxot7oa-1z7NSMtBzYgHRAAaEWi5_tH6TtESiaL7LDWqXXcuFur9W7R0YYwR6YV3hX4Uz2KfkYTUM6PPHGXJJCpmISAJUdPWjWvE4vxpGhwbfp93ySnbyZmE5KVv1b-Nyp2KpZjQQIwxRpyi1aAYXzN7vF7_R5iCjpWzrZzwWcUfS_qRyfi_r_VuECnwrb5caK6wMUXOl08kZ_ohBf5Y7x-J6plIO6kliDFN5XHAphccA18t50XLMoCv7o6vSXtrqsMaOSgEXat4hibVEjGq5xWoWFgt0ZoaedmE4.r3tnDmVvCecXxDlc4KY8listnpf5iWCH5gVrqCR3DQk&dib_tag=se&keywords=kindle&qid=1711224482&s=electronics&sprefix=kindl%2Celectronics%2C274&sr=1-1&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
}

response = requests.get(url=product_url,headers=header)
site_text = response.text


def sendmail():
    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        #change the xxxxxxx
        conection.login(user='xxxxxxxxxx' ,password='xxxxxxxxx')
        conection.sendmail(from_addr='xxxxxxxxxx',to_addrs="xxxxxxxxxx", msg=f"Subject:the product goal price has been reached {product_url}")




soup = BeautifulSoup(site_text,"html.parser")
price =soup.find(name="span", class_="a-price-whole")
tprice =str(price.getText())
intprice = int(tprice[:-1])
print(intprice)
#set your goal price for your product
goal_price = 350
if intprice < goal_price:
   sendmail()