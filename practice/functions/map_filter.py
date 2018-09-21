#map function
def square(num):
  return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
  print(item)

def splicer(mystring):
  if len(mystring)%2 == 0:
    return 'EVEN'
  else:
    return mystring[0]
names = ['Andy', 'Eve', 'Sally']
print list(map(splicer, names))

#filter function
def check_even(num):
  return num % 2 == 0
mynums = [1,2,3,4,5,6]
print list(filter(check_even, mynums))

#lamba expression
square = lambda num: num ** 2
print square(2)

mylist = [5,6,7]
print map(lambda num: num**2, mylist)

mylist = [2,3,4,5,6]
print list(filter(lambda num: num%2==0, mylist))

names = ['Andy', 'Eve', 'Sally']
print list(map(lambda name: name[0], names))