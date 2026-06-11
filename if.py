#if , elif , else statement 
age= int(input("enter your age:"))
has_ticket=True
price= 10.00

if age >= 18: 
    print("you are an adult")
    print(f"the ticket price for you is {price*0.75}")

elif age==0:
    print("you were just born")
    print(f"the ticket price for you is {price}")
else:
    print("you are an child")
    print(f"the ticket price for you is {price*0.5}")


if has_ticket:
    print("you may enter")
else:
    print("buy ticket")