import re

#finding strings
patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other term'

print re.search('hello', 'hello world')

for pattern in patterns:
  print 'Searching for "%s" in: \n"%s"' % (pattern, text),

  if re.search(pattern, text):
    print '\n'
    print 'Match was found. \n'
  else:
    print '\n'
    print 'No Match was found.\n'

match = re.search(patterns[0],text)
print text[match.start(): match.end()]

#splitting strings
split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
print re.split(split_term, phrase)

#findall
all_matches = re.findall('match', 'Here is one match, here is another match')
print len(all_matches)

#split string based on punctuation
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print re.findall('[^!.? ]+', test_phrase)