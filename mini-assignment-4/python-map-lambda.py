# 1. Using a lambda function take inputs as
# 4 integers and give the output for equation ax^2+bx+c
cal_polynomial = lambda x, a, b, c: print("polynomial expression result :- ", (a * (x * x)) + (b * x) + c)

cal_polynomial(2, 3, 4, 5)


# 2. Using map() function and lambda and count() function
# create a list consisted of the number of occurrence of both letters: A and a.

list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

result = list(map(lambda x: x if (x.count("A") > 0 and x.count("a") > 0) else "", list1))
print("list of items which contains `A` & `a` : -", result)
