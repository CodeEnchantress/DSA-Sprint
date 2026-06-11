name= input("enter your name")

while name=="":
    name= input("enter your name:")

age= int(input("enter your age:"))


while age<0:
    print("age cant be less then 0")
    age= int(input("enter your age:"))

print(f"hello{name}")
print(f"your age is {age}")