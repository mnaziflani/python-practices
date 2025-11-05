"""
Logical operators are used to combine conditional statements.

Python has three logical operators:

and
or
not
Let's see how the and operator works:

The and operator returns True if both statements are true.

# Create two boolean variables
x = True
y = True

# Check if both x and y are True
result = x and y
After executing the above code, result contains:

True
If one of the values is False, the result will be False:

# Create two boolean variables
x = True
y = False

# Check if both x and y are True
result = x and y
This gives us:

False
"""

# Complete the code to determine if a person is eligible to drive based on their age and license status.

# A person is eligible to drive when:
    # They are at least 18 years old AND
    # They have a valid driving license
# Fill in the blanks with the correct values:
    # Fill in the age variable with 20
    # Fill in the has_license variable with True
    # Fill in the minimum age requirement in the comparison

age = 20
has_license = True

result = age >= 18 and has_license

# Don't change the line below
print("Eligible to drive:", result)

"""
Logical operators have a special table called "Truth table" that shows what the combination of logical operators returns.

Truth table for the and operator:

a	     b	   a and b
False	False	False
False	True	False
True	False	False
True	True	True
The only way to get a True for the and operator is if both a and b are True

Truth table for the or operator:

a	      b  	a or b
False	False	False
False	True	True
True	False	True
True	True	True
In this case, to get a True result, either a or b should be True.

Truth table for the not operator:

a	    not a
False	True
True	False
Here the value of a is reversed. If a is False then not a is True
"""

# Replace the values of variables b1 and b2 with numbers so that b3 evaluates to True.
# b3 will be True when the multiplication of b1 and b2 is greater than their addition.

# Replace the values with numbers
b1 = 10
b2 = 20

# This line checks if b1 * b2 is greater than b1 + b2
b3 = (b1 * b2) > (b1 + b2)

# Don't change the line below
print(f"b3 = {b3}")
b4 = not b3
print(f"b4 = {b4}")

