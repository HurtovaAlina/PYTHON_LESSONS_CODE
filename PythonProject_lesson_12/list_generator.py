# генератор списків

# ls = []
# ls.append("Den")
# print(ls)

# list of random elements
# 1.
# ls = []
# for _ in range(10):
#     ls.append(random.randint(1, 100))
#
# print(ls)
# print(len(ls))
# 2.
# [вираз for елемент in ітератор <if умова>]
# ls = [random.randint(1, 100) for _ in range(10)]
# print(ls)
# # вибрати парні числа
# ls2 = [i for i in ls if i % 2 == 0]
# print(ls2)

# incorrect list -> to update and correct
# ls = ["  Den  ", "", "", "   ", "Bob", "  Alice"]
# ls = [s.strip().title() for s in ls if s.strip()]
# print(ls)

# [вираз_якщо_так <if умова> else вираз_якщо_ні for елемент in ітератор <if умова>]
#
# ls = [5, -2, 7, -8, 0, -1, 4]
# # replace negative numbers with 0
# ls = [n if n >=0 else 0 for n in ls]
# print(ls)

# ls = [5, -2, 7, -8, 0, -1, 4]
# # replace negative numbers with 0 but don't put 5 -> filters element in list before checking condition
# ls = [n if n >=0 else 0 for n in ls if n!= 5]
# print(ls)

# [значення, що повернеться, якщо умова вірна, УМОВА, значення що повернеться, якщо умова не вірна ІТЕРАТОР ПО СПИСКУ
# Умова фільтрації списку]
#
# list1 = [x*y for x in range(1,4) for y in range(1,4)]
# print(list1) # [1, 2, 3, 2, 4, 6, 3, 6, 9]
# for y in range(1,4):
#     for x in range(1, 4):
#         list1.append(x*y)
#
#
# list2 = [[x*y for x in range(1,4)] for y in range(1,4)]
# print(list2) #[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# ls = []
# for y in range(1,4):
#     temp = []
#     for x in range(1, 4):
#         temp.append(x*y)
#     ls.append(temp)
# print(ls)


# methods
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
# print(len(ls)) # length of listObj
# print(max(ls)) # max element of listObj
# print(min(ls)) # min element of listObj
# print(sum(ls)) # sum of elements of listObj only with numbers, parameter start = int(from what element sum)
# print(sorted(ls)) # Return a new list containing all items from the iterable in ascending order.
# # parameter reverse = True, sorts letters as well using ASCII. Returns new sorted list. To sort current ->
# # ls.sort(). In this case ls will be sorted
# print(enumerate(ls)) # numerates elements
#
# line = "hello"
# for i, v  in enumerate(line, 10):
#     #print( i, end=' ') # cortage (key, value) (0, 'h') (1, 'e') (2, 'l') (3, 'l') (4, 'o')
#     #print(v, i, end =' ')
#     print(i, v)


# ls = []
# ls.append("Hello")
# print(ls)
# ls.count("Hello") # -> count element in the list
# ls.pop() # -> cut last element of the list and returns, can remove by index. Raises exception of not found
# print(ls)
# ls.clear() # -> cleans list
# ls.insert(0, "Hello") # put to the list element by index
# ls = [1,2,3,4,5]
# # ls.insert(0, -10)
# # print(ls)
# # ls.remove(5) # removes first found element. Raise exception if not found -> use if to check
# ls2 = [6,7,8,9,0]
# ls.extend(ls2) # add to existing from other list
# print(*ls)
# ls.index(7) # returns index of element -> Raises exception if element not found, start and stop parameters
# # diapason for searching
# ls.reverse() # reversed list doesn't create new list

# COPY
# ls1 = [3,4,5]
# # ls2 = ls1 ->  only one list exists, ls2, ls1 - pointers to this list
# ls2 = ls1.copy()
# ls1[0] = 5
# ls2[1] = 5
# print(ls1)
# print(ls2)

# customers =["Bob", "Anna", "Joe", "Bob", "Nick"]
# # count = 0
# ind = -1
# for item in customers:
#     if item == 'Bob':
#         print(item)
#
# for i in range(len(customers)):
#     if customers[i] == 'Bob':
#         print(i, customers[i])
#         # count +=1 # counts elements
#         i +=1 # saves current index of the element / if returns -1 element not found

# MATRIX
# each row  is inner list
# 1. [1,2,4,5,6]
# 2. [2,3,4,6,6]

# list2 = [[x*y for x in range(1,4)] for y in range(1,4)]
# print(list2)
# for inner_list in list2:
#     for item in inner_list:
#         print(item, end = " ")
#     print()
# for inner_list in list2:
# #     for item in inner_list:
# #         print(item, end = " ")
#     print(inner_list)

# in the list where sum of elements <10 replace with 0

# for i in range(len(list2)):
#     summa = sum(list2[i])
#     if summa < 10:
#         list2[i] = [0] * len(list2[i]) # replace all elements with 0
# for item in list2:
#     print(item)

# Task

ls = [
    9,
    2,
    10,
    1,
    -10,
    -4,
    7,
    0,
    -4,
    -7 - 8,
]  # [random.randint(-10,10) for _ in range(10)]
print(ls)

# sum_neg = 0
# for x in ls:
#     if x>0:
#         sum_neg +=1
# print(sum_neg)
#
# sum_even =0
# sum_odd = 0
# for x in ls:
#     if x%2 == 0:
#         sum_even +=1
#     if x % 2 == 0:
#         sum_odd +=1
# print(sum_even, sum_odd)
#
# prod_idx3 = 1
# for i, x in enumerate(ls): # returns index
#     if x % 3 == 0:
#         prod_idx3 *=x # multiple indexes
# print(prod_idx3)

# mult elements between min and max

# max_val = ls[0]
# min_val = ls[0]
# max_i = 0
# min_i = 0
#
# for i in range(1, len(ls)):
#     if ls[i] > max_val:
#         max_val = ls[i]
#         max_i = i
#
#     if ls[i] < min_val:
#         min_val = ls[i]
#         min_i = i
# print(max_val, "[",max_i,"]", min_val, "[",min_i,"]")
#
# prod_between =1
# for i in range (min_i+1, max_i):
#     prod_between *=ls[i]
# print(prod_between)

# sum of elements between first positive and last positive
# positive_1 = ls[0]
# positive_2 = ls[0]
# ind_1 = 0
# ind_2 = 0
# count = 0
#
# for i in range(0, len(ls)):
#     if ls[i] > 0 and count ==0:
#         positive_1 = ls[i]
#         ind_1 = i
#         count += 1
#
#     if ls[i] >0  and count > 0:
#         positive_2 = ls[i]
#         ind_2 = i
# print(positive_1, "[",ind_1,"]", positive_2, "[",ind_2,"]")
#
# sum_between = 0
# for i in range(ind_1, ind_2+1):
#     sum_between += ls[i]
# print(sum_between)
