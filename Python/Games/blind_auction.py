bids = {}
currency = 'PLN'

from clear import clear
def bid():
    clear()
    print('Welcome to this blind auction.')
    bids[input('What\'s your name?\n')] = float(input(f'How much are you biddn\' ({currency})?\n'))
    
    if input('Are there any more bidders? y/n\n') == 'y':
        bid()


def find_highest_bid():
    biggest_bid = 0

    for name in bids:
        if bids[name] > biggest_bid:
            biggest_bid = bids[name]
            the_name = _

    clear()
    print(f'The biggest bidder was {the_name} and they bid\'d {biggest_bid:.2f}{currency}')


bid()
find_highest_bid()