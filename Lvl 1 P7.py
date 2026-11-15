import sys
import time


def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    return ''


def discount(amount):
    return amount * 0.10


P = print

type_effect('Welcome To Amazon!')

Choice = (' Food', 'Clothes', 'Electronics')

for kk in range(len(Choice)):
    P(str(kk+1) + '.' + Choice[kk], sep='\t')

Section = input('In which section do you want to buy?\n')




if Section == '1':

    menu = ['Pizza', 'Milkshake', 'Burger', 'Ice-Cream', 'Sandwich']
    price = ['150', '120', '100', '40', '60']

    for kk in range(len(menu)):
        print(str(kk+1) + '. ' + menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('--------------------------------------------\n')

    while not shopping_complete:

        order = int(input('Type 1-5 to process the item, press 6 for checkout.\n'))

        if 1 <= order <= 5:

            print('Purchasing')
            quant = int(input('How many units?\n'))

            if quant <= 0:
                print('Please enter a valid quantity.')

            elif menu[order-1] in shopping_cart:
                type_effect('Repeat Purchase')
                idx = shopping_cart.index(menu[order-1])
                shopping_quant[idx] += quant

            else:
                shopping_cart.append(menu[order-1])
                shopping_quant.append(quant)

        elif order == 6:
            type_effect('Proceed to checkout..')
            shopping_complete = True

        else:
            type_effect('Sorry that was not a valid input.')


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0

    print('Item', 'Quant', 'Unit Price', 'Total', sep='\t\t\t')

    for kk in range(len(shopping_cart)):

        idx = menu.index(shopping_cart[kk])
        unit_price = int(price[idx])

        tot_price = round(unit_price * shopping_quant[kk], 2)
        grand_tot += tot_price

        print(shopping_cart[kk], shopping_quant[kk], unit_price,
              tot_price, sep='\t\t\t')


    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
        print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
        dollar = grand_tot / 100
        print("Your total order is ($)", dollar)
        total = dollar

    elif choice == 2:
        print("Your total order is (INR)", grand_tot)
        total = grand_tot

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)
        total = yen

    else:
        print("Invalid choice!")
        total = None


    print('\n')

    if total is not None:

        d = input('How do you want to pay? (UPI or card)\nSorry cant do Cash because we do not have "cash on delivery."\n')

        if d.lower() == 'card':

            CC = ('Visa (INR)', 'Mastercard (YEN)', 'Amex (DOLLAR)')

            for kk in range(len(CC)):
                print(str(kk+1) + '. ' + CC[kk])

            checkout = int(input('Please choose a card to proceed checkout! '))

            if checkout == 1:

                type_effect('We have 10% discount in INR(₹)')

                if choice == 2:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card')

            elif checkout == 2:

                type_effect('We have 10% discount in Yen(¥)')

                if choice == 3:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card')

            elif checkout == 3:

                type_effect('We have 10% discount in Dollar($)')

                if choice == 1:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card')

            else:
                print('Invalid card choice!')

        elif d.lower() == 'upi':

            print('Please Pay', total)
            print('Dingg come from the machine')

        else:
            print('Invalid payment method!')

        type_effect('Thank you for using Amazon.')
        type_effect('I wish seeing you again.')


    print('--------------------------------------------\n')


# ---------------- CLOTH SECTION ----------------

elif Section == '2':

    menu = ['T-shirt', 'Jeans', 'Kurta', 'Track pant', 'Shirt']
    price = ['300', '420', '301', '720', '610']

    for kk in range(len(menu)):
        print(str(kk+1) + '. ' + menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('--------------------------------------------\n')

    while not shopping_complete:

        order = int(input('Type 1-5 to process the item, press 6 for checkout.\n'))

        if 1 <= order <= 5:

            print('Purchasing')
            quant = int(input('How many units?\n'))

            if quant <= 0:
                print('Please enter a valid quantity.')

            elif menu[order-1] in shopping_cart:
                type_effect('Repeat Purchase')
                idx = shopping_cart.index(menu[order-1])
                shopping_quant[idx] += quant

            else:
                shopping_cart.append(menu[order-1])
                shopping_quant.append(quant)

        elif order == 6:
            type_effect('Proceed to checkout..')
            shopping_complete = True

        else:
            type_effect('Sorry that was not a valid input.')


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0

    print('Item', 'Quant', 'Unit Price', 'Total', sep='\t\t\t')

    for kk in range(len(shopping_cart)):

        idx = menu.index(shopping_cart[kk])
        unit_price = int(price[idx])

        tot_price = round(unit_price * shopping_quant[kk], 2)
        grand_tot += tot_price

        print(shopping_cart[kk], shopping_quant[kk], unit_price,
              tot_price, sep='\t\t\t')


    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
        print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
        dollar = grand_tot / 100
        print("Your total order is ($)", dollar)
        total = dollar

    elif choice == 2:
        print("Your total order is (INR)", grand_tot)
        total = grand_tot

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)
        total = yen

    else:
        print("Invalid choice!")
        total = None


    print('\n')

    if total is not None:

        d = input('How do you want to pay? (UPI or card)\nSorry cant do Cash because we do not have "cash on delivery."\n')

        if d.lower() == 'card':

            CC = ('Visa (INR)', 'Mastercard (YEN)', 'Amex (DOLLAR)')

            for kk in range(len(CC)):
                print(str(kk+1) + '. ' + CC[kk])

            checkout = int(input('Please choose a card to proceed checkout! '))

            if checkout == 1:

                type_effect('We have 10% discount in INR(₹)')

                if choice == 2:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for INR')

            elif checkout == 2:

                type_effect('We have 10% discount in Yen(¥)')

                if choice == 3:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for YEN')

            elif checkout == 3:

                type_effect('We have 10% discount in Dollar($)')

                if choice == 1:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for DOLLAR')

            else:
                print('Invalid card choice!')

        elif d.lower() == 'upi':

            print('Please Pay', total)
            print('Dingg come from the machine')

        else:
            print('Invalid payment method!')

        type_effect('Thank you for using Amazon.')
        type_effect('I wish seeing you again.')


    print('--------------------------------------------\n')


# ---------------- ELECTRONICS SECTION ----------------

elif Section == '3':

    menu = ['Tv', 'Mobile', 'Fridge', 'Ps5', 'X-box']
    price = ['35000', '40020', '30001', '70020', '61210']

    for kk in range(len(menu)):
        print(str(kk+1) + '. ' + menu[kk], price[kk], sep='\t\t')

    shopping_cart = []
    shopping_quant = []

    shopping_complete = False
    print('--------------------------------------------\n')

    while not shopping_complete:

        order = int(input('Type 1-5 to process the item, press 6 for checkout.\n'))

        if 1 <= order <= 5:

            print('Purchasing')
            quant = int(input('How many units?\n'))

            if quant <= 0:
                print('Please enter a valid quantity.')

            elif menu[order-1] in shopping_cart:
                type_effect('Repeat Purchase')
                idx = shopping_cart.index(menu[order-1])
                shopping_quant[idx] += quant

            else:
                shopping_cart.append(menu[order-1])
                shopping_quant.append(quant)

        elif order == 6:
            type_effect('Proceed to checkout..')
            shopping_complete = True

        else:
            type_effect('Sorry that was not a valid input.')


    print('\n')
    print('Your shopping cart')

    grand_tot = 0.0

    print('Item', 'Quant', 'Unit Price', 'Total', sep='\t\t\t')

    for kk in range(len(shopping_cart)):

        idx = menu.index(shopping_cart[kk])
        unit_price = int(price[idx])

        tot_price = round(unit_price * shopping_quant[kk], 2)
        grand_tot += tot_price

        print(shopping_cart[kk], shopping_quant[kk], unit_price,
              tot_price, sep='\t\t\t')


    type_effect('\n')

    Currency = ('Dollars($)', 'INR(₹)', 'Yen(¥)')

    for kk in range(len(Currency)):
        print(str(kk+1) + '. ' + Currency[kk])

    choice = int(input('In which currency do you want to buy?\n'))

    if choice == 1:
        dollar = grand_tot / 100
        print("Your total order is ($)", dollar)
        total = dollar

    elif choice == 2:
        print("Your total order is (INR)", grand_tot)
        total = grand_tot

    elif choice == 3:
        yen = grand_tot / 10
        print("Your total order is (¥)", yen)
        total = yen

    else:
        print("Invalid choice!")
        total = None


    print('\n')

    if total is not None:

        d = input('How do you want to pay? (UPI or card)\nSorry cant do Cash because we do not have "cash on delivery."\n')

        if d.lower() == 'card':

            CC = ('Visa (INR)', 'Mastercard (YEN)', 'Amex (DOLLAR)')

            for kk in range(len(CC)):
                print(str(kk+1) + '. ' + CC[kk])

            checkout = int(input('Please choose a card to proceed checkout! '))

            if checkout == 1:

                type_effect('We have 10% discount in INR(₹)')

                if choice == 2:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for INR')

            elif checkout == 2:

                type_effect('We have 10% discount in Yen(¥)')

                if choice == 3:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for YEN')

            elif checkout == 3:

                type_effect('We have 10% discount in Dollar($)')

                if choice == 1:
                    final_total = total - discount(total)
                    print('Please Pay', round(final_total, 2))
                    print('Dingg come from the machine')
                else:
                    type_effect('Cant use this card, this card is only for DOLLAR')

            else:
                print('Invalid card choice!')

        elif d.lower() == 'upi':

            print('Please Pay', total)
            print('Dingg come from the machine')

        else:
            print('Invalid payment method!')

        type_effect('Thank you for using Amazon.')
        type_effect('I wish seeing you again.')


    print('--------------------------------------------\n')


else:
    print('Sorry, that was not a valid section!')