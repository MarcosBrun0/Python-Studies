import Config
import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

def getstockdata():

    function="TIME_SERIES_DAILY"
    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    response = requests.get(f"{STOCK_ENDPOINT}?function={function}&symbol={STOCK_NAME}&apikey={Config.AlphaAdvantage_APIKEY}")
    response.raise_for_status()
    data = response.json()
    return data



def getNews():
    url ="https://newsapi.org/v2/everything"
    q ="tesla"
    Sortby ="PublishedAt"
    language="pt"
    pageSize = "3"
    api =config.newsAPI
    response = requests.get(f"{url}?q={q}&apiKey={api}&sortBy={Sortby}&language={language}&pageSize={pageSize}")
    response.raise_for_status()
    data =response.json()
    data = data["articles"]
    print(data)
    return data










#date config
today = datetime.date.today()
day = str(today)[8:]
#yersterday
temp = int(day)-1
yerterday = f"{str(today)[0:9]}"+f"{str(temp)}"
#the day before
temp= temp-1
daybefore = f"{str(today)[0:9]}"+f"{str(temp)}"

#getting dated data
data = getstockdata()
yerterOpenValue =(data["Time Series (Daily)"][yerterday]["1. open"])
daybeforeOpenValue =(data["Time Series (Daily)"][daybefore]["1. open"])

#regra de 3 para achar percentual
percent = (100*float(yerterOpenValue))/float(daybeforeOpenValue)
print("%",percent)

porcentagedifference = percent-100
if porcentagedifference > 5 or porcentagedifference<-5:
    news = getNews()
print(news)


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

