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