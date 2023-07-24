import json

s = '{"vegetable": "tomato", "color": "red"}'

js = json.loads(s)
print("vegetable is {}".format(js["vegetable"]))
print("color is {}".format(js["color"]))

print("--------- End -----------")

s = '{"flower": "rose", "color": "red", "leaves": "green"}'

js = json.loads(s)
print("flower is {}".format(js["flower"]))
print("color is {}".format(js["color"]))
print("leaves is {}".format(js["leaves"]))

print("------------ End ----------")

america = '{"code": "US", "states": ["California", "Texas", "Arizona", "New York", "Florida"]}'
stateToFind = input("enter state:")

am = json.loads(america)
states = am["states"]
found = False
for state in states:
    if state == stateToFind:
        found = True
        break
print("is state '{}' found? {}".format(stateToFind, found))

print("---------- End -------------")
