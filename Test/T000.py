# _*_ coding: UTF-8 _*_
"""
python3.0 scripts test
"""
#
print('python3.0 scripts test')
#
#################################################################################

while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print
        print('bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')

