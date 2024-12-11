import re

file = r"./data03.txt"

with open(file) as data:
  datafile = data.read()

# datafile = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

data = re.findall(r"mul[(]\d+,\d+[)]",datafile)
numbers = []
results = 0

for i in data:
    number = numbers.append([int(s) for s in re.findall(r"\d+",i)])
print(numbers)

for x, y in numbers:
    results += int(x) * int(y)

print(results)