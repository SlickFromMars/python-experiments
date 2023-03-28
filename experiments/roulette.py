import os
import random

chance = 6

if random.randint(0, chance) == chance:
    print("DEATH")
    os.remove(__file__)
else:
    print("SAFE")