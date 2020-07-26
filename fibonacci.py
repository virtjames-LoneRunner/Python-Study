import time

n1, n2 = 0, 1

for i in range(0, 99999999999999999):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    time.sleep(0.5)
 