# Write a function that returns the lesser to two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
  if a % 2 == 0 and b % 2 == 0:
    return min(a, b)
  else:
    return max(a, b)
first_result = lesser_of_two_evens(2, 4)
second_result = lesser_of_two_evens(7, 5)
print first_result
print second_result

#Write a function that takes a two-word string and returns True if both words begin
#with the same letter
def animal_crackers(s):
  first_word = s.split()[0].lower()
  second_word = s.split()[1].lower()
  return first_word[0] == second_word[0]
print animal_crackers('Hello world')

#Given two intergers, return True if the sum of the integers is 20 or if one of the 
#integers is 20. If not, return False
def makes_twenty(a,b):
  return (a + b == 20) or (a == 20) or (b == 20)

# print makes_twenty(5, 20)

#Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
  first = name[0].upper()
  fourth = name[3].upper()
  return first + name[1:3] + fourth + name[4:]
print old_macdonald('macdonald')

#Given a sentence, return a sentence with the words reversed
def master_yoda(text):
  words = text.split()
  reversed = words[::-1]
  return ' '.join(reversed)
print master_yoda('I am home')

#Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
  return (num >= 90 and num <= 110) or (num >= 190 and num <= 210)
print almost_there(211)

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
  for i in range(0, len(nums)-1):
    if nums[i] == 3 and nums[i + 1] == 3:
      return True
  return False
print has_33([1, 3, 4, 3])
print has_33([3, 1, 3, 3])

#Given a string, return a string where for every char in the original there are 
#3 characters
def paper_doll(s):
  extended_string = ''
  for char in s:
    extended_string += char*3
  return extended_string
print paper_doll('hello')

#Given 3 integers between 1 and 11, if their sum is less than or equal to 21,
#return their sum. If their sum exceeds 21 and there's an eleven, reduce the total
#sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(*args):
  total = sum(args)
  if total <= 21:
    return total
  elif 11 in args and total <= 31: 
      return total - 10
  else:
    return 'BUST'
print blackjack(5,6,7)
print blackjack(9,9,9)
print blackjack(9,9,11)
  
#Return the sum of the numbers in the array, except ignore the sections of numbers
#starting with a 6 and extending to the next 9 (every 6 will be followed by at least
#one 9). Return 0 for no numbers.
def summer_69(nums):
  sum = 0
  add = True
  for num in nums:
    if num == 6:
      add = False
    if add:
      sum += num
    if num == 9:
      add = True 
  return sum
print summer_69([1,3,5])
print summer_69([4,5,6,7,8,9])
print summer_69([2,1,6,9,11])

#Write a function that takes in a list of integers and returns True if it contains
#007 in order
def spy_game(nums):
  group = []
  for num in nums:
    if num == 0 or num == 7:
      group.append(str(num))
  res = ''.join(group)
  return res == '007'
print spy_game([1,2,4,0,0,7,5])
print spy_game([1,0,2,4,0,5,7])
print spy_game([1,7,2,0,4,5,0])

#Write a function that asks the user for a list of people they know
def who_do_you_know():
  known_people = raw_input('Enter the people you know, seperated by commas: ')
  list_people = known_people.split(',')
  list_people_nospace = []
  for person in list_people:
    list_people_nospace.append(person.strip())
  
  print list_people_nospace
  return list_people_nospace

#Write a function that asks the user for they know and see if the name is in the list 
#of people they know
def ask_user():
  name = raw_input('Provide a name: ')

  if name in who_do_you_know():
    print 'You know {}'.format(name)
  else:
    print 'You do not know {}'.format(name)

ask_user()
