####Python – Replace characters  in String list
## here we are replacing 'P/p' to "N/n" and 's/S' to 'q/Q'

str = 'Pythonp SLearnings'
li = list(str.replace(" ",""))
string ='PpSs'
print("********Before replacing the string********")
print(li)
for i in range(len(li)):
    if li[i] in string:
        li[i] = chr(ord(li[i])-2)
print("********After replacing the string********")
print(li)
