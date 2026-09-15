#csv file using user input
f=open("check.csv","w")
N=int(input("Enter the number of students: "))
for i in range(N):
    name=input("name:")
    roll=int(input("roll no:"))
    cgpa=float(input("cgpa:"))
    f.write("{},{},{}\n".format(name,roll,cgpa))
f.close()