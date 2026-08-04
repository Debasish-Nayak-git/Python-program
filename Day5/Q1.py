name=input("Enter your name:")
reg=int(input("Enter your redg. no:"))
Department=input("Enter your Department:")
Email=input("Enter your Email:")
count,consonant=0,0
vowel="aeiouAEIOU"
for i in name:
    if i.isalpha():
        if i in vowel:
            count=count+1
        else:
            consonant=consonant+1
print("Reverse of name:",name[::-1])
check=name.replace(" ","").lower()
if check==check[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
print("name=",name)
print("redg. no.=",reg)
print("Department=",Department)
print("Email=",Email)
print("no. of vowel=",count,",no. of consonant=",consonant)
print("no. of character=",count+consonant)