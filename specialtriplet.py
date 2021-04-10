#Q. A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a2 + b2 = c2. If a + b + c = 1000, find the product abc.

for a in range(0, 1000):
    for b in range(0, 1000):
        for c in range(0,1000):
            if a**2 + b**2 == c**2 and a + b + c == 1000 and a < b < c:
                print("{}".format(a*b*c))
                exit()
#Answer = 31875000
