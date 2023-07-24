f = open('tiffins.csv', 'r')
for line in f:
    print(line.rstrip())

print("------- Find tiffin with max price --------")
f = open('tiffins.csv', 'r')
maxTiffin = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxTiffin = arr[0]

print(maxTiffin + ": " + str(maxPrice))

print("------- Find total price for all tiffin --------")
f = open('tiffins.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)
