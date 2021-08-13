# def convert(lst): 
#     return (lst[0].split()) 
  
# lst =  ["NavGurukul is an alternative to higher education reducing the barriers of current formal education system"] 
# print( convert(lst)) 


sentence = 'This is a sentence'
split_value = []
tmp = ''
for c in sentence:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_value.append(tmp)
print(split_value)


# words = "navgurukul is great"
# counter = 0
# b=[]
# t=" "
# while counter < len(words):
#     if " " in words:
#         t += words[counter]
#     b.append(t)        
#     counter+=1

