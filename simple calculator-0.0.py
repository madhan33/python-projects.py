#program make a simple calculator


#this function add two numbers

def add (x,y):
    return x+y

#this function subtract two numbers

def subtract (x,y):
    return  x-y

#this function multiply two numbers

def multiply  (x,y):
    return x*y

#this function  divide two numbers

def divison(x,y):
    return x/y

#this function floor divison two numbers

def floordivison(x,y):
    return x//y


print("select operation.")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divison")
print("5. floordivison")

#take input from the user
choice = input("ENTER YOUR CHOICE (1/2/3/4/5): ")

num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))


if choice == '1':
 print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divison(num1,num2))

elif choice == '5':
    print(num1,"//",num2,"=",floordivison(num1,num2))
else:
    print("invalid input")
    




 
