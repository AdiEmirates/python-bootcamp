a=int(input("Enter="))
for i in range(1,a+1):
    print((a-i)*" ",end="")
    for j in range(1,i+1):
        print(chr(j+64),end="")
    for j in range(j-1,0,-1):
        print(chr(j+64),end="")
    print()
for i in range(a-1,0,-1):
    print((a-i)*" ",end="")
    for j in range(1,i+1):
        print(chr(j+64),end="")
    for j in range(j-1,0,-1):
        print(chr(j+64),end="")
    print()
