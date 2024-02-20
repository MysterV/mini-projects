print('Welcome to this silent auction.')

bids = {}
currency = 'PLN'

def bid():
    bids[input('What\'s your name?\n')] = float(input('How much are you biddin\'?\n'))
    if input('Are there any more bidders? y/n\n') == 'y': bid()

bid()

biggest_bid = 0

for _ in bids:
    if bids[_] > biggest_bid:
        biggest_bid = bids[_]
        the_name = _

print(f'The biggest bidder was {the_name} and they bid\'d {biggest_bid:.2f}{currency}')
