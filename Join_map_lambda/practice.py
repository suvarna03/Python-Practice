#### Join function ####
####The string join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.
#### Syntax ###
## string.join(iterables) ----> join works only with string  objects
# list = ['python', 'and', 'data science']
# print(" ".join(list))
# list = " ".join(['python', 'and', 'data science'])
# print(list)

# list = [1,2,4,5]
# print(" ".join(list)) --> Error as join won't work with numbers


#### lambda function ####
### In Python, a lambda function is a special type of function without the function name.
### This function can have any number of arguments but only one expression, which is evaluated and returned.
##### Syntax ######
## ----> lambda argument(s) : expression
## ----> argument(s) - any value passed to the lambda function
## ----> expression - expression is executed and returned

#### Example #####
# # lambda that accepts one argument
# greet_user = lambda name : print('Hey there,', name)
#
# # lambda call
# greet_user('Delilah')


# mul = lambda x : print(x*2)
# mul([1,2,3])

### WAP to reverse the string with lower case
# str = lambda x : x.lower()[::-1]
# print(str("PYTHON"))

### WAP to find Max number between two numbers
# large = lambda x, y: x if(x > y) else y
# print(large(5,6))

###WAP to convert list of string with upper case
# upp = [lambda i: i.upper()[::-1] for i in ['python','machine learning','data science']]
# # print(upp) # --> will display object of lambda function
# for item in upp:
#     print(item)

#
# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#
# # iterate on each lambda function
# # and invoke the function to get the calculated value
# for item in is_even_list:
#     print(item())



### ------ Lambda function with filter() -----###
### Basically filter() function works with function and arguments---> filter(function(), arguments)
## ----> Example -->

# list = list (filter(lambda x : x%2 == 0, range(0,10)))
# print(list)


### ========== Map( )======
##====Being a higher-order function, the map function takes another function and an iterable (e.g., a list, set, tuple) as input, applies the function to the iterable, and returns an output. It’s syntax is defined as follows:

##== map(function, iterable)==--> Output of Map function will be map object so that we need to convert this into iterables


### ========= Reduce() =====
## =====An emoji example:

## reduce(mix, [🥬,🥕,🍅,🥒]) →🥗

####As mentioned, the reduce function is typically used for operations such as summing or multiplying all elements in a list


## ========= Example ==========
### dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

### map(lambda x : x['name'], dict_a) # Output: ['python', 'java']

### map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]

### map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]


### ================ Exercise =============

##write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = list(filter((lambda x : x < 5), a))
# print(result)

### Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

# number = int(input("Enter the number "))
# result = list(filter((lambda i: number % i ==0) , range(1, number+1)))
# print(result)

### Create a program that prints commons elements in given 2 lists
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda x: x in a,b))
# print(result)

### String is palindrom or not
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# print("Orginal list of strings:")
# print(texts)
# result = list(filter(lambda x: (x == x[::-1]), texts))
# print("\nList of palindromes:")
# print(result)

# string = ["12321","abcd","php"]
# result =list(map((lambda x : "palindrom" if x == x[::-1] else "not palindrom"),string))
# print(result)
