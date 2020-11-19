Number = input("Number: ")
number = int(Number)
counter = 0
number2 = number
factor = []
prime = []
notprime = 0

while (number2 > 1):
    counter += 1
    if (number % counter == 0):
        number2 = number / counter
        factor.append(number2)

#check if prime number
for i in range(0, len(factor)):
    if factor[i] > 1:
        a = int(factor[i]) // 2
        for j in range(2, a):
            if (factor[i] % j == 0):
                notprime = factor[i]
    if (factor[i] != notprime):
        prime.append(factor[i])
print(int(prime[0]), "is the largest prime factor.")
    
#for 644 the answer is 23
#for 13195 the answer is 29
#for 600851475143 the answer is 6857



