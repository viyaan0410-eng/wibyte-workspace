import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    return ''


type_effect('You are a part of an underground stealing society.')
type_effect('You have just gotten information that a luxurious art auction is going to happen in 3 days ')
type_effect('And a person has offered you 3 million to steal as many artworks as you can.')
Answer = input('Do you accept this offer? (Y/N)')
if Answer = 'Y':
    type_effect('You have just accepted the offer.')
    type_effect('You spent Rest 2 days, collecting information about the Auction. ')
    type_effect('You got to know that its happening at night. There are five paintings that are going up at the auction ')