f = open('flowers.csv', 'r')
for line in f:
    print(line.rstrip())

print("-------- Find flower with max price -------")
f = open('flowers.csv', 'r')
maxFlower = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxFlower = arr[0]

print(maxFlower + ": " + str(maxPrice))

print("------ Find total price for all flowers --------")
f = open('flowers.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)

