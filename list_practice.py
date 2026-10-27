import random

random.seed(0) # we get the same random #s every time we run our program

nums = []
for i in range(20):
    rand_num = random.randrange(1, 11) # [1, 11)
    # rand_num = random.randint(1, 10) # [1, 10]
    nums.append(rand_num)

print(nums)

# 1.a.
for num in nums:
    print(num, end=" ")
print() # to get a newline after loop
print("here")

# 1.b.
nums.sort() # sorts the original list
print(nums)

# 1.c.
print("min:", nums[0])
print("max:", nums[-1])

# 1.d.
user_num = int(input("Enter a number in [1, 10]: "))
print(nums.count(user_num))

# 1.e.
if user_num in nums:
    while user_num in nums:
        nums.remove(user_num)
else:
    print("Sorry, your number is not here!")
print(nums)

# practice problem #2
table = []
for i in range(10):
    row = []
    for j in range(5):
        row.append(random.randrange(1, 11))
    table.append(row)

print(table)
# 2.a.
for row in table:
    for val in row:
        print(val, end=" ")
    print()
print()

# 2.b.
smallest = 11 # 11 is outside of [1, 10]
largest = 0
for row in table:
    if min(row) < smallest:
        smallest = min(row)
    if max(row) > largest:
        largest = max(row)
print("smallest:", smallest)
print("largest:", largest)

# 2.c.
user_num = int(input("Enter a number in [1, 10]: "))
table_count = 0
for row in table:
    table_count += row.count(user_num)
print(table_count)

# 2.d.
found = False
for row in table:
    while user_num in row:
        found = True
        row.remove(user_num)

if not found:
    print("Sorry, your number is not here!")
print(table)