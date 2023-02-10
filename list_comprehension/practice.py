### Iteration with List comprehension
# list = [i+2 for i in [1,2,3]]
# print(list)

### For and if loop Iteration with List comprehension
##Print the even numbers for given range
# list = [["Even", i] for i in range(1,21) if i % 2 == 0 ]
# print(list)

### Nested loop with list compehension
# list = [[i,j] for i in range(2) for j in range(3)]
# print(list)

### if else with list comprehension
# list = ["Even number" if i%2 == 0 else "odd number" for i in range (1,10)]
# print(list)

###nested IF loop with list comprehension
# list = [i for i in range(100) if i%5 == 0 if i%7 == 0]
# print(list)

### nested elif loop with list comprehension
##usecase numbers form 1-6
# if number equal  3 --> number, equal number
# elif : number less than 3 --> number, less than 3
# else: greater than 3
# list = [("{} is equal number".format(i)) if i == 3 else ("{} is less than number".format(i)) if i < 3 else ("{} is greater than number".format(i)) for i in range(1,6)]
# print(list)

#### Drawback of list comprehension
## without list comprehension
# first_names = ['John', 'Danny', 'Aaron']
# last_names = ['Smith', 'Brown', 'Thompson']
# for i in zip(first_names,last_names):
#     print(" ".join(i))

## with list comprehension
# first_names = ['John', 'Danny', 'Aaron']
# last_names = ['Smith', 'Brown', 'Thompson']
# names = [' '.join(x) for x in zip(first_names, last_names)]
# for name in names:
#     print(name)


#### Where you should skip list comprehension
## When you don't want output in list data type --> as list comprehension returns list object
## When the condition is large
## when you want to add comments with every condition
