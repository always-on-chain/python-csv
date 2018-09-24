def ask_for_input():
  while True:
    try:
      result = int(input('Please provide number: '))
    except:
      print "That is not a number"
      continue
    else:
      print "Yes, thank you"
      break
    finally:
      print "End of try/except/finally"

ask_for_input()

for i in ['a', 'b', 'c']:
  try:
    print i**2
  except:
    print 'need to make elements numbers'
  finally:
    print 'this is run either way'

try:
  x = 5
  y = 0
  z = x/y
except:
  print 'This is the zero division error'
finally:
  print 'All done'

def ask():
  waiting = True
  while waiting:
    try:
      result = input('Provide us with a value: ')
      result = result ** 2
    except:
      print 'Argument needs to be an integer'
    else:
      waiting = False
  print 'Your number squared is: {}'.format(result)
ask()


