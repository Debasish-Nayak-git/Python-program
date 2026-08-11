#local and global variable
a=10
def fun():
    b=10
    print("local",b)
    print("global",a)
fun()
print("global",a)