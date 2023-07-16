
a=int(input("Enter="))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print(" "*(2*(a-j)),end="")
    for j in range(j,0,-1):
        print(chr(j+64),end="")
    print()