phrase="ram is a boy he studies in herald college kathmandu,he is very popular among students in college"
phrase=phrase.lower()
result={}
word_list=phrase.split()
for word in word_list:
    if word not in result:
        result[word]=1
    else:
        result[word]+=1
print(result)        

