file = r"./data02.txt"

with open(file) as data:
    datafile = data.readlines()

def is_safe(seq, safe_range):
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] not in safe_range:
            return False
    return True

safe = 0
increasing = range(1,4)
decreasing = range(-3, 0)

for i in range(len(datafile)):
    seq = [int(num) for num in datafile[i].strip().split()]
    if is_safe(seq,increasing) or is_safe(seq,decreasing):
        safe += 1
print("Total safe sequences:", safe)
