# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000'

__author__ = 'banyaofei'

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('''
n = %s
f = %f
s1 = %s
s2 = %s
s3 = %s
s4 = %s
    ''' % (n, f, s1, s2, s3, s4))
