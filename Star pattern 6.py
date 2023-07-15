
a=int(input("Enter="))
for i in range(1,a):
    print(" "*(a-i),"*"*i,sep="")
for i in range(a,0,-1):
    print(" "*(a-i),"*"*i,sep="")