"""
When working with logical expressions, sometimes we need to simplify or rearrange them. This is particularly useful when dealing with complex conditions that combine multiple and and or operators.

De Morgan's Laws provide rules for transforming logical expressions. These transformations help make code more readable and easier to understand.

First Law: not (A and B) is the same as (not A) or (not B)

For example:

# Let's check if a number is NOT (between 1 and 10)
number = 15

# These two expressions are equivalent:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number <= 10)

print(result1)  # True
print(result2)  # True
"""

"""
Second Law: not (A or B) is the same as (not A) and (not B)
For example:

# Checking if a person is NOT (a student or employed)
is_student = False
is_employed = False

# These two expressions are equivalent:
result1 = not (is_student or is_employed)
result2 = (not is_student) and (not is_employed)

print(result1)  # True
print(result2)  # True
"""

"""
Complex Example with Both AND and OR: 
Sometimes you need conditions that combine both operators. Here's a practical example:

# Checking if we CAN'T accept a job application
# We reject if: (no experience AND no degree) OR doesn't meet age requirement

has_experience = False
has_degree = False
meets_age = True

# Complex condition using both AND and OR
reject_application = (not has_experience and not has_degree) or not meets_age

print(reject_application)  # True (rejected because no experience AND no degree)

# This can also be written using De Morgan's Laws:
# "NOT accepted" = NOT(experience OR degree) AND meets age
accept_application = (has_experience or has_degree) and meets_age
reject_application2 = not accept_application

print(reject_application2)  # True (same result, different logic)
"""