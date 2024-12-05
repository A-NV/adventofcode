file = r"./data02.txt"

with open(file) as data:
    datafile = data.readlines()

def is_safe_with_removal(seq, safe_range):
    def is_safe(subseq):
        return all(subseq[i] - subseq[i - 1] in safe_range for i in range(1, len(subseq)))

    if is_safe(seq):
        print(f"Safe without removing any level: {seq}")
        return True

    for i in range(len(seq)):
        modified_seq = seq[:i] + seq[i + 1:]
        if is_safe(modified_seq):
            print(f"Safe by removing level {seq[i]}: {modified_seq}")
            return True

    print(f"Unsafe regardless of which level is removed: {seq}")
    return False

safe = 0
increasing = range(1,4)
decreasing = range(-3, 0)

for i in range(len(datafile)):
    seq = [int(num) for num in datafile[i].strip().split()]
    if is_safe_with_removal(seq,increasing) or is_safe_with_removal(seq,decreasing):
        safe += 1
print("Total safe sequences:", safe)