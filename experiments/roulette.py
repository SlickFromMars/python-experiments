import os
import random

chance = 4

if random.randint(0, chance) == chance:
    print("DEATH")
    os.remove(__file__)
else:
    print("SAFE")