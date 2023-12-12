import time
start_time = time.time()
lines = [*map(str.split,open("12/12.txt").read().split("\n"))]

mem = {}
def get_counts(line, goals, count):
    if (line, goals, count) in mem:
        return mem[(line, goals, count)]
    if len(goals) == 0:
        return not "#" in line
    if count > goals[0] or sum(goals) - count + len(goals) - 1 > len(line):
        return 0
    if not line:
        return count == goals[0]

    valid = 0
    if line[0] in "?#":
        valid += get_counts(line[1:], goals, count + 1)
    if line[0] in "?.":
        if count == goals[0]:
            valid += get_counts(line[1:], goals[1:], 0)
        elif count == 0:
            valid += get_counts(line[1:], goals, 0)

    mem[(line, goals, count)] = valid
    return valid

for i in 1,5:
    print(sum([get_counts('?'.join([line[0]]*i), (*map(int,line[1].split(",")),)*i, 0) for line in lines]))

print("took %s seconds" % (time.time() - start_time))