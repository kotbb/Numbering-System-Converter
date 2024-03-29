"""
Eslam Gabr Abd-El Azim       =>  20230058
Mohamed Ashraf Said Ibrahim  =>  20230320
Mohamed Ahmed Kotb           =>  20230315
"""

# Functions_Used
# converting from decimal to any system
def dec_to_any(num, base):
    num = int(num)
    input_digits = '0123456789ABCDEF'
    res = ''
    while num > 0:
        rem = num % base
        res = input_digits[rem] + res
        num = num // base
    return res


# converting from any system to decimal except 'hexadecimal'
def any_to_dec(num, base):
    num = int(num)
    res = 0
    power = 0
    while num > 0:
        digit = num % 10
        res = res + digit * (base ** power)
        num = num // 10
        power += 1
    return res


# converting from hexa to decimal manual
def hex_to_dec_manual(num):
    res = 0
    hex_digits = '0123456789ABCDEF'
    i = 0
    for digit in reversed(num):
        res += hex_digits.index(digit) * (16 ** i)
        i += 1
    return res


# menu_1
print("** Welcome to Numbering System Converter **")
print("Menu_1")
while True:
    print("A) Insert a new number: ")
    print("B) Exit program")
    choice = input("Please select an option 'A' or 'B':").upper()

    if choice == 'A':
        num_input = input("Please Enter the number: ")
        if not all(char in '0123456789ABCDEF' for char in num_input):  # to check that the number is valid.
            print("error!!...please enter a valid number...")
            continue

    elif choice == 'B':
        print("Program is ended.\n"
              "Thanks for your time")
        break

    else:
        print("Please select a valid choice (A/B).")
        continue

    # menu_2
    print("Menu_2")
    print(
        "** Please select the base you want to convert a number from**\n"
        "A) Decimal\n"
        "B) Binary\n"
        "C) Octal\n"
        "D) Hexadecimal")
    base_from = input("").upper()  # taking the numbering system that the user want to convert from.

    # menu_3
    print("menu_3")
    print(
        "** Please select the base you want to convert a number to **\n"
        "A) Decimal\n"
        "B) Binary\n"
        "C) Octal\n"
        "D) Hexadecimal")
    base_to = input("").upper()  # taking the numbering system that the user want to convert to.

    # to check if user enter the same two numbering systems
    if base_from == base_to:
        print("error!!...the two numbering systems you entered are the same ")
        continue

    # Decimal checking
    if base_from == 'A':
        if not num_input.isdigit():
            print("error!!...please enter a valid decimal number...")
            continue

    # Binary checking
    if base_from == 'B':
        if not all(char.upper() in '01' for char in num_input):  # check if the user enter a number rather than 0 or 1
            print("error!!...please enter a valid binary number...")
            continue

    # Octal checking
    if base_from == 'C':
        if not all(char.upper() in '01234567' for char in num_input):  # check if the user enter a number more than 7
            print("error!!...please enter a valid octal number...")
            continue

    # Hexadecimal checking
    if base_from == 'D':
        if not all(char in '0123456789ABCDEF' for char in num_input):
            print("error!!...please enter a valid hexadecimal number...")
            continue

    # converting from Decimal_to_any system
    elif base_from == 'A':

        # Decimal_to_Binary
        if base_to == 'B':
            print("the number in binary system is", dec_to_any(num_input, 2))
            continue

        # decimal_to_octal
        elif base_to == 'C':
            print("the number in octal system is", dec_to_any(num_input, 8))
            continue

        # decimal_to_Hexadecimal
        elif base_to == 'D':
            print("the number in hexadecimal system is", dec_to_any(num_input, 16))
            continue

    # Converting from_binary_to_any system
    if base_from == 'B':

        # binary_to_decimal
        if base_to == 'A':
            print("the number in decimal system is:", any_to_dec(num_input, 2))
            continue

        # binary_to_octal
        if base_to == 'C':
            bin_to_dec = any_to_dec(num_input, 2)
            print("the number in octal system is:", dec_to_any(bin_to_dec, 8))
            continue

        # binary_to_hexa
        if base_to == 'D':
            bin_to_dec = any_to_dec(num_input, 2)
            print("the number in hexadecimal system is:", dec_to_any(bin_to_dec, 16))
            continue

    # Converting from_octal_to_any system
    if base_from == 'C':

        # octal_to_decimal
        if base_to == 'A':
            print("the number in decimal system is:", any_to_dec(num_input, 8))
            continue

        # octal_to_binary
        if base_to == 'B':
            oct_to_dec = any_to_dec(num_input, 8)
            print("the number in binary system is:", dec_to_any(oct_to_dec, 2))
            continue

        # octal_to_hex
        if base_to == 'D':
            oct_to_dec = any_to_dec(num_input, 8)
            print("the number in hexadecimal system is:", dec_to_any(oct_to_dec, 16))
            continue

    # Converting from_hexa_to_any system
    if base_from == 'D':

        # hexa_to_decimal
        if base_to == 'A':
            print("the number in decimal system is:", hex_to_dec_manual(num_input))
            continue

        # hexa_to_binary
        if base_to == 'B':
            hex_to_dec = hex_to_dec_manual(num_input)
            print("the number in binary system is:", dec_to_any(hex_to_dec, 2))
            continue

        # hexa_to_octal
        if base_to == 'C':
            hex_to_dec = hex_to_dec_manual(num_input)
            print("the number in octal system is:", dec_to_any(hex_to_dec, 8))
            continue
