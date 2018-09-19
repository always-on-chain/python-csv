#enumerate function
word = 'abcde'

for index,letter in enumerate(word):
  print index
  print letter
  print '\n'

#zip function
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
  print item

print list(zip(mylist1,mylist2,mylist3))

#random method
from random import shuffle
from random import randint

mylist = [1,2,3,4,5]
shuffle(mylist)
print mylist

mynum = randint(0, 10)
print mynum

#input
result = input('Enter a num: ')
print 'this is your number: {}'.format(result)


