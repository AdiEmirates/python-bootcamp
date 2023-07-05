
salary=int(input("Enter salary="))
tax=0
if salary<=300000:
    tax=0   
elif salary<=500000:
    tax=0+(salary-300000)*0.05
elif salary<=1000000:
    tax=0+(salary-300000)*0.05+(salary-500000)*0.1
elif salary<=2000000:
    tax=0+(salary-300000)*0.05+(salary-500000)*0.1+(salary-1000000)*0.2
elif salary<=3000000:
    tax=0+(salary-300000)*0.05+(salary-500000)*0.1+(salary-1000000)*0.2+(salary-1500000)*0.3

print("tax=",tax)
