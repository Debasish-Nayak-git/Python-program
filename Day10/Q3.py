#count no. of alphabet capital,small,digit and special character in a text file
upper,lower,digit,special=0,0,0,0
f=open("name.txt","r")
data=f.read()
for i in data:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1
print("Upper case letters:",upper)
print("Lower case letters:",lower)
print("Digits:",digit)
print("Special characters:",special)
f.close()