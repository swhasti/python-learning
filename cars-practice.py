f = open('cars.csv', 'r')
for line in f:
    print(line.rstrip())

print("------- Find car with max price -------")
f = open('cars.csv', 'r')
maxCar = ''
maxPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    if maxPrice < price:
        maxPrice = price
        maxCar = arr[0]

print(maxCar + ': ' + str(maxPrice))

print("------- Find total price for all cars -------")
f = open('cars.csv', 'r')
totalPrice = 0
for line in f:
    arr = line.split(',')
    price = int(arr[1])
    totalPrice = totalPrice + price

print(totalPrice)