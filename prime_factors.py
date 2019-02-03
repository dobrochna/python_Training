#  Find all prime factors of given number


def find_prime_numbers(number):
    prime_numbers = []
    for numb in range(2, number+1):
        dividers = 1
        for divider in range(2, number+1):
            if numb % divider == 0:
                dividers += 1
        if dividers == 2:
            prime_numbers.append(numb)
    return prime_numbers


def find_prime_factors(number):
    prime_factors = []
    prime_numbers = find_prime_numbers(number)
    for numb in prime_numbers:
        if number % numb == 0:
            prime_factors.append(numb)
    return prime_factors


if __name__ == '__main__':
    number = int(input('Pass the value for wchich factors we are looking for: '))
    prime_factors = find_prime_factors(number)
    if len(prime_factors) == 0:
        print('%i doesnt have any prime factor!' % number)
    else:
        factors_str = ''
        for numb in prime_factors:
            factors_str += str(numb) + ', '
        print('%i prime factors are: %s' % (number, factors_str))
