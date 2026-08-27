# here's a program to calculate factorial using loop and recursion:
# using for loop
n=int(input("enter no"))
fact=1
for i in range(1,n+1):
  fact=fact*i

print("factorial of n is :",fact)

# # using while loop.
n=int(input("enter no"))
fact=1
i=1
while(i<=n):
  fact=fact*i
  i+=1
print("factorial of n is :",fact)
# # using recursion function:
def cal_fact(n):
  if n==0 or n==1 :
    return 1
  else:
    return cal_fact(n-1)*n
n=int(input("enter number"))
print("factorial of n is",cal_fact(n))