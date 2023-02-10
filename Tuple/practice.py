###Find minimum and maximum 2 elements from given tuple without sorting
# tuple = (3,2,6,1,5,4)
# list = list(tuple)
# temp = 0
# for i in range(len(list)):
#     for j in range(i+1, len(list)):
#         if list[i] > list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list[0], list[1], list[-1], list[-2])


###Python program to create a list of tuples from given list having number and its cube in each tuple
# list1 = [1, 2, 5, 6]
# tuple_list = []
# for i in list1:
#     tuple_list.append((i, i**3))
#
# print(tuple_list)

#### Add number in given tuple
# test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
# print(test_list)
# update = [tuple(j+5 for j in i) for i in test_list]
# print(str(update))
