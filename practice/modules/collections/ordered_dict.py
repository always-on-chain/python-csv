#retains order in which k,v pairs are stored in dict, unlike reg dict
from collections import OrderedDict

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
  print k,v

