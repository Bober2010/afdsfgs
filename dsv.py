import shutil
x = 1
for i in range(x,8):
    c = str(i) + "/" + "data.txt"
    shutil.copy("data.txt", c)
    print(c)
    f = open(c,"w")
    f.write(str(i))
    f.close()
    