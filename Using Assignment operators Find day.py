days=int(input("Enter the days="))
print("There are",days//365,"Years",end=" ")
days=days%365
print(days//30,"Months",end=" ")
days=days%30
print(days//7,"Weeks",end=" ")
days=days%7
print("Days",days)