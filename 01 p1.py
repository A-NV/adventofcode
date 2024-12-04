with open("./data01.txt", "r") as data:
    datafile=data.readlines()

sorted_list1= []
sorted_list2 = []

for i in range(len(datafile)):
    num1, num2 = datafile[i].strip().split()
    num1 = int(num1)
    num2 = int(num2)
    sorted_list1.append(num1)
    sorted_list2.append(num2)

sorted_list1.sort()
sorted_list2.sort()

result = 0
assert len(sorted_list2) == len(sorted_list1)
for j in range(len(sorted_list1)):
    diff = sorted_list1[j] - sorted_list2[j]
    result += abs(diff)

print(f"{result}")

#answer = 197020


