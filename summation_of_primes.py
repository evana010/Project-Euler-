#Q. Find the sum of all the primes below two million.
counter = 2
prime = 0
notprime = 0
while counter < 2000000:
    for j in range(2, (counter // 2) + 1):
        if (counter % j == 0):
            notprime = counter
    if (counter != notprime):
        prime = prime + counter
    counter += 1
print(prime)
#Answer = 
