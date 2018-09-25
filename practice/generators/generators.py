# #storing list in memory
def create_cubes(n):
  result = []
  for x in range(n):
    result.append(x**3)
  return result

print create_cubes(10)

# #generating the list one value at a time, only needs previous value to generate subsequent value
for x in create_cubes(10):
  print(x)

#generator - makes create_cubes func much more memory efficient
def create_cubes(n):
  for x in range(n):
    yield x**3

for x in create_cubes(10):
  print(x)

def gen_fibon(n):
  a = 1
  b = 1
  for i in range(n):
    yield a
    a,b = b,a+b

for num in gen_fibon(10):
  print num

#generators with next function
def simple_gen():
  for x in range(3):
    yield x

for num in simple_gen():
  print num

g = simple_gen()
print next(g)
print next(g)
print next(g)

#iter function: turning something that is not inherently iterable as a generator, into something that can be
s = 'hello'
for letter in s:
  print letter
s_iter = iter(s)
print next(s_iter)
print next(s_iter)