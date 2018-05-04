# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000'

__author__ = 'banyaofei'

def is_palindrome(n):
    if not isinstance(n,int):
        return False
    else:
        num2str = str(n)
        num_len = len(num2str)
        for i in range(num_len//2):
            if num2str[i] != num2str[-i - 1]:
                return False
        return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')