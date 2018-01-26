
mypath="\\Hamshahri\\"

d={}
from collections import defaultdict
with open(mypath+"Model.txt",'r',encoding="utf-8") as f:
    for item in f:
        item = item.split("\n")[0]
        item=item.split(':')
        d[item[0]]=item[1]
a=input("لغت را انتخاب کنید:  ")
print('\n')
s =a.strip()+" "
for i in range(0,6):
    try:
        s += d[a].strip()+" "
        a=d[a].strip()
    except:
        break;
print(s)
