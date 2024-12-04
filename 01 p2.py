from collections import defaultdict

with open("./data01.txt", "r") as data:
    datafile=data.readlines()

d1 = defaultdict(int)
sorted_list1= []
sorted_list2 = []

for i in range(len(datafile)):
    num1, num2 = datafile[i].strip().split()
    num1 = int(num1)
    num2 = int(num2)
    sorted_list1.append(num1) #key
    sorted_list2.append(num2)

similarity_score = 0

for num in sorted_list1:
    count = sorted_list2.count(num)
    similarity_score += num * count

print(similarity_score)

#answer = 17191599







