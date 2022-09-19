## Add code below with answer clearly stated

def sumofdigits(number):
    """Assumes n > 1.
    returns sum of digits of n's factorial."""
    fact = factorial(number)
    print("Factorial",fact)
    total = 0
    for dig in str(fact):
        total += int(dig)
    return total


def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    print(sumofdigits(100))
