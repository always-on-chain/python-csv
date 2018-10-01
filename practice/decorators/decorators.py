import functools

#manually created a decorator
def new_decorator(original_func):
  def wrap_func():
    print 'Some extra code, before the orignal function'
    original_func()
    print 'Some extra code, after the original function'
  
  return wrap_func

def func_needs_decorator():
  print 'I want to be decorated!!'

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

#actual decorator
@new_decorator
def func_needs_decorator():
  print 'I want to be decorated!!'

func_needs_decorator()

#new examples
def my_decorator(func):
  @functools.wraps(func)
  def function_that_runs_func():
    print 'In the decorator func'
    func()
    print 'After the decorator!'
  return function_that_runs_func
  
@my_decorator
def my_function():
  print "I'm the function!"

my_function()
