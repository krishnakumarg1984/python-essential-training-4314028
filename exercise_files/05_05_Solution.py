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


def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # It's prime!
                primes.append(number)
                break
    return primes


print(allPrimesUpTo(100))

print(allPrimesUpTo(1000))

print(allPrimesUpTo(100000))


