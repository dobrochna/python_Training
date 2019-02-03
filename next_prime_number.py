#  Find next prime numbers


def is_prime_number(value):
    dividers = 1
    for divider in range(2, value+1):
        if value % divider == 0:
            dividers += 1
    if dividers == 2:
        return True
    else:
        return False


def find_next_prime(number):
    while True:
        number += 1
        if is_prime_number(number):
            break
    return number

if __name__ == '__main__':
    start_number = int(input('Pass the number to start: '))
    all_prime_numbers = []
    while True:
        next_prime_number = find_next_prime(start_number)
        all_prime_numbers.append(next_prime_number)
        print('Next prime number after %i is: %i' % (start_number, next_prime_number))
        decision = input('Do you want next prime number? Pass y or n!')
        if decision == 'y':
            start_number = next_prime_number
        else:
            break
    print('Ok, so all prime numbers we printed: %s' % str(all_prime_numbers))
