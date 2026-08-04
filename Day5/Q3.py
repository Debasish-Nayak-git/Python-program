sentence=input("sentence=")
new,count="",0
part=sentence.split(" ")
word=len(part)
mean=[]
for i in part:
    mean.append(i[::-1])
    new=new+i.upper()+" "
check=input("searched word=")
for i in part:
    if check==i:
        count +=1
print("modified sentence:",new)
print("reverse of each word:",mean)
print(check," present ",count," times")
