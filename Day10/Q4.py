#accept and write n sentences
N=int(input("number of sentences: "))
f=open("test.txt","w")
for i in range(N):
    sentence=input("Enter sentence: ")
    f.write("{}".format(sentence) + "\n")
f.close()