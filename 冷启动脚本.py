#encoding:utf-8
import csv
import os
from time import sleep
class App(object):
    def __init__(self):
        self.content=''
    #启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.huawei.camera/com.huawei.camera'
        self.content=os.popen(cmd)
    #停止App
    def StopApp(self):
        cmd = 'adb shell input keyevent 3'
        # cmd = 'adb shell am force-stop com.android.browser'
        os.popen(cmd)
    def Get_nowtime(self):
        for line in self.content.readlines():
            if 'ThisTime'in line:
                with open('startTime2.csv', 'a+',newline='')as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(line)
                print(line)
            else:
                pass
        # print(line)
class Run(App):
    def testprocess(self):
        self.LaunchApp()
        sleep(2)
        self.StopApp()
        sleep(2)
        self.Get_nowtime()
if __name__ == "__main__":
    count =0
    counter =3
    x=Run()
    while count<counter:
        x.testprocess()
        print('第 %s 次执行'%count)
        x.Get_nowtime()
        count += 1