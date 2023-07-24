f = open('vegetables.csv', 'r')
for line in f:
    print(line)

print("-------- Find vegetable with max price --------")
f = open('vegetables.csv', 'r')
maxVegetables = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxVegetables = arr[0]

print(maxVegetables + ": " + str(maxPrice))

print("------- Find total price for all vegetables-------")
f = open('vegetables.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)

