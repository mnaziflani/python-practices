"""
The modulo operator % tells you what's left over after dividing one number by another.

result = dividend % divisor
dividend: The number being divided.
divisor: The number that divides the dividend.
result: The remainder of the division.
For example

result = 10 % 3
Here, 10 is divided by 3. 3 goes into 10 three times, with a remainder of 1. So, result will be 1.

Usually modulo is used for checking if a number is even or odd:

If a number is even, dividing it by 2 will leave a remainder of 0.
If a number is odd, dividing it by 2 will leave a remainder of 1.
"""

# Type your code below
a = 10%3
b = 10.5%0.5

# Don't change the line below
print(f"a = {a}")
print(f"b = {b:.0f}")
