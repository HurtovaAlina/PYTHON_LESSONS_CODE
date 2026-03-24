re_numbers_1 = r"^\d+$"  # "123", "1"
re_numbers_2 = r"\d+"
re_test = r"cat"

# m = re.search(re_test,"a b cat c cat") # перше співпадіння знаходить
# print(bool(m), m)
# print(m.span())
#
# m1 = re.match(re_test, "catapult") # тільки з початку рядка перевіряє чи є збіг (підстрока)
# m2 = re.match(re_test, "a b cat c cat")
# print(bool(m1), bool(m2))
# if m1:
#     print("catapult")
#
# print("catapult".startswith("cat"))

# m= re.fullmatch(re_numbers_2, "123 a") # повне співпадіння
# l= re.fullmatch(re_numbers_2, "123") # adds ^ and $
# print(m, l)
# findall, finditer, sub, subn, split, compile

# print(re.findall(r"\d+", "a1 b22 c333")) # ['1', '22', '333']
#
# print(re.findall(r"(\w+)=(\d+)", "a=1 b=22 c=333")) # key=value [('a', '1'), ('b', '22'), ('c', '333')]

# for m in re.finditer(r"\d+", "a1 b22 c333"):
#     print(m.group(), m.span())# iterator for match objects

# заміна
# text = re.sub(r"\s+", " ", "a   b \n c") # find spaces and replace to 1 space
# print(text)
# text = re.subn(r"\s+", " ", "a   b \n c") # returns qty what was replaced
# print(text)

# print("a b c".split(","))
# ls = re.split(r"[,\s;]+", "a, b;  c d") # need to mke a list
# print(ls)
#
# RE_NUMBERS =  re.compile(r"\d+")
# print(RE_NUMBERS.findall("a1 b22 c333"))
# text = re.sub(r"\d+", "", "a1 b22 c333") # returns qty what was replaced
# print(text)

# атомарне групування, *+ ++ ?+ compile - flags

# перевірка номеру телефону україни (+380)
# +380987654321, 380987654321, 0987654321 valid phone
# +38 (098) 765-43-21, 0 98 765 43 21, 380 98 7654321 valid

# RX_UA_PHONE = re.compile(r"^(380\d{9}|0\d{9})$")
#
# line = "+38 (098) 765-43-21"
# digits_only = re.sub(r"\D", "", line.strip())
# print(digits_only)
# is_correct_phone = RX_UA_PHONE.fullmatch(digits_only)
# if is_correct_phone:
#     print("Yes")
# else:
#     print("No")
# print(RX_UA_PHONE.fullmatch(digits_only))

# RX_UA_PHONE = re.compile(r"^(380\d{9}|0\d{9})$")
# RX_ALLOWED_CHARS = re.compile(r"^[0-9+\s()\-\t]+$")
#
# line = "+38 (098) 765-43-21"
# line = line.strip()
#
# if RX_ALLOWED_CHARS.fullmatch(line):
#     digits_only = re.sub(r"\D", "", line)
#     is_correct_phone = RX_UA_PHONE.fullmatch(digits_only)
#     if is_correct_phone:
#         print("Yes")
#     else:
#         print("No")
# print(RX_UA_PHONE.fullmatch(digits_only))

# Lists
# int, float, string, bool
# строка, список, кортеж, множина - контейнери містять більше одного значення
# список як масив - може зберігати любий тип даних одночасно
# [], list()
# n1 = 0 #const
# n2 = int() #constructor

# ls1 = [] # create list
# ls2 = list() # create list
# print(ls1, ls2)
#
# ls1= [1, 2.5, "ads", True, print, list()] # inner list of function can be, but should use one type
# ls2 = list()
# print(ls1, ls2)

# ls = [5] * 5 # [5, 5, 5, 5, 5]
# print(ls)
#
# ls = list("Hello") # ['H', 'e', 'l', 'l', 'o']
# print(ls)
# print(" ".join(ls)) #H e l l o

# ls = ["Den", "John", "Alice", "Bob"] # тип даних ссилочного типу змінна має посилання на список, адреса його в памʼяті
# # та посилається на 0 елемент
# print(ls[0]) # Den
# print(ls[-1]) # Bob
# print(ls[::2]) # each second ['Den', 'Alice']

ls = ["Den", "John", "Alice", "Bob"]
# unpack to variables:  _ not used
# a, b, *x = ls # a, b, x, _ = ls  in x all remainig elements
# a, b, x, _ = ls
# *a, b, x = ls # last 2 elements were saved in variable
a, *b, x = ls
print(a, b, x)
