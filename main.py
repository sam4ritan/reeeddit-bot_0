import sys
import random


in_string = ' '.join(sys.argv[1:])

mocked = ''

# Makes long runs less likely, maximum run is equal to pool size.
max_run = 3
rand_pool = [random.choice([True, False]) for _ in range(max_run)]
for c in in_string:
    if c is not ' ':
        capitalize = random.choice(rand_pool)
        rand_pool.remove(capitalize)
        if capitalize:
            c = c.upper()
            rand_pool.append(False)
        else:
            c = c.lower()
            rand_pool.append(True)
    mocked += c
    
print(mocked)
