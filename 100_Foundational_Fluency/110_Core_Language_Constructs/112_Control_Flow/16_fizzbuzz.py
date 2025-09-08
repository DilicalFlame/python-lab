# a classic programming challenge
# print the numbers from 1 to 100
# for multiples of 3 print "Fizz" instead of the number
# for multiples of 5 print "Buzz" instead of the number
# for multiples of both 3 and 5 print "FizzBuzz" instead of the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
