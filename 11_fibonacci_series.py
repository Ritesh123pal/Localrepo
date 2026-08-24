# fibonacci:0,1,1,2,3,5,8,13,21......,
N=22
a=0
print(a)
b=1
print(b)
c=a+b
print(c)
while(c<N):
    a=b
    b=c
    c=a+b
    print(c)


# find no by their index no
i=9
a=0
b=1
for x in range(i-1):
    c=a+b
    a=b
    b=c
print("\n",c)
