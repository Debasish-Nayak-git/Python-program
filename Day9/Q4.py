#student name and marks using dictionary
student={}
name=["Ashu","Brij","Chand","deb"]
mark=[90,80,70,60]
for i in range(len(mark)):
    student[name[i]]=mark[i]
highest=max(mark)
for s in student:
    if student[s]==highest:
        print("Highest mark=",highest,"obtained by ",s)