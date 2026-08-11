def test(*args):
    print("sum=",sum(args))
    print("avg=",(sum(args)/len(args)))
    print("max=",max(args))
    print("min=",min(args))
test(12,24,85,87,19)