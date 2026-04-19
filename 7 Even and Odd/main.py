# Even & Odd using List Comprehension

nums = list(range(1, 21))

even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]

print("Even:", even)
print("Odd:", odd)