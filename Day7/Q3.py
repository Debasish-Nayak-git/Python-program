#higher order function
mark=[95,97,98,87,93]
a=[]
def higher(t,a):
    return t(grade,a)
def sqr(x,k):
    for i in range(len(k)):
        a.append(k[i]**2)
    print("Squire of each marks:",a)
    return x(sum(k)/len(k))
grade=lambda a:("O" if a>=90 else
"E" if a>=80 else
"A" if a>=60 else "Fail")
print("Grade=",higher(sqr,mark))