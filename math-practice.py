import math

nums = [8, 4, 2, 9, 2]
maxNum = max(nums)
print("max number is {}".format(maxNum))

minNum = min(nums)
print("min number is {}".format(minNum))

print("-------- End ---------")


nums = [33, 21, 10, 40, 58]
maxNum = nums[0]
for x in nums:
    if maxNum < x:
        maxNum = x

print("max number is {}".format(maxNum))

minNum = nums[0]
for x in nums:
    if minNum > x:
        minNum = x
print("min number is {}".format(minNum))

print("------ End ---------")

num = -10
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 2
num_y = 4
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------ End -------")

num = 20
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 4
num_y = 3
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------- End -------")

num = -30
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 3
num_y = 3
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------ End ------")

num = 40
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 11
num_y = 2
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("-------- End -------")

num = -50
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 10
num_y = 2
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------- End --------")

num = 60
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 23
num_y = 3
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------- End --------")

num = -1
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 6
num_y = 7
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))
print("------- End -------")

num = -22
print("absolute value for {} is {}".format(num, abs(num)))

num_x = 4
num_y = 7
print("{} power {} is {}".format(num_x, num_y, pow(num_x, num_y)))

num = 4
print("square root of {} is {}".format(4, math.sqrt(num)))

num = 4.2
print("floor of {} is {}".format(4, math.floor(num)))

num = 4.2
print("ceil of {} is {}".format(4, math.ceil(num)))

print("------- End --------")
num = 5
print("square root of {} is {}".format(5, math.sqrt(num)))

num = 5.2
print("floor of {} is {}".format(5, math.floor(num)))

num = 5.2
print("ceil of {} is {}".format(5, math.ceil(num)))


