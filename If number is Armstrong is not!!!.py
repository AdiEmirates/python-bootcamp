Input = int(input("Input: "))
number = Input
no = 0
no += (number%10)**3
number = number//10
no += (number%10)**3
number = number//10
no += (number%10)**3
if no==Input :
  print(Input," is an Armstrong Number")
else :
  print(Input," is not an Armstrong Number")