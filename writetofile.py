f = open('dresses.csv', 'w')
f.write("jean,25")
f.write("\n")
f.write("t-shirt,15")
f.close()

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
