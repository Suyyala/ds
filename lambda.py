# lamda function in python

# lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.

# syntax: lambda arguments : expression

# Example: Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# Example: Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Example: Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

# Or, use the same function definition to make both functions, in the same program:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.



# Python map() function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# syntax: map(fun, iter)

# Example:
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# Example:
# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)

print(list(result))

# Example:
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)





