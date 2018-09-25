from collections import Counter

l = [1,1,1,1,1,12,2,2,2,2,2,2,3,3,4,4,4,4,5,5,5,5]
print Counter(l)

s = 'asssssvssteerereredkkkk'
print Counter(s)

s = 'How many times does each word show up in this sentence word word show up'
words = s.split()
c = Counter(words)
print Counter(words)
print c.most_common(2)
print c.most_common(4)

s = 'new sentence with new values and if and there what if sentence values if new with if if'
words = s.split()
c = Counter(words)
print sum(c.values())