#total no of char,word ,lines and frequency of "the"
count_char,word,lines,freq_the=0,0,0,0
f=open("test.txt","r")
data=f.read()
for i in range(len(data)):
    if data[i]=="\n":
        lines += 1
    elif data[i]==" ":
        word += 1
    else:
        count_char += 1
    if data[i:i+3]=="the" or data[i:i+3]=="The":
        freq_the += 1
print("Total no of char:",count_char)
print("Total no of word:",word)
print("Total no of lines:",lines) 
print("Frequency of 'the':",freq_the)

f.close()