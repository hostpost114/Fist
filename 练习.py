from time import sleep
from uiautomator import device as d
import os,csv,time
import subprocess
import multiprocessing
devices_list=['007ff2b2','DU2SSE15C3115777']
def pro(i):
    try:
        for m in range(5):#循环次数
            cmd='adb -s %s shell'%i
            x=os.popen(cmd)
            print(cmd,time.ctime())
            sleep(5)
    except Exception as e:
        print(e)
if __name__=="__main__":
    #几台设备 ，做多进程
    # p1=multiprocessing.Process(target=pro,args=(devices_list[0],))
    # p2=multiprocessing.Process(target=pro,args=(devices_list[1],))
    # p1.start()
    # p2.start()
    p=multiprocessing.Pool(2)
    for line in  devices_list:
        p.apply_async(pro,args=(line,))
    p.close()
    p.join()
    print('test over....')
