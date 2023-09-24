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

# ### Bytes

bytes(4)

smileyBytes = bytes("🙄", "utf-8")
smileyBytes

smileyBytes.decode("utf-8")

smileyBytes = bytearray("🙄", "utf-8")

smileyBytes

smileyBytes[3] = int("85", 16)

smileyBytes.decode("utf-8")


