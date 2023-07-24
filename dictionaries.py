dict1 = {
    "Tom": 84.4,
    "Jerry": 168.0
}

for key in dict1:
    print("person={0} weight={1}".format(key, dict1[key]))

print("-------------- End ---------------")

dict2 = {
    "honda": 23800,
    "tesla": 46990
}

for key in dict2:
    print("car={0} price={1}".format(key, dict2[key]))

dict3 = {
    "apple": 15,
    "mango": 20
}

for key in dict3:
    print("fruit={0} price={1}".format(key, dict3[key]))

print("------ Find friut with max price -------")
maxFruit = ''
maxPrice = 0
for key in dict3:
    price = int(dict3[key])
    if maxPrice < price:
        maxPrice = price
        maxFruit = key

print("maxFruit={0} maxPrice={1}".format(maxFruit, str(maxPrice)))

print("-------- Find total price for all fruits -------")
totalPrice = 0
for key in dict3:
    price = int(dict3[key])
    totalPrice = totalPrice + price

print(totalPrice)

print("------- Find car with max price --------")
maxCar = ''
maxPrice = 0
for key in dict2:
    price = int(dict2[key])
    if maxPrice < price:
        maxPrice = price
        maxCar = key

print("maxCar={0} maxPrice={1}".format(maxCar, str(maxPrice)))

print("-------- Find total price for all car ---------")
totalPrice = 0
for key in dict2:
    price = int(dict2[key])
    totalPrice = totalPrice + price

print(totalPrice)

print("-------- END ---------")

dict4 = {
    "potato": 8,
    "tomato": 15
}

for key in dict4:
    print("vegetable={0} price={1}".format(key,dict4[key]))

print("--------- Find vegetable with max price --------")
maxVegetable = ''
maxPrice = 0
for key in dict4:
    price = int(dict4[key])
    if maxPrice < price:
        maxPrice = price
        maxVegetable = key

print("maxVegetable={0} maxPrice={1}".format(maxVegetable, str(maxPrice)))

print("------- Find total price for all vegetable ---------")
totalPrice = 0
for key in dict4:
    price = int(dict4[key])
    totalPrice = totalPrice + price

print(totalPrice)

print("---------- End ----------")

dict5 = {
    "jean": 30,
    "T-shirt": 25
}

for key in dict5:
    print("dress={0} price={1}".format(key, dict5[key]))

print("-------- Find dress with max price --------")
maxDress = ''
maxPrice = 0
for key in dict5:
    price = int(dict5[key])
    if maxPrice < price:
        maxPrice = price
        maxDress = key

print("maxDress={0} maxPrice={1}".format(maxDress, str(maxPrice)))





