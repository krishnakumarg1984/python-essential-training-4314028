# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3.10.4 64-bit
#     language: python
#     name: python3
# ---

# ## Faster Prime Finding
#
# Write a function that returns a list of all primes up to a given number.
#
# For each number, in order to determine if it is prime, take the following steps:
# 1. Find the square root of the number
# 2. Find all the primes up to that square root
# 3. Test to see if any of those primes are divisors
#
# If a number has no prime divisors, it is prime!
#

# ### Challenge Hints!

# **Hint 1:** The function should collect a list of prime numbers as goes. This is the list that it adds "new primes" to as well as the list it uses to check for factors.
#

# **Hint 2:** Don't try to test whether or not 2 is prime. You can assume it's prime and just add it to your list to start

# **Hint 3:** Try modifying the previously-written code:

for number in range(2, 100):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f"{number} is prime!")


def allPrimesUpTo(num):
    pass


allPrimesUpTo(100)

allPrimesUpTo(1000)
