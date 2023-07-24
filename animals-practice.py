f = open('animals.csv', 'r')
for line in f:
    print(line.rstrip())

print("------- Find animal with max weight and max height ------")
f = open('animals.csv', 'r')
maxWeightAnimal = ''
maxWeight = 0
maxHeightAnimal = ''
maxHeight = 0
for line in f:
    arr = line.split(',')
    weight = int(arr[1])
    height = int(arr[2])
    if maxWeight < weight:
        maxWeightAnimal = arr[0]
        maxWeight = weight

    if maxHeight < height:
        maxHeightAnimal = arr[0]
        maxHeight = height

print('max weight animal=' + maxWeightAnimal + ',  max weight=' + str(maxWeight))
print('max height animal=' + maxHeightAnimal + ',  max height=' + str(maxHeight))

print("-------- Find total weight and total height for all animals -------")
f = open('animals.csv', 'r')
totalWeight = 0
totalHeight = 0
for line in f:
    arr = line.split(',')
    weight = int(arr[1])
    totalWeight = totalWeight + weight
    height = int(arr[2])
    totalHeight = totalHeight + height

print('total weight=' + str(totalWeight))
print('total height=' + str(totalHeight))


