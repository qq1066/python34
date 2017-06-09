# _*_ coding: UTF-8 _*_
# 时间: 2017 - 06 - 09
"""
python 学习手册(第四版）示例内容
"""
#
import platform
print(platform.python_version())
print('python 学习手册(第四版）示例内容')
#
#嵌套代码三层
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print ('low')
        else:
            print(num ** 2)
print('Bye')