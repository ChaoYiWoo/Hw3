sentence = input("Please type anything:\n")
a = list(sentence)
dic = {}
a.sort()
for word in a :
    if word in dic:
        dic[word] = dic[word]+1
    else:
        dic[word] = 1

for key in dic.keys():
    print("'",key,"': ",dic[key],sep='')
