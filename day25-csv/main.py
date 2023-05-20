import pandas

data = pandas.read_csv("weather_data.csv")
soma = 0

temp_Lista = data["temp"].tolist()
print(temp_Lista)
quant = len(temp_Lista)
print(quant)
for temp in temp_Lista:
    soma += temp

print(soma)
media = soma/quant


print(media)
