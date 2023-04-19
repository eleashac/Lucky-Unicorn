"""
Lucky Unicorn - token generator v1
generates random choice of token in random order
Created by Eleasha Chan
"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t') # can wrap output making it easier to screenshot
