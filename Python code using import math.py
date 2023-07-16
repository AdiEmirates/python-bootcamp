import math
n=int(input("Enter="))
angle=int(input("angle="))
rad=angle*(22/7)/180
sum=0
for i in range(0,n):
    sum=sum+(((-1)**i)*rad**(2*i+1)/math.factorial(2*i+1))

print(sum)