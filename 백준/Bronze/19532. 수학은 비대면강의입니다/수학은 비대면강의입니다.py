import sys
a, b, c, d, e, f = map(int, input().split())

if a == 0:
    y = c/b
    x = (f-e*y)/d
    print(int(x), int(y))
    sys.exit()
# if b == 0:
#     x = (c-b*y)/a
#     y = (f-d*x)/e
#     print(x, y)
#     sys.exit()
# if c == 0:


for y in range(-999, 1000):
    x = (c-b*y)/a
    if (d*x+e*y) == f:
        print(int(x), int(y))