# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000#0'

__author__ = 'banyaofei'

class Chain(object):
  def __init__(self,path='GET '):
    self._path = path

  def __getattr__(self,path):
    return Chain('%s/%s' % (self._path,path))

  def __call__(self,user):
    return Chain('%s/%s' % (self._path,user))

  def __str__(self):
    return self._path

  __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('python').repos('Hello'))