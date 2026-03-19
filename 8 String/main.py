# Завдання 1
# Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат.

text = input("Enter any text ")
count = 0

for i in text:
    if i == "." or i == "?" or i == "!" or i == ";":
        count+=1
print("Number of sentences = ", count)

# Завдання 2
# Користувач вводить з клавіатури рядок. Перевірте чи є введений рядок паліндромом.
# Паліндром — слово або текст, що читається однаково зліва направо і справа наліво. Наприклад:
# Кок;
# Козак з казок;
# Радар;
# А мене нема.

text = input("Enter any text ")

text_without_spaces = text.replace(" ", "").lower()
reversed_text = text_without_spaces[::-1].lower()

if reversed_text == text_without_spaces:
    print("Text is a palindrom")
else:
    print("Text is NOT a palindrom")

# Завдання 3
# Користувач вводить рядок і два символи. Видаліть із рядка всі символи між першим входженням
# першого символу і першим входженням другого символу, включаючи самі символи. Виведіть результат.

text = input("Enter any sentence ").lower()
char_1 = input("Enter char 1 ")
char_2 = input("Enter char 2 ")
count = 0
index_1 = 0
index_2 = 0

for i in range(len(text)):
    if text[i] == char_1 and count ==0: #finds first char
        index_1 = i
        count +=1 # first char was found
    if text[i] == char_2 and i > index_1 and count > 0: #needed if char_1 == char_2
        index_2 = i
        break

slice_to_remove = text[index_1:index_2+1]
print("slice to remove: ",slice_to_remove)
result = text[:index_1] + text[index_2 + 1:]
print("Result: ", result)
