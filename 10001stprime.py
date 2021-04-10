#Q. What is the 10001st prime number?

counter = 2
prime = 0
notprime = 0
prime_counter = 0
while prime_counter < 10001:
    for j in range(2, (counter // 2) + 1):
        if (counter % j == 0):
            notprime = counter
    if (counter != notprime):
        prime = counter
        prime_counter += 1
    counter += 1
print(prime)

#Answer = 104743

