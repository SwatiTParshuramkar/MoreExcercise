# n = [ "Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# duplicate_n=[]
# index=0
# number=[]
# while index<len(n):
#     if n[index] not in duplicate_n :
#         duplicate_n.append(n[index])
#     # else :
#         # number.append(n[index])
#     index+=1
# print(duplicate_n)
# # print(number)

def duplicate_string(list1):
    duplicate_n=[]
    index=0
    number=[]
    while index<len(n):
        if n[index] not in duplicate_n :
            duplicate_n.append(n[index])
        index+=1
    return duplicate_n

n = [ "Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]

print(duplicate_string(n))

