cource=["btech","bca","bsc","mtech","mba"]
fees=[5.6,3.2,1.2,2.8,6]
duration=[4,3,3,2,2]
id=[123,124,125,126,127]
h,l=fees.index(max(fees)),fees.index(min(fees))
print("Avialave cource",":Btech",",Bca",",Bsc",",Mtech",",Mba")
ch=input("Enter year choice:")
search=lambda a:True if a.lower() in cource else False
if search(ch):
    i=cource.index(ch.lower())
    print("Cource id:",id[i],"\nName:",cource[i])
    print("Duration:",duration[i],"\nfees:",fees[i],"lakh")
print("\n Highest fees:")
print("Cource id:",id[h],"\nName:",cource[h])
print("Duration:",duration[h],"\nfees:",fees[h],"lakh")
print("\n Lowest fees:")
print("Cource id:",id[l],"\nName:",cource[l])
print("Duration:",duration[l],"\nfees:",fees[l],"lakh")