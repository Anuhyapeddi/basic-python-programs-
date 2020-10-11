a=0
b=1
c=0
n=int(input('enter a number'))
print(a)
print(b)
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c
