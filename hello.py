import time

start = int(round(time.time() * 1000))

arr = []
for i in range(100000000):
  arr.append(i)

print('Time spent: ', int(round(time.time() * 1000)) - start)