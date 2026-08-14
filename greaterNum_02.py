# Here is a Python program that uses recursion to find the greatest of three numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def find_greatest(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    elif a==b==c:
        return "All numbers are equal"
    else:
        return c

print(find_greatest(num1,num2,num3))
