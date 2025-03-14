# # Quest 1 square of n no. =============================

def squa(n):
    n = int(input("Enter the no.:= "))
    root = n**2
    return (root)

value = squa(6)
print(value)

# # Quest 2 Return of sum of 2 no. ====================================

def sum(a,b):
    add = a + b
    return add

print(sum(3,3))

# # Quest 3 Mult of 2 no. of any str in the def funuction ========================

def mult(a,b):
    return a * b

value = mult(3,"Monty")
print(value, end =" ")

# # Quest 4 Area and circumifarence of the circle 

def circle(r):
    p = 22.7
    area = p * (r ** 2)
    circumifarence = 2*p*r
    print("Area of the circle is := ",area,"And")
    print("circumifarence of the circle is := ",circumifarence )

circle(7)

# # Quest 5 Write a function that greets a user. if no name is provided, it should greet with a default name.

def greets(name = "user"):
    return ("Welcome", name, "in this world ")

print(greets())

# # Quest 6 create a lambda function to find the cube of the no. 

def cube(a):
    return a ** 3  # this is not a lambda fun.

print(cube(3))

# #  lambda fun =====================

cube = lambda a: a ** 3

print(cube(4))

# # Quest 7 write a function that takes variable number of arguments and return their multipal of 2

def value(*args):
    for i in args:
        print( i * 2)
    return sum(args)

print(value(5,3,4))

# # Quest 8 Create a function any number of keyword argument and print them in the format

def heros(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end = " ")

heros(name = "Hulk", power = "Thunder clap", end =  " \n" )
heros(name = "Spiderman", power = "Spider web", end = " \n")
heros(name = "Thor", power = "Thunder stom ", end = " \n")

# # Quest 9 Write a genrator function that yields even number up to a specfied limit.

def even_no(value):
    for i in range(2, value + 1, 2):
        yield i
       
for num in even_no(10):
    print(num)


# # Quest 10 Create a recursive function to calculate the factore of a number

def mult(a):
    count = 1
    total_mult = a 
    while count <= a -1 :
        total_mult = count * total_mult
        count += 1
    return total_mult

print(mult(6))

# # or ========== using of recursive function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1 )
    
print(factorial(5))