#function annotation
name=input("name:")
reg=int(input("reg no:"))
mark=[95,97,98,87,93]
def fun(n:str,r:int,m:list):
    print("name=",n,"\nreg no:",r,"\nmarks:",m,"\ntotal=",sum(m))
fun(name,reg,mark)