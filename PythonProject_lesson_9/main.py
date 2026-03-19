# string
# 'asd'
# "asd"
# """fghh"""
# name = "John" # immutable незмінний, змінити не можна, створити новий

# for i in range(1000): # print symbols UTF
#     print(f"{i} - {chr(i)}")
# передача даних по мережі (з одного проекту на інший) через кодування в бінарний формат

# userMessage = "привіт"
# userMessageEnc = userMessage.encode('utf-8')
# print(userMessageEnc)
#
# userMessageDec = userMessageEnc.decode('utf-8')
# print(userMessageDec)

# line = "Hello World!"
# print(line)
# index from 0
# []
# H[0]
# e[1]
# ...
# ![11]
#
# l1 = line[2]
# print(l1)
# print(len(line))
# #last element
# print(len(line)-1)
# print(line[-1]) # to get last element in the string

# line[start:stop:step]
# print(line[0:5], line[:5])
# print(line[5:], line[5:11]) # 11 not included

# print(line[::2], line[::1])
# line1 = "Hello World!"
# #id - unique id in memory
# print(id(line), id(line1))

#reversed line
# print(line[::-1])
# print(line[-2:-8:-1])
# print(line[-2:5:-1])
# print(line[-10:5:1]) # converted to [2:5:1]
# print(line[5:-2:-1]) # [5:8:-1] # step -1 start should be > stop
# print(line[5:2:-1])

# multiple of string
# line2 = line*2
# print(line2)

# Methods
#1 registr:
# print("hello".capitalize()) # from capital letter
# print("hello".title())
# print("hello".lower()) # lower letters
# print("hello".upper()) # caps letters
# print("Straße".casefold()) # for other languages to decrease register
#trim
# print("    hello World    ".strip( )) # removes spaces in start or end of the line
# print("    hello World  !  ".strip("!")) # removes symbols
# print("    hello World  #@! ".strip("#@!"))
# print("    hello World  #@! ".lstrip("#@!")) # left
# print("    hello World  #@! ".rstrip("#@!")) # right


# print( "hello World.txt".removesuffix(".txt"))
# print("+380661844701".removeprefix("+380"))

# print("banana".find("na")) #find substring -> index(start)
# print("banana".rfind("na")) #find substring -> index(start)
# print("banana".index("nas")) #find substring -> if not found error returns

# print("banana".count("na")) #count substrings
# print("banana".startswith("na")) # True / False
# print("banana".endswith("na")) #True / False

# transf
# print("I like Java".replace("Java", "Python")) #replaces

# split
# print("Ilike Java".split()) # divides string to list by spaces
# print("I.like.Java".rsplit('.', 1))
# print("I.like.Java".split('.', 1))
# print("I like Java".split())

# print("I\nlike\nJava".splitlines())

#join
# print(" ".join(['I', 'like', 'Java'])) # send list to string
#just
# print("hi".center(30, '-'))
# print("hi".ljust(30, '-'))
# print("hi".rjust(30, '-'))
# print("7".zfill(3))

#format
# name = "Alex"
# age =10
# print(f"{name} hi!")
#
# print("{0} hi!".format(name)) # take 0 element in name
# print("{name} hi! Age = {age}".format(name=name, age=age))
#
# price = 34
# print(" Price = {0:.2f}".format(price))

#bool  prefix is
# print("123abc".isalnum()) #alph + num
# print("123abc  ".isalnum())

