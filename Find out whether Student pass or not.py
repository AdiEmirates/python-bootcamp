subject="Maths"
marks=int(input("Enter the marks="))
if marks<45:
    print("Failed")
elif marks>45:
    print("pass in",subject)
elif (45<marks and marks<=60):
    print("Good in",subject)
elif (61<marks and marks<=75):
    print("Very good",subject)
elif (76<marks and marks<=100):
    print("Excellent in",subject)