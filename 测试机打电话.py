#coding=utf-8
import os,time
from time import sleep
import csv
import multiprocessing
import unittest
from uiautomator import device as d
def Dailr():
    for i in  range(1,10,1):
        cond=''
        wait_time=10
        restar_time = 15
        """当前时间戳   now_time=
        
        拨号后间隔时间   wait_time
         
        多次通话间隔时间 restar_time=15   
        
        """
        now_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        try:
            os.popen('adb shell am start -a android.intent.action.CALL -d tel:10010')
            sleep(wait_time)
            if d(resourceId='com.android.dialer:id/holdButton').wait.exists(timeout=5000):
                cond='拨打成功'
                print(now_time,cond,'第 %s 次执行'%i)
            else:
                cond ='未接通'
                print(now_time,cond,'第 %s 次执行'%i)
            d(resourceId='com.android.dialer:id/floating_end_call_action_button').click()
            sleep(restar_time)
        except Exception as e:
            print(e)
        with open('autophone.csv','a+',newline='')as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([now_time,cond])
if __name__=='__main__':
    Dailr()






