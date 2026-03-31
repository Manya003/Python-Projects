# List->
numbers = [1,2,3,4]
print(numbers[0])

# insert
numbers.insert(0,99)

# append
numbers.append(34)
print(numbers)

# checking if this thing exist in list or not.
print(99 in numbers)

# length
print(len(numbers))

# printing list using while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# clear list
numbers.clear()
print(numbers)


# Tuple->

marks = (95, 80, 70, 95, 95)
# this gives error as tuple is immutable
# marks[0] = 68

# count
print(marks.count(95))

# index
print(marks.index(95))

# set-> storing collection of only unique elements. Set is unordered as it does not contain indexes.
marks = {20, 41, 52, 63, 74, 94} # prints 24 only one time as set stores unique elements.
print(marks)

# Incase of set you cannot access the values using index. You need to use Loop for accessing.
# print(ages[0])

for score in marks:
    print(score)

# dictionary-> stores data in key value pairs.
marks = {"english" : 98, "physics": 95, "Maths": 98}
marks["chemistry"] = 54
print(marks)

marks["chemistry"] = 97
print(marks)

