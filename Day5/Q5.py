feedback=input("your feedback:")
part=feedback.split(" ")
pos,neg,ch=0,0,0
positive=["good","exellent","happy","nice"]
negative=["bad","poor","slow","worst"]
for i in range(len(part)):
    if part[i].lower() in positive:
        pos=pos+1
    elif part[i].lower() in negative:
        neg=neg+1
    else:
        pass
    ch=ch+len(part[i])
if pos>neg:
    print("positive feedback")
elif pos<neg:
    print("negative feedback")
else:
    print("neutral feedback")
print("total words=",len(part))
print("total characters=",ch)