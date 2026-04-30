import math

for x in range(2, 1_000_000_000):
    y = 1  # 1 is always a divisor (for x > 1)

    # only check up to sqrt(x)
    for j in range(2, int(math.sqrt(x)) + 1):
        if x % j == 0:
            y += j
            if j != x // j:   # avoid adding square root twice
                y += x // j

    if y == x and x != 1:
        print(x, "is a perfect number")
