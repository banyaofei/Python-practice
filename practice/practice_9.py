# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000'

__author__ = 'banyaofei'

def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
