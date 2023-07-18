a=int(input("Enter="))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(91-j),end="")
    print()