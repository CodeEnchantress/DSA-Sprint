#set{}= mutable (add/remove), unordered, no dupilcate , best for membership testing 
fruits= { "apple", "mango", "coconut", "orange"}
#sets do not follow index assignemet cuz they are unordered 

#fruits.add("lichi")
#fruits.remove("mango")
#fruits.clear()
fruit= input("enter the fruit to be found: ")
if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} not found")
