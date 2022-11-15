from math import sin


def numericalIntegration(lower, upper, n):
    integral = 0
    dx = (upper - lower) / n
    x = lower


    for _ in range(1, n):
        x += dx
        integral += abs(sin(x))
    integral *= 2

    integral += abs(sin(lower))
    integral += abs(sin(upper))

    return (dx / 2) * integral


n = [5, 10, 100, 1000, 10000, 100000, 1000000]

for i in n:
    print(numericalIntegration(0, 3.14159, i))
