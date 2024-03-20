import os
x = 1
for i in range(x,8):
    c = str(i) + "/data.txt"
    os.remove(c)
    print(c)