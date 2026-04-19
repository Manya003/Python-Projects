# List Comprehension range for printing table.

num = int(input("Enter the number: "))

table = [num * i for i in range(1, 11)]

for i in range(10):
    print(f"{num} x {i+1} = {table[i]}")
