t=["Bideah",7,(56,85,97,45,12,35,0),(4,3,2,0,1,3,5)]
print("name=",t[0])
print("no. of matches played:",t[1])
for i in range(t[1]):
    print("match:",i+1)
    print("run:",t[2][i],"wickets:",t[3][i])
print("highest score:",max(t[2]),"wicket:",max(t[3]))
print("lowest score:",min(t[2]),"wicket:",min(t[3]))