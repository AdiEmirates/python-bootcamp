Student_1=int(input("Enter the Student1="))
Student_2=int(input("Enter the Student2="))
Student_3=int(input("Enter the Student3="))
if Student_1>Student_2:
    if Student_1<Student_3:
        greatest=Student_3
    else:
        greatest=Student_1
else:
    if Student_2<Student_3:
        greatest=Student_3
    else:
        greatest=Student_2
print("Largest is",greatest)

a=int(input("Enter the number:"))
sum=0
for i in range(1,a+1):
    sum=sum+i

print(sum)