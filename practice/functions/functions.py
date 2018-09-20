#basic string
def say_hello(name='Name'):
  return ('Hello ' + name)
result = say_hello('Wayne')
print(result)

#basic add
def add(x,y):
  return x + y
result = add(20, 40)
print(result)

# Find out if the word 'dog' is in a string
def dog_check(string):
  return 'dog' in string.lower()
res = dog_check('this is a string without Dog')
print res

#piglatin
def pig_latin(word):
  first_letter = word[0]
  if first_letter.lower() in 'aeiou': 
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + first_letter + 'ay'
  
  return pig_word

print pig_latin('apple')
print pig_latin('word')