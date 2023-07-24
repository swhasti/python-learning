f = open('fruits.csv', 'r')
for line in f:
    print(line)

print("------- Find fruit with max price --------")
f = open('fruits.csv', 'r')
maxFruit = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxFruit = arr[0]

print(maxFruit + ": " + str(maxPrice))

print("------- Find total price for all fruits --------")
f = open('fruits.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)
