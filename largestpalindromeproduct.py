#Q. Find the largest palindrome made from the product of two 3-digit numbers

numbers = []
palindromic = []
#cycles through all three digit numbers, multiplies them then puts them into an array
for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        string_number = str(number)
        numbers.append(string_number)
#find the reverse of all the multiples of three digit numbers
for a in range(0, len(numbers)):
    reverse_number = numbers[a] [::-1]
#compares the reverse with the original number
    if numbers[a] == reverse_number:
        numbers[a] = int(numbers[a])
        palindromic.append(numbers[a])

#sort the numbers in the palindroic array using a bubble sort
for j in range (0, len(palindromic) - 1):
    for i in range (0, len(palindromic) - j - 1):
        if palindromic[i] > palindromic[i + 1]:
            temp = palindromic[i]
            palindromic[i] = palindromic[i + 1]
            palindromic[i + 1] = temp
print(palindromic[len(palindromic) - 1])

#Answer = 906609
