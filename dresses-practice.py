f = open('dresses.csv', 'r')
for line in f:
    print(line.rstrip())

print("------- Find dress with max price -------")
f = open('dresses.csv', 'r')
maxDress = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxDress = arr[0]

print(maxDress + ': ' + str(maxPrice))

print("------- Find total price for all dresses --------")
f = open('dresses.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)




