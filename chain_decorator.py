import functools

def split_string(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs).split()
  
  return wrapper

def to_upper(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs).upper()
  
  return wrapper

@split_string
@to_upper
def say_hello(name):
  return f"Hello, {name}!"

print(say_hello("Kitty"))
