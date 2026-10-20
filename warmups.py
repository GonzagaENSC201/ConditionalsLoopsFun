def pow(b, p):   
    y = b ** p   
    return y

def square(x):   
    a = pow(x, 2)   
    return a

n = 5
result = square(n)
print(result)

x = -10
if x < 0:
    print("The negative number",  x, "is not valid here.")
print("This is always printed")

x = 3
y = 5
z = 2
if x < y and x < z:      
    print("a")  
elif y < x and y < z:      
    print("b")  
else:      
    print("c")


age = 10
height_cm = 119
if age >= 8:
    if height_cm >= 120:
        print("You can ride!")
    else:
        print("Too short")
else:
    print("Too young")