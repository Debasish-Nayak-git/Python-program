class Head:
    name="head"
#single interitance Head->child
class child(Head):
    def display(self):
        print(super.name)
#hyrarchical inhertance Head->child and Head->son 
class son(Head):
    def check(self):
        super.display()
#Hybrid inhertance Head->child and son ->mul and multilevel Head->child->mul
#multiple inhertance Son ->mul and child->mul
class Mul(son,child):
    def ply(self):
        super.check(),super.display()