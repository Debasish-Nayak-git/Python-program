#N no. of students
N=int(input("Enter the number of students: "))
f=open("name.txt","w")
for i in range(N):
    name=input("name of student : ")
    f.write("Name: {}\n".format(name))
f.close()