mystring = 'hello'
mylist = []

for letter in mystring:
  mylist.append(letter)
print mylist

#list comprehension
mylist = [letter for letter in mystring]
print mylist

mylist = [x for x in range(0,11) if x % 2 == 0]
print mylist

celcius = [0,10,20,34.5]
fahrenheit = [(((float(9)/5)*temp) + 32) for temp in celcius]
print fahrenheit

#nested for loop
mylist = []
for x in [2,4,6]:
  for y in [1,10,1000]:
   mylist.append(x*y)
print mylist