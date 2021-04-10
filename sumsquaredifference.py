#Q. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_of_squares = 0
sum = 0
square_of_sum = 0
for i in range(1, 101):
    square = i * i
    sum_of_squares = sum_of_squares + square

    sum = sum + i
    square_of_sum = sum * sum

answer = square_of_sum - sum_of_squares
print(answer)

#Answer = 25164150
