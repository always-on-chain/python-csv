class Circle():
  #CLASS OBJECT ATTRIBUTE
  pi = 3.14

  def __init__(self,radius=1,):
    self.radius = radius
    self.area = radius * radius * Circle.pi
  
  #METHOD
  def get_circumference(self):
    return self.radius * Circle.pi * 2

my_circle = Circle(30)
print my_circle.get_circumference()
print my_circle.area

class Animal():
  def __init__(self):
    print('Animal created')
  def who_am_i(self):
    print('I am an animal')
  def eat(self):
    print('I am eating')

class Dog(Animal):
  #CLASS OBJECT ATTRIBUTE
  #SAME FOR ANY INSTANCE OF A CLASS
  species = 'mammal'

  def __init__(self,breed,name):
    Animal.__init__(self)
    #INSTANCE ATTRIBUTES
    self.breed = breed
    self.name = name

  #OPERATIONS/ACTIONS ---> METHOD
  def bark(self,number):
    print('WOOF! My name is {} and the number is {}'.format(self.name,number))

dog = Dog('bichon', 'fluffy')
print dog.who_am_i()

#special methods
class Book():
  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  def __str__(self):
    return '{} by {}'.format(self.title, self.author)

  def __len__(self):
    return self.pages

b = Book('Python rocks', 'Wayne', 200)
print b
print len(b)