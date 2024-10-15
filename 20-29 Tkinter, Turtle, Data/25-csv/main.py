import pandas

# data = pandas.read_csv("weather_data.csv")
# soma = 0
#
# temp_Lista = data["temp"].tolist()
# print(temp_Lista)
#
# maxtemp = (data["temp"].max())
#
#
# print(data[data.temp == maxtemp])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

graysquarrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamonsquarrel=len(data[data["Primary Fur Color"] == "Cinnamon"])
blacksquarrel=len(data[data["Primary Fur Color"] == "Black"])

data_dict = {

    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [ graysquarrel, cinnamonsquarrel, blacksquarrel ]

}

print(data_dict)

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_cout.csv")
