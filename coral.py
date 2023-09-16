import stddraw
import random

n = 50000

x, y = 0, 0
xn,yn = x,y

stddraw.setPenRadius(.0005)
stddraw.setPenColor(stddraw.BLUE)

for i in range(n):
    r = random.randint(0, 101)
    if r <= 15:
        x = (0.31 * xn) + (-0.08 * yn) + 0.22
        y = (0.15 * xn) + (-0.45 * yn) + 0.34

    elif r > 15 and r <= 55:
        x = (0.31 * xn) + (-0.53 * yn) + 0.89
        y = (-0.46 * xn) + (-0.29 * yn) + 1.04

    elif r > 55 and r <= 100:
        x = (0.55 * yn) + 0.01
        y = (0.69 * xn) + (-0.20 * yn) + 0.38
    
    stddraw.point(xn, yn)
    xn, yn = x, y

stddraw.show()