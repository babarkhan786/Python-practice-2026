# google list of logical operators in python
# | Operator | Description                                            | Example            | Result  |
# | -------- | ------------------------------------------------------ | ------------------ | ------- |
# | `and`    | Returns `True` if **both** conditions are `True`       | `5 > 2 and 10 > 3` | `True`  |
# | `or`     | Returns `True` if **at least one** condition is `True` | `5 > 10 or 10 > 3` | `True`  |
# | `not`    | Reverses the Boolean value                             | `not(5 > 2)`       | `False` |

# 1. and Operator
age = 25
salary = 60000

print(age > 18 and salary > 50000)
print(age < 18 and salary > 50000)

# 2. or Operator
marks = 45
attendance = 80

print(marks >= 50 or attendance >= 75)

# 3. not Operator
is_logged_in = False
is_logged_in = True
print(not is_logged_in)

#  Truth table
# and

# A	    B	    A and B
# True	True	True
# True	False	False
# False	True	False
# False	False	False

# or
# A	    B	    A or B
# True	True	True
# True	False	True
# False	True	True
# False	False	False

# not
# A	not A
# True	False
# False	True

# == equal to
# != 
# > greater then
# < less then

# >= greater then or equal to
# <= less then or eual to
# and
# or
# not
# True
# False