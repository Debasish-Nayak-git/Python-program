sentence=input("Enter a sentence:")
vowel={"vowel":"aeiou"}
for i in vowel["vowel"]:
    count=0
    for j in sentence:
        if i.lower() ==j.lower():
            count+=1
    print(i," present ",count," times.")