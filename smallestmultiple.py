#Q. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
answer = False
number = 20
while answer == False:
    counter = 0
    for i in range(1, 21):
        if number % i == 0:
            counter += 1
        else:
            number += 20
            break
    if counter == 20:
        print(number)
        answer = True
  #Answer = 232792560
        
