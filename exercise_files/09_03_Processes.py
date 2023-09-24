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

# +
import threading
import time

from multiprocess import Process
# -

# ## Processes


# +
def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print("Finished computing!")


results = {}
processes = [Process(target=longSquare, args=(n, results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]
# -


results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)


