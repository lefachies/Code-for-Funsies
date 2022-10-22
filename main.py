import random
list_length = int(input("pick a positive non zero integer"))

print("the list length is :::: {}".format(list_length))
list = []
for i in range(1, list_length):
    numDigits = 10**i
    num = random.random()
    print("rand num:", num)
    list.append(int(numDigits * num))

print(list)

