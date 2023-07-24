def sum_of_even_numbers(nums):
    value = 0
    for x in nums:
        if x % 2 == 0:
            value = value + x
    return value


def sum_of_odd_numbers(nums):
    value = 0
    for x in nums:
        if x % 2 == 1:
            value = value + x
    return value


def find_number(nums):
    for x in nums:
        if x == 2:
            return True
    return False


def find_length(name):
    count = 0
    for x in name:
        count = count + 1
    return count


def count_characters(input):
    count = 0
    for x in input:
        count = count + 1
    return count


def count_a_characters(input):
    count = 0
    for x in input:
        if x == 'a':
            count = count + 1
    return count


def count_any_characters(input, char):
    count = 0
    for x in input:
        if x == char:
            count = count + 1
    return count



def count_vowels_characters(input):
    count = 0
    for x in input:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'D':
            count = count + 1
    return count


def find_fruits(input):
    count = 0
    for x in input:
        if x == 'mango':
            count = count + 1
            print('I ate mango')


def find_animals(input):
    count = 0
    for x in input:
        if x == 'rabbit':
            count = count + 1
            print("I saw rabbit")


input1 = [1, 2, 3, 4, 5, 6]
input2 = [10, 20, 30, 40, 50 , 60]
# sum of even numbers
print(sum_of_even_numbers(input1))
print(sum_of_even_numbers(input2))

# sum of odd numbers
print(sum_of_odd_numbers(input1))
print(sum_of_odd_numbers(input2))

# find number
print(find_number(input1))
print(find_number(input2))
