animals = {"tiger", "sheep", "lion"}
a = "lion"
if a in animals:
    print("{0} found".format(a))

print("---------- end -----------")

fruits = {"apple", "orange", "mango"}
a = "orange"
b = "apple"
if a in fruits:
    print("{0} found".format(a))

if b in fruits:
    print("{0} found".format(b))

print("---------- end ----------")

dresses = {"jean", "T-shirt", "long frock"}
a = "jean"
b = "T-shirt"
c = "long sleeves"
if a in dresses:
    print("{0} found".format(a))

if b in dresses:
    print("{0} found".format(b))

if c in dresses:
    print("{0} found".format(c))

print("--------- end ---------")

vegetables = {"tomato", "potato", "carrot"}
a = "carrot"
if a in vegetables:
    print("{0} found".format(a))

b = "tomato"
if b in vegetables:
    print("{0} found".format(b))

print("--------- end ---------")

birds = {"parrot", "pigeon", "crow", "hen"}
a = "parrot"
if a in birds:
    print("{0} found".format(a))

b = "pigeon"
if b in birds:
    print("{0} found".format(b))

c = "hen"
if c in birds:
    print("{0} found".format(c))

d = "crow"
if d in birds:
    print("{0} found".format(d))

print("------- end ---------")

cars = {"tesla", "honda", "audi"}
a = "tesla"
if a in cars:
    print("{0} found".format(a))
b = "honda"
if b in cars:
    print("{0} found".format(b))
c = "audi"
if c in cars:
    print("{0} found".format(c))

# --------- find length of a set ----------------
total = len(birds)
print("total:{0}".format(str(total)))
print("-------- End birds ---------")

total = len(fruits)
print("total:{0}".format(str(total)))
print("--------- End fruits --------")

total = len(vegetables)
print("total:{0}".format(str(total)))
print("-------- End vegetables --------")

total = len(dresses)
print("total:{0}".format(str(total)))
print("-------- End dresses ----------")

flowers = {"lotus", "rose", "sunflower", "water lily"}
a = "lotus"
if a in flowers:
    print("{0} found".format(a))
b = "rose"
if b in flowers:
    print("{0} found".format(b))
c = "sunflower"
if c in flowers:
    print("{0} found".format(c))
d = "water lily"
if d in flowers:
    print("{0} found".format(d))

print("----- Find length of a set ---------")
total = len(flowers)
print("total:{0}".format(str(total)))

