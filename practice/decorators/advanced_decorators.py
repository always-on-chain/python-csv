import functools

#advanced decorators
def decorator_with_arguments(number):
  def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func(*args):
      print('In the decorator!')
      if number == 56:
        print 'Not running the function!'
      else:
        func(*args)
      print('After the decorator!')
    return function_that_runs_func
  return my_decorator

@decorator_with_arguments(57)
def my_function_too(x, y):
  print(x + y)

my_function_too(57, 67)
