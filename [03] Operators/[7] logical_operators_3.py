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

When to use De Morgan's Laws:

To make negative conditions easier to read
To simplify complex logical expressions
To convert between different representations of the same logic
"""

# Honestly, it depends on your style of writing. Every developer have their own style.

"""
You're helping a pet shop create a system to determine if they can sell a pet to a customer.

Initialize the following variables:
    has_license with the value True
    has_space with the value True
    has_experience with the value False
    
Write logical expressions to determine if:
    can_sell_regular_pet: Customer can buy a regular pet if they have EITHER a license OR experience, AND they must have space
    can_sell_exotic_pet: Customer can buy an exotic pet if they have BOTH a license AND experience, AND they must have space
    cannot_sell_any_pet: The shop CANNOT sell any pet if the customer has NO license AND NO experience, OR they have NO space

Expected Results with the given values:
    can_sell_regular_pet: True (has license and space)
    can_sell_exotic_pet: False (no experience)
    cannot_sell_any_pet: False (has both license and space)
"""

# Initialize variables

# Calculate conditions
can_sell_regular_pet =
can_sell_exotic_pet =
cannot_sell_any_pet =

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)