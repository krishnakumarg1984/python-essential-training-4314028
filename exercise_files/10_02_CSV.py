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

import csv

# ## CSV

# ### Reading

with open("10_02_us.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

with open("10_02_us.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader)
    next(reader)
    for row in reader:
        print(row)

with open("10_02_us.csv", "r") as f:
    reader = list(csv.reader(f, delimiter="\t"))
    for row in reader[1:]:
        print(row)

with open("10_02_us.csv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        print(row)

# ### Filtering data

with open("10_02_us.csv", "r") as f:
    data = list(csv.DictReader(f, delimiter="\t"))

primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        primes.append(number)

data = [
    row
    for row in data
    if int(row["postal code"]) in primes and row["state code"] == "MA"
]
len(data)

# ### Writing

with open("10_02_ma_prime.csv", "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row["place name"], row["county"]])


