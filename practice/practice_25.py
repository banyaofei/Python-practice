# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000'

__author__ = 'banyaofei'

import re

def is_valid_email(addr):
    return re.match(r'^[a-zA-Z]+[0-9a-zA-Z.]+@[0-9a-zA-Z]+.com$', addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    group = re.match(r'^[<]?([a-zA-Z ]+)[>|@](.+)', addr)
    return group.group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

