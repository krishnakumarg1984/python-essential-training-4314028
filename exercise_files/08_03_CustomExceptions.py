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

# ## Custom Exceptions


# +
class CustomException(Exception):
    pass


def causeError():
    raise CustomException("You called the causeError function!")


causeError()
# -


# ### Adding Attributes


# +
class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(
            f"Status code: {self.statusCode} and message is: {self.message}"
        )


class NotFound(HttpException):
    statusCode = 404
    message = "Resource not found"


class ServerError(HttpException):
    statusCode = 500
    message = "The server messed up!"


def raiseServerError():
    raise ServerError()


raiseServerError()
# -

