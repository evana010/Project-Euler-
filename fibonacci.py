#Q. By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
total = 0
array = []
array.append(1)
array.append(2)
for i in range (0, 50):
    if (i >= 2):
        array.append(array[i - 1] + array[i - 2])
    if (array[i] % 2 == 0) and (array[i] <= 4000000):
        total = total + array[i]
print(total)
#Answer = 4613732
