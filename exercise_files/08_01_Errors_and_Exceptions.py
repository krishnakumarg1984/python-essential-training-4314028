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

# ## Errors and Exceptions


# +
def causeError():
    return 1 / 0


causeError()


# +
def causeError():
    return 1 / 0


def callCauseError():
    return causeError()


callCauseError()
# -

# ### Try / Except

try:
    1 / 0
except Exception as e:
    print(type(e))


