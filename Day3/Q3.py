stu=int(input("enter no. of students"))
py,em,eng,bee,iwt,no,fail=0,0,0,0,0,0,0
for i in range(stu):
    name=input("Enter your name:")
    py=int(input("py result:"))
    em=int(input("em result:"))
    eng=int(input("eng result:"))
    bee=int(input("bee result:"))
    iwt=int(input("iwt result:"))
    total=(py+em+eng+bee+iwt)
    avg=total/5
    per=(total/500)*100
    if avg>=90:
        grade="A+"
    elif avg>=80:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=60:
        grade="C"
    elif avg>=50:
        grade="D"
    else:
        fail+=1
        grade="Fail"
    if py<40:
        no+=1
    if em<40:
        no+=1
    if eng<40:
        no+=1
    if bee<40:
        no+=1
    if iwt<40:
        no+=1
    if no>0:
        print("name:",name)
        print("Grade=",grade)
        print(name ," fail in ",no," subjects")
    else:
        print("name:",name)
        print("Grade=",grade)
        
print((stu-fail)," students are pass")
print(fail," students are fail")