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


def allPrimesUpTo(max_num: int):
    primes_list = [2]
    for num in range(3, max_num):
        sqrt_num = int(num**0.5)
        for prime_factor in primes_list.copy():
            if num % prime_factor == 0:
                break  # Not prime
            if prime_factor > sqrt_num:
                primes_list.append(num)  # 'num' is prime!
                break
    return primes_list


print(allPrimesUpTo(100))

print(allPrimesUpTo(1000))
