subject=["math","python","iwt","coa"]
mark=[]
for i in range(4):
    print("mark of ",subject[i],":")
    a=int(input())
    mark.append(a)
pass1=sum(1 for m in mark if m>=40)
fail=sum(1 for m in mark if m<40)
print("passed subject:",pass1,"\nFailed subject:",fail)
print("highest mark:",max(mark),"lowest of mark:",min(mark))