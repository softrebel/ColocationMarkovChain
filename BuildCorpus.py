import os
from os import listdir
from os.path import isfile, join
mypath="\\Hamshahri\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
a=""
for i in onlyfiles:
    with open(mypath+str(i),'r',encoding="utf-8") as f:
        for item in f:
            with open(mypath+"Total.txt",'a',encoding="utf-8") as x:
                x.write(item)
                x.write(' ')
    print(i)
print("done")