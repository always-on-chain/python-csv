with open('newfile.txt', 'w') as text:
  text.write('Hello world')
  text.write('\nI am here')

with open('newfile.txt', 'a') as text:
  text.write('\nGoodbye World')

with open('newfile.txt', 'r') as text:
  contents = text.read()
  print contents
