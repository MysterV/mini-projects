import random

print('''
=== Blackjack ===
- special cards (except ace) count as 10
- ace counts as 11 if your total score is <= 21 and becomes 1 if you go over, you are saved
- both you and dealer draw 2 cards, one of which is visible to both of you
- if dealer is under 17 points, he draws a third card

- you can continually draw another card as long as you are not over 21 points or pass to finish the round

you win if
- dealer goes over 21
- you are both under 21 and you have more points than dealer

you lose if
- you go over 21
- you are both under 21 and you have less points than dealer

you draw if
- both you and dealer go over 21
- you are both under 21 and have equal score
      
======
''')

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player_cards = []
player_score = 0

dealer_cards = []
dealer_score = 0


def dealer_draw():
    global dealer_cards, dealer_score
    roll = random.choice(cards)
    dealer_cards.append(roll)
    dealer_score += roll
    if 11 in dealer_cards and dealer_score > 21:
        dealer_score -= 10
    
    
def player_draw():
    global player_cards, player_score
    roll = random.choice(cards)
    player_cards.append(roll)
    player_score += roll
    if 11 in player_cards and player_score > 21:
        player_score -= 10


def blackjack():
    global player_cards, player_score, dealer_cards, dealer_score
    # phase 1: force draw
    for _ in range(2):
        dealer_draw()
        player_draw()
    if dealer_score < 17: dealer_draw()
    
    # phase 1 results
    print(f"\nDealer's first card: {dealer_cards[0]}")
    print(f'Your cards: {player_cards}, your score: {player_score}')
    
    # phase 2: optional draw
    while player_score <= 21:
        action = input('Draw again? y/n: ')
        if action == 'y': 
            player_draw()
            print(f'Your cards: {player_cards}, your score: {player_score}')
        else: break
    
    # phase 3: results
    print(f'\nYour final cards: {player_cards}, your final score: {player_score}')
    print(f"Dealer's final cards: {dealer_cards}, dealer's final score: {dealer_score}\n")

    # busts
    if player_score > 21 and dealer_score > 21: print('You both busted. It is a draw.')
    elif player_score > 21: print('You busted. You lose.')
    elif dealer_score > 21: print('Dealer busted. You win.')
    # score difference
    elif player_score == dealer_score: print('It is a draw.')
    elif player_score < dealer_score: print('Dealer scored higher. You lose.')
    elif player_score > dealer_score: print('You scored higher. You win.')

    # play again?
    if input('Next round? y/n: ') == 'y':
        # clear variables
        player_cards, player_score, dealer_cards, dealer_score = [], 0, [], 0
        blackjack()

blackjack()