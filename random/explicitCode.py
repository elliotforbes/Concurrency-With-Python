
# Bad Practice
def notExplicit(*args):
  x, y = args
  return x + y

# Good Practice!
def explicit(x, y):
  return x + y

print(notExplicit(2, 3))
print(explicit(3,4))
