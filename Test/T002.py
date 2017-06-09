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
#赋值语句的形式
spam = 'Spam' #基本形式
spam,ham = 'yum','YUM' #元组赋值运算（位置性）
[spam, ham] = ['yum','YUM'] #列表复制运算（位置性）
a,b,c,d = 'spam' #序列复制运算，通用性
a, *d = 'spam' #扩展的序列解包（Python 3.0)
spam = ham = 'lunch' #多目标赋值运算
spams += 42 #增强赋值运算（相当于 spams = spams + 42)
#序列赋值
nudge = 1
wink =2
A, B = nudge, wink
print(A, B)
[C, D] = [nudge,wink]
print(C, D)




