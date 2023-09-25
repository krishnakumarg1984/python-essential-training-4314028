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

from decimal import Decimal, getcontext

# ## Integers

int("100")

int("100", 2)

int(100, 2)

int("1ab", 16)

1.2 - 1.0

# ## Decimals

getcontext()

getcontext().prec = 4

getcontext()

Decimal(1) / Decimal(3)

getcontext().prec = 2

Decimal(1) / Decimal(3)

Decimal(3.14)

Decimal("3.14")

round(1.2 - 1.0, 2)
