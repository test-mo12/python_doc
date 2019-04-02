def fizz_buzz(number):
    if not number % 5 and not number % 3:
        return "FizzBuzz"
    if not number % 3:
        return "Fizz"
    if not number % 5:
        return "Buzz"
    return number


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
