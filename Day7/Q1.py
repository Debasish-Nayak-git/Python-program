#generator function
sub=["math","chem","phy","bee","c"]
mark,sum=[97,94,95,95,98],0
def gen(n):
    for i in range (n):
        yield i
for j in gen(len(mark)):
    print(sub[j],":",mark[j])
    sum +=mark[j]
print("total marks =",sum)