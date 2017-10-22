#coding =utf-8
from time import sleep
import os

os.system('adb shell am start -W -n com.huawei.camera/com.huawei.camera ')
sleep(3)
devices1 =("DU2SSE15C3115777")
devices2 =('dsfadfaf')
def photo():

    os.system('adb -s "%s"% shell tap 564 1667')
    sleep(3)
if __name__ =='__main__':
    totaltime =10000
    times =1
    while totaltime<totaltime:
        photo('DU2SSE15C3115777')
        print(times)
        times +=1