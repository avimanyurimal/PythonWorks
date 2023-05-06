line="hello my name is avimanyu"
count=0
for c in line:
    if c != "" and c !="\n":
        count+=1
        print("the string has", count,"non_blank non_newline characters.")