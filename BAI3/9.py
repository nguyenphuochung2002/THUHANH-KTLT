print("sinh viên : Nguyen Phuoc Hung 205751030110042")
###########################
#this funtion adds two numbers
def add(x,y):
    return x+y
#this funtion subtracts two numbers
def subtract(x,y):
    return x-y
#this funtion multiplies two numbers
def multiply(x,y):
    return x*y
#this funtion divides two numbers
def divide(x,y):
    return x/y
print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

#take input from the user
choice=input("enter choice(1/2/3/4):")
num1=int(input("enter first number:"))
num1=int(input("enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
     print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
     print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
     print(num1,"/",num2,"=",devide(num1,num2))
else:
    print("invalid input")
