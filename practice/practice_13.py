# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000'

__author__ = 'banyaofei'

def normalize(name):
    if not isinstance(name,str):
        return name
    else:
        return name[:1].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT', None, '']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    if not isinstance(s, str):
        raise(TypeError)
    else:
        pos = s.find('.')
        if pos == -1:
            high = s
            low_num = 0
        else:
            high = s[:s.find('.')]
            low = s[s.find('.') + 1:]
            low_num = reduce(lambda x, y: x * 10 + y, list(map(int, low))) / 10 ** (len(low))
        high_num = reduce(lambda x,y : x * 10 + y, list(map(int,high)))
        return high_num + low_num

print(str2float('123456'))
print(str2float('0.0'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')