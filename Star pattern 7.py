a=int(input("Enter="))
for i in range(1,a+1):
    print("*"*i," "*((a-i)*2),"*"*i,sep="")