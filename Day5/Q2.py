Email=input("Enter your Email:")
spe,digit,letter=0,0,0
part=Email.split("@")
name=part[0]
domain=part[1]
new=input("new domain=")
mod_email=name+"@"+new
for i in Email:
    if i.isalpha:
        letter +=1
    elif i.isdigit():
        digit +=1
    else:
        spe +=1
print("username=",name)
print("domain =",domain)
print("new email=",mod_email)
print("no. of letter=",letter,",no. of digit=",digit,",no. of special char=",spe)