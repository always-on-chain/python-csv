#print words that start with 's'
st = 'Sam Print only the words that start with s in this sentence'

for word in st.split():
  if word[0].lower() == 's':
    print word

#use range() to print all even numbers from 0 to 10.
print list(range(0,11,2))

#use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
mylist = [num for num in range(0,51,3)]
print mylist

#go through the string below and if the length of a word is even print 'even!'
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
  if len(word) % 2 == 0:
    print '{} is even!'.format(word)

#fizzBizz

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print '{} FizzBuzz'.format(num)
  elif num % 3 == 0:
    print '{} Fizz'.format(num)
  elif num % 5 == 0:
    print '{} Buzz'.format(num)
  else:
    print num

#use list comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
mylist = [word[0] for word in st.split()]
print mylist
