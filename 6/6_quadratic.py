import time

times, distances = open('6/6.txt')

start = time.time()

def calc(ms, mm):
    return int((ms ** 2 - 4 * mm) ** 0.5 + ms) // 2 * 2 - ms + 1

races = list(zip([int(x) for x in times.split()[1:]], [int(x) for x in distances.split()[1:]]))
ans = 1
for ms, mm in races:
    ans *= calc(ms, mm)
print(ans)

ms, mm = int(times[9:].replace(" ","")), int(distances[9:].replace(" ",""))
print(calc(ms, mm))

print("took %s milliseconds" % ((time.time() - start) * 1000))