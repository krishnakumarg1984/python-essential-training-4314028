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

import time

# ## Handling Exceptions

# ### Try / Except


# +
def causeError():
    try:
        return 1 / 0
    except Exception as e:
        return e


causeError()


# +
def causeError():
    try:
        return 1 / 0
    except Exception:
        print("There was some sort of error!")


causeError()
# -


# ### Finally


# +
def causeError():
    try:
        return 1 / 1
    except Exception:
        print("There was some sort of error!")
    finally:
        print("This will always execute!")


causeError()


# +
def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1 / 0
    except Exception:
        print("There was some sort of error!")
    finally:
        print(f"Function took {time.time() - start} seconds to execute")


causeError()
# -


# ### Catching Exceptions by Type


# +
def causeError():
    try:
        return 1 + "a"

    except TypeError:
        print("There was a type error!")
    except ZeroDivisionError:
        print("There was a zero division error!")
    except Exception:
        print("There was some sort of error!")


causeError()
# -


# ### Custom Decorators


# +
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("There was a type error!")
        except ZeroDivisionError:
            print("There was a zero division error!")
        except Exception:
            print("There was some sort of error!")

    return wrapper


@handleException
def causeError():
    return 1 / 0


causeError()
# -


# ### Raising Exceptions


# +
@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)


raiseError(1)
# -

