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

# ## Message Exceptions
#
# The SaveMessages class now has limited memory and should only be able to hold a maximum of 10 messages at once.
#
# This challenge has three parts, outlined in comments below.
#
# **\# 1. Finish creating the TooManyMessagesException class**
#
# Fill in the TooManyMessagesException class. Add a custom message!
#
# **\# 2. Raise a TooManyMessagesException exception here**
#
# Make sure that the SaveMessages class doesn't get over-full and raises an Exception if the max_messages limit is reached.
#
# **\# 3. Catch a TooManyMessagesException and print the messages**
#
# Modify this code so that, if an exception is raised when the message is sent, the messages are printed out (emptying the message list) and the message is re-sent. Make sure to print out any remaining messages at the end!
#

# ### Challenge Hints!
#
# **Hint 1:** Remember to make your TooManyMessagesException extend the Exception class


# +
from datetime import datetime


class TooManyMessagesException(Exception):
    pass


# -

# **Hint 2:** You can call the initialization function in the parent class using "super":
#
#

super().__init__("Some string argument, like a message or something")

# **Hint 3:** Use a try / except to send messages and re-send messages on failure:

message = "This is another message"
try:
    sender.send(message)
except:
    listener.printMessages()
    sender.send(message)

# +


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners

    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        pass


# 1. Finish creating the TooManyMessagesException class
class TooManyMessagesException:
    pass


class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        self.max_messages = 10

    def receive(self, message):
        if len(self.messages) >= self.max_messages:
            # Raise a TooManyMessagesException exception here
            pass
        self.messages.append({"message": message, "time": getCurrentTime()})

    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []


# -

listener = SaveMessages()
sender = Messenger([listener])

# 3. Catch a TooManyMessagesException and print the messages
for i in range(0, 20):
    sender.send(f"This is message {i}")


