# Question 1
# Convert a number to positive if
# it's negative in the list. Only pass those that are
# converted from negative to positive to the new list.
from functools import reduce

lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]

result = list(filter(lambda x: x if (x < 0) else x, lst1))
final = list(map(lambda x: -x if (x < 0) else x, result))
print(final)

# Take the first two values, run the function on them.
# Then take the result and the next value and have a multiplication
# between them. etc. When no more values are left, return the last result.

nums = [1, 2, 3, 4, 5, 6]
multiply = reduce(lambda a, b: a * b, nums)
print("final result : -", multiply)

# Using zip and dict functions create a dictionary which has
# its key-value pairs coming from lst1 and lst2.

lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst2 = [198, 166, 237, 125]

dic = dict(zip(lst1, lst2))

print(dic)
