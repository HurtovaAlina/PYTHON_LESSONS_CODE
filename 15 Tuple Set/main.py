# 1
import re

text = (
    "oцініть найкращі 5 шоу з Київстар — без реклами, без обмежень! "
    "cтав на паузу й продовжуй перегляд із місця, де зупинився. "
    "yкраїнське кіно. mультики українською. більше 1000 переглядів щодня!"
)


def capitalize_sentences(text):
    sentences = re.split("([.!?] *)", text)
    # print(sentences)
    sentences = [s.capitalize() for s in sentences]
    return "".join(sentences)


new_text = capitalize_sentences(text)
print("Text with capitalized sentences:\n", new_text)

numbers_count = len(re.findall(r"\d+", text))

punctuation_count = len(re.findall(r"[.,!?;:—]", text))

exclamation_count = len(re.findall(r"!", text))

print("Count of numbers:", numbers_count)
print("Count of punctuation marks:", punctuation_count)
print("Count of exclamation marks:", exclamation_count)

# 2
list_from_user = list(input("Enter int numbers, using ' ' as separator "))
print(list_from_user)
int_list = (int(i) for i in list_from_user if i != " ")
print(set(int_list))
