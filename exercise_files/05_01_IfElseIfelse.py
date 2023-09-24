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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## If statements with "FizzBuzz"

# +
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        if n % 3 == 0:
            print("Fizz")
        else:
            if n % 5 == 0:
                print("Buzz")
            else:
                print(n)
# -

# ### Elif statements

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# ### Single Line if statements

n = 5
print("Fizz" if n % 3 == 0 else n)

fizzBuzz = "Fizz" if n % 3 == 0 else n

"Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n

"FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n

[
    "FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n
    for n in range(1, 101)
]


