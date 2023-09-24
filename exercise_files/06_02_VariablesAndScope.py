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

# ## Function Scope


# +
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)


performOperation(1, 2, operation="sum")
# -


# ### locals()


# +
def performOperation(num1, num2, operation="sum"):
    print(locals())


performOperation(1, 2, operation="multiply")
print(num1)
# -

# ### globals()

globals()

# ### Global and Local scope

# +
message = "Some global data"


def function1(varA, varB):
    print(message)
    print(locals())


def function2(varC, varB):
    print(message)
    print(locals())


function1(1, 2)
function2(3, 4)

# +
message = "Some global data"
varA = 2


def function1(varA, varB):
    message = "Some local data"
    print(varA)
    print(message)
    print(locals())


def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())


function1(1, 2)
function2(3, 4)


# +
def function1(varA, varB):
    message = "Some local data"
    print(varA)

    def inner_function(varA, varB):
        print(f"inner_function local scope: {locals()}")

    inner_function(123, 456)


function1(1, 2)


# +
def function1(varA, varB):
    message = "Some local data"
    print(varA)

    def inner_function(varA, varB):
        print(f"inner_function local scope: {locals()}")

    print(locals())
    inner_function(123, 456)


function1(1, 2)
# -

