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

# ## Can You Hear Me Now?
#
# Create a function "getWithRetry" that calls a function until it receives response that is not None, and then returns that response. If it continues to get no response, it should give up after a certain number of tries (to be decided by you)
#
# After filling out the "getWithRetry" function, run all of the cells in this notebook in order to test the following scenarios:
# - All services are up
# - All services are down
# - All services are down and making a request takes 0.1 seconds to execute
#
# What is the ideal number of retries before giving up? How do you know whether the service is down or you're just unlucky?

# **HINT 1:** Your retry function might look nice if it has a "maxRetries" variable in it, indicating the maximum number of retries the function should iterate for

# **HINT 2:** Use a loop to call the function passed in, and then return if you get string value back

import random
import time

# +
servicesAreUp = True


def getData50():
    if servicesAreUp and random.random() < 0.5:
        return "You got the data! That only happens 50% of the time!"


def getData25():
    if servicesAreUp and random.random() < 0.25:
        return "You got the data! That only happens 25% of the time!"


def getData10():
    if servicesAreUp and random.random() < 0.1:
        return "You got the data! That only happens 10% of the time!"


# -

# Your code here!
def getWithRetry(dataFunc):
    pass


# Should return 'You got the data! That only happens 50% of the time!'
getWithRetry(getData50)

# Should return 'You got the data! That only happens 25% of the time!'
getWithRetry(getData25)

# Should return 'You got the data! That only happens 10% of the time!'
getWithRetry(getData10)

servicesAreUp = False

# Returns None
getWithRetry(getData50)

# Returns None
getWithRetry(getData25)

# Returns None
getWithRetry(getData10)


# +
def getData50():
    time.sleep(0.1)
    if servicesAreUp and random.random() < 0.5:
        return "You got the data! That only happens 50% of the time!"


def getData25():
    time.sleep(0.1)
    if servicesAreUp and random.random() < 0.25:
        return "You got the data! That only happens 25% of the time!"


def getData10():
    time.sleep(0.1)
    if servicesAreUp and random.random() < 0.1:
        return "You got the data! That only happens 10% of the time!"


# -

# Returns None
getWithRetry(getData50)
getWithRetry(getData25)
getWithRetry(getData10)


