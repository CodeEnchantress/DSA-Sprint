#list []= mutable , most flexible
#tuple()= immutable , faster
#set{}= mutable (add/remove), unordered, no dupilcate , best for membership testing 

fruit= ["apple", "orange", "banana", "coconut"]
#list are mutable so i can change the elemenets in the list 

fruit[0]= "mango"
#WE CAN REMOVE ANY ELEMENT using remove cammand 
fruit.remove("banana")
#we can add elements using append command
fruit.append("lichi")
#we can also use pop command 
fruit.pop(0)


for fruit in fruit :
    print(fruit )