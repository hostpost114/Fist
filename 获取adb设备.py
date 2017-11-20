import os
x=('adb devices')
m=os.popen(x)
# print(m)
pp=[]
for lie in m.readlines():
    if "devices"not in lie:
        l=lie.split('device')[0]
        pp.append(l)
        print(l)
        print("##################")
        print(pp[0])