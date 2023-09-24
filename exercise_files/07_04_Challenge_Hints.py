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

# ## Extending the Messenger
#
# Create a class "SaveMessages" that extends the Messenger class that does the following things:
#
# - Add any messages it receives to a list, along with the time the message was received
# - Use the provided "getCurrentTime" function so that the received message time is a string
# - Contains a method called "printMessages" that prints all collected messages when it's called.
#
# You might also consider clearing the message list when "printMessages" is called.

# **Hint 1:** Make sure to override the "receive" method in your SaveMessages class, in addition to adding the "printMessages" method. You'll want something like this:


# +
from datetime import datetime


class SaveMessages:
    def receive(self, message):
        # Save the message here!
        pass

    def printMessages(self):
        # print your messages here!
        pass


# -

# **Hint 2:** Consider using an array of dictionaries to hold the message data

# +
message = "Hello, there! This is the first message"

messages = []
messages.append({"message": message, "time": getCurrentTime()})

for m in messages:
    print(f'Message: "{m["message"]}" Time: {m["time"]}')
# -


# **HINT 3:** Remember, you can add additional attributes to child class by extending the \_\_init\_\_ method:
#


class SomeClass:
    def __init__(self, existingAttribute=[]):
        super().__init__(existingAttribute)
        self.newChildClassAttribute = []


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
        # Must be implemented by extending classes
        pass


class SaveMessages(Messenger):
    # Your code here!
    pass


# +
# Run this cell after you've written your solution
listener = SaveMessages()

sender = Messenger([listener])

sender.send("Hello, there! This is the first message")
# -


# Run this cell after you've written your solution
sender.send("Oh hi! This is the second message!")

# +
# Run this cell after you've written your solution
sender.send("Hola! This is the third and final message!")

listener.printMessages()
