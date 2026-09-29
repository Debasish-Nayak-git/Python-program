"""Write a Python program using a module and package to calculate
 the sum, average, maximum, and minimum of user-entered numbers.
"""
from classpython import oper 
list1=[56,75,84,65,23]
result=oper.r(list1)
list2=["total:","avg:","max:","min:"]
for i in range(len(result)):
    print(list2[i],result[i])
