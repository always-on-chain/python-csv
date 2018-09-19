#basic for loop adding numbers in array
mylist = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for num in mylist:
  sum += num
  if num == 10:
    break
  print sum
  
print 'final: {}'.format(sum)