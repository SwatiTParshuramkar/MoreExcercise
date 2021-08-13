# i=1
# b=[]
# while i < 100:
#     if  i % 21 == 0:
#         a=(i,"Navgurukul")
#         b.append(a)
#     elif i % 7 == 0:
#         a= (i,"Gurukul")
#         b.append(a)
#     elif i % 3 == 0 :
#         a=(i,"Nav")
#         b.append(a)
#     i+=1
# print(b)


def multiple(num):
    i=1
    b=[]
    while i < num:
        if  i % 21 == 0:
            a=(i,"Navgurukul")
            b.append(a)
        elif i % 7 == 0:
            a= (i,"Gurukul")
            b.append(a)
        elif i % 3 == 0 :
            a=(i,"Nav")
            b.append(a)
        i+=1
    return b
number = int(input("Enter the number"))

print(multiple(number))

