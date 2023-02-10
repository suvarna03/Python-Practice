my_dict = {'name': 'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))

list_details = ['salary','state','department']
list_info = [12000,'maharashtra', 'QA']


for key in range(len(list_details)):
  for value in range(len(list_info)):
     if type(list_info[value]) == int:
        if list_info[value] < 15000:
            my_dict[list_details[key]] = 'less salary'
            list_info.remove(list_info[value])
            break
     else:
         my_dict[list_details[key]] = list_info[value]
         list_info.remove(list_info[value])
         break

print(my_dict)
