import shutil
x = 1
for i in range(x,11):
    c = str(i) + "/" + "data.txt"
    shutil.copy("data.txt", c)
    print(c)