num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Addition
def add(num1, num2):
    print(num1,"+",num2,"=",num1+num2)

#Subtraction
def sub(num1, num2):
    print(num1,"-",num2,"=",num1-num2)

#Multiplication
def mul(num1, num2):
    print(num1,"*",num2,"=",num1*num2)

#Division
def div(num1, num2):
    res = num1/num2
    print(num1,"/",num2,"=",round(res, 5))

#Modulo division
def mod_div(num1, num2):
    res = num1%num2
    print(num1,"%",num2,"=",round(res, 5))

#Exponentiation
def expo(num1, num2):
    res = num1**num2
    print(num1,"^",num2,"=",round(res, 5))

#Printinting results by invoking functions
print("Results:")
add(num1,num2)
sub(num1,num2)
mul(num1,num2)
div(num1,num2)
mod_div(num1,num2)
expo(num1,num2)