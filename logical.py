""" logical operator = evaluate multiple condtion(or, not , and)
or = at least one condtion must be true
and = both the condtion need to be true 
not = inverts the condtion (not false , not true)

"""
 #or 
#temp= 25
#is_raining = True
#if temp>35 or temp< 0 or is_raining :
 #   print("event is cancelled")
#else:
 #   print("the event is still scheduled")

#and
print("hellop")
temp=25
is_sunny= True
if temp>=28 and is_sunny:
    print("it is sunny")
elif temp <=0 and is_sunny:
    print("this cold")
else:
    print("not sunny")

#not

temp=18
is_sunny= True
if temp>=28 and is_sunny:
    print("it is sunny")
elif temp <=0 and not is_sunny:
    print("this cold")
    print("its cloudy")
elif temp >15 and not  is_sunny:
    print("this cold")
    print("its cloudy")
elif temp <=0 and not is_sunny:
    print("this cold")
else:
    print("not sunny")

