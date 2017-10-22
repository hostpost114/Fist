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
        os.popen(cmd)
    def csv_title(self):#写入标题
        with open('startTime2.csv', 'a+', newline='')as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['名称', '测试时间'])
    def Get_nowtime(self):
        for line in self.content.readlines():#测试时间的记录
            if 'ThisTime'in line:
                with open('startTime2.csv', 'a+',newline='')as csvfile:
                    z=line.split(':')#分割称列表并加入excel
                    writer = csv.writer(csvfile)
                    # writer.writerow(['名称','测试时间'])
                    writer.writerow(z[0:2])
                print(line)
            # else:
            #     print('要找的数据不存在')
class Run(App):
    def testprocess(self):
        self.LaunchApp()
        sleep(4)
        self.StopApp()
        sleep(2)
        self.Get_nowtime()
if __name__ == "__main__":
    count =0
    counter =9
    x=Run()
    x.csv_title()
    while count<counter:
        print('第 %s 次执行' % count)
        x.testprocess()
        # x.Get_nowtime()
        count += 1

