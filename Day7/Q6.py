#keyword only argument
name=input("name:")
reg=int(input("reg no:"))
mark=[95,97,98,87,93]
def key(na,*,re,ma):
    print("name=",na,"\nreg no:",re,"\nmarks:",ma)
key(name,re=reg,ma=mark)