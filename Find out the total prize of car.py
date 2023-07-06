car_price=int(input("Carprice="))
tax=0
if car_price>=200000:
    tax=car_price*0.15
elif car_price<200000 and car_price>=100000:
    tax=car_price*0.1
elif car_price<100000:
    tax=car_price*0.05
print(tax)
print("Total=",car_price+tax)