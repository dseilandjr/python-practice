def get_fizzbuzz(my_input):
    my_fizzbuzz_result = ''

    if my_input % 3 == 0 and my_input % 5 == 0:
        my_fizzbuzz_result = "Fizzbuzz"
    elif my_input % 3 == 0 and not (my_input % 5 == 0):
        my_fizzbuzz_result = "Fizz"
    elif not (my_input % 3 == 0) and my_input % 5 == 0:
        my_fizzbuzz_result = "Buzz"
    else:
        my_fizzbuzz_result = ''

    print(my_fizzbuzz_result)

get_fizzbuzz(45)
get_fizzbuzz(30)
get_fizzbuzz(12)
get_fizzbuzz(20)
get_fizzbuzz(7)

def calc_exp(num, power = 1):
    return num ** power

print(calc_exp(3))
print(calc_exp(3, 3))

def add(num1, num2):
    return num1 + num2

print(add(1,2))

def add(num1, num2, num3):
    return num1 + num2 + num3

print(add(1,2,3))

