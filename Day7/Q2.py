#multiple return
mark=[95,97,98,87,93]
def check(a):
    return sum(a),sum(a)/len(a),max(a),min(a)
r=check(mark)
print("total mark=",r[0],"\navg mark=",r[1])
print("max mark=",r[2],"\nmin mark=",r[3])