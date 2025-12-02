def check_even_odd(number):
    # The % (modulo) operator returns the remainder of division.
    # If a number divided by 2 has a remainder of 0, it is even.
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print(check_even_odd(7))  # Output: Odd
