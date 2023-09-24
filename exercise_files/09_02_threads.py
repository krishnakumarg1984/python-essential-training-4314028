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

import threading
import time

# ## Threads


# +
def longSquare(num):
    time.sleep(1)
    return num**2


[longSquare(n) for n in range(0, 5)]


# +
t1 = threading.Thread(target=longSquare, args=(1,))
t2 = threading.Thread(target=longSquare, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()


# +


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2


results = {}
t1 = threading.Thread(target=longSquare, args=(1, results))
t2 = threading.Thread(target=longSquare, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)


# +


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2


results = {}
threads = [
    threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 100)
]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
# -

