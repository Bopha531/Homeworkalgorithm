EX1:
text = input("Enter text: ")
for char in text:
    print(char)

EX2:
text = input("Enter your text:")
index = 0
for i in range(len(text)):
    print(index)
    index += 1

EX3:
text = input("Enter your text:")
result = ""
for i in range(len(text)):
if text[i].isupper():
        result += text[i]
        print("Yes!")
else:
        print("No!")

EX4:
text = "3 4 5 6"
result = 0
Sum = ""
for i in range(len(text)):
    if text[i] == " ":
        Sum += ""
    else:
        Sum += text[i]
        result += int(text[i])
print(Sum)
print("Total:",result)

EX5:
text = "454639"
result = 0
coundodd = 0
coundeven = 0
lastindex = len(text) -1
Number_revers = ""
for i in range (len(text)):
    Number_revers += text[lastindex -i]
    if i % 2 != 0:
        coundodd += 1
        result += int(text[i])
    else:
        coundeven += 1
print("letter even:", coundeven)
print("letter odd:", coundodd)
print("total:", result)
print("letter revers", Number_revers)

EX6:
Number = int(input(""))
if Number % 2 == 0:
   print("Even!")
else:
   print("Odd!")

EX7:
Found_Num = False
while not Found_Num:
    Number = int(input())
    if Number <= 20 and Number >= 10:
        print("Continue")
    else:
        Found_Num = True
print("Out of range")

EX8:
text = "9394884039"
number_eight = 0
first_index_of_eight = 0
isfound = False
for i in range(len(text)):
    if text[i] == "8":
        number_eight += 1
        if text[i] == "8" and not isfound:
            first_index_of_eight = i
        isfound = True
print(number_eight)
print(first_index_of_eight)

EX9:
text = "3 4 5 6"
no_space = ""
total_x_two = 0
for i in range(len(text)):
    if text[i] != " ":
        no_space += text[i]
        total_x_two += int(text[i]) * 2
        print(total_x_two)
    else:
        no_space += ""
print(no_space)
EX10:
big_number = 0
small_number = 0
for i in range(5):
    number = int(input("Enter number : "))
    if big_number == 0 and small_number == 0:
        big_number = number
        small_number = number
    else:
        if number > big_number:
            big_number = number
        if number < small_number:
            small_number = number
print("Big number : ", big_number)
print("Small number : ", small_number)