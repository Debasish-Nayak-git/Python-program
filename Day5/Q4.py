book=[]
for i in range(5):
    titel=input("input the titel:")
    book.append(titel)
short=book[0]
long=book[0]
word=0
for i in book:
    if len(i)>=len(long):
        long=i
    if len(i)<=len(short):
        short=i
check=input("searched word=")
for i in book:
    words=i.split(" ")
    for j in words:
        if check.lower()==j.lower():
            print(check," is found ")
            break
print("Longest titel=",long)
print("smallest titel=",short)
for i in book:
    print(i," ,no. of words=",len(i.split()))
book.sort()
print(book)