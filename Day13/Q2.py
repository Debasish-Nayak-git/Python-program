marks=[]
class student:
    def name(self):
        name=input("stu name:")
class mark:    
    def input_mark(self):    
        list1=["math","Bee","Ds","Coa","Python"]
        for i in range (5):
            n=float(input("enter the mark of {}".format(list1[i])))
            marks.append(n)
    r=lambda self,a:("O" if a>=90 else "A" if a>=70 else "B" if a>=50 else "fail")
class result(student,mark):
    def display(self):
        res.input_mark()
        res.name()
        print("Total=",sum(marks),"\npercentage=",sum(marks)/5)
        print("grade",res.r(sum(marks)/5))
res=result()
res.display()