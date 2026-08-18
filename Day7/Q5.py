sen=input("Enter a sentence:")
word=sen.split(" ")
vowel="AEIOUaeiou"
special="*/-+~!@#$%^&*()_+|"
alphabet="qwertyuiopasdfghjklzxcvbnm"
no_lower,no_vowel,no_consonant,no_special=0,0,0,0
def check(a):
    global no_lower,no_vowel,no_consonant,no_special
    for i in a:
        for j in i:
            if j in special:
                no_special +=1
            if j.isalpha():
                if j in vowel:
                    no_vowel +=1
                else:
                    no_consonant=no_consonant+1
            if j in alphabet:
                no_lower += 1
check(word)
print("no of upper=",(no_consonant+no_vowel-no_lower))  
print("no of lower=",no_lower)  
print("no of vowel=",no_vowel)
print("no of consonant=",no_consonant)  
print("no of words=",len(word))
print("no of special character=",no_special)