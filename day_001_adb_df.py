import csv
import time
from multiprocessing import Process
from time import sleep
import os
result = ''
now_time = time.strftime("%Y-%m-%d %H:%M:%S")


def adb_df():
    cmd = ('adb shell df')
    result = os.popen(cmd)
    with open('tese.csv', 'a+', newline='')as csvfile:
        for line in result:
            if '/data' in line and '/data/sec_storage' not in line:
                # print(line)
                data = line.split()
                print(data, now_time)
                write = csv.writer(csvfile)
                write.writerows([[now_time] + data[0:]])  # 中间会有换行操作
                # write.writerows([['haha',2,34]])#写在同一行
                # write.writerows([['haha',234]])#写在同一行
                # write.writerows([['haha',2,34]])#写在同一行
                # write.writerows([['haha',234]])#写在同一行


def system():
    cmd1 = ('adb shell df')
    result1 = os.popen(cmd1)
    with open('tese2.csv', 'a+', newline='')as csvfile1:
        for line1 in result1:
            if '/system' in line1:
                # print(line)
                data2 = line1.split()
                print(data2, now_time)
                write = csv.writer(csvfile1)
                write.writerows([[now_time] + data2[0:]])  # 中间会有换行操作


if __name__ == '__main__':
    for i in range(3):
        adb_df()
        system()
