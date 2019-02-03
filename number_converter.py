#  Program to convert binary number to decimal or the other way


def bin_to_dec(bin_number):
    dec_number = 0
    for power, value in enumerate(reversed(list(bin_number))):
        dec_number += (int(value) * 2 ** int(power))
    return dec_number


def dec_to_bin(dec_number):
    power = 0
    bin_number = ''
    dec_number_int = int(dec_number)
    while dec_number_int > 2**power:
        power += 1
    if 2**power == int(dec_number_int):
        bin_number += '1' + '0' * power
    else:
        for num in range(power-1, -1, -1):
            if 2**num <= dec_number_int:
                bin_number += '1'
                dec_number_int -= 2**num
            else:
                bin_number += '0'
    return int(bin_number)


if __name__ == '__main__':
    while True:
        conversion_type = int(input("If you want to convert binary do decimal pass '1' if the other way: decimal to "
                                    "binary, pass '2': "))

        numb_to_convert = input('Pass the number to convert: ')

        if conversion_type == 1:
            result = bin_to_dec(numb_to_convert)
            print('Your number %s converted to decimal is: %i' % (numb_to_convert, result))
        elif conversion_type == 2:
            result = dec_to_bin(numb_to_convert)
            print('Your number %s converted to binary is: %i' % (numb_to_convert, result))
