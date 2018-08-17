from card_class import Card, Card_Deck, Hand

def score_hand(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card.value in ['Jack', 'Queen', 'King']: 
            score += 10
        elif card.value == 'Ace':
            score += 11
            ace_count += 1
        else:
            score += card.value
    ## Assigns Aces to be worth 1 point instead of 11 until score <= 21
    while ace_count > 0 and score > 21:
        ace_count -= 1
        score -= 10
    return score
                
def blackjack():
    # Function that manages a single round of blackjack
    deck = Card_Deck()
    ## Makes hands of players
    player_hand = Hand()
    comp_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck)
    for i in range(2):
        comp_hand.add_card(deck)
    ## Human decides how many cards to take
    while True:
        print "Your hand is "+ str(player_hand)
        hit_me = raw_input('Do you want another card (y/n)? ')
        if hit_me == 'n': ## Human done taking cards, now computer turn
            break
        elif hit_me != 'y': ## Invalid response
            print
            print "Invalid response, please answer 'y' or 'n'"
            continue
        player_hand.add_card(deck)
        print 
    ## Computer AI (Computer is dealer). Dealer hits when score < 17 
    comp_score = score_hand(comp_hand.cards)
    while comp_score < 17:
        comp_hand.add_card(deck)
        comp_score = score_hand(comp_hand.cards)
    player_score = score_hand(player_hand.cards)
    print
    ## Determine the winner. Dealer wins ties.
    if player_score <=21 and (player_score > comp_score or comp_score > 21):                                               
        print ('You won!')
    elif comp_score <= 21 and (comp_score >= player_score or player_score > 21):
        print ('You lost')
    else:
        print('Double Bust!')
    print('Computer hand was ' + str(comp_hand))
    print
    print 'Your score was ' + str(player_score)
    print "Dealer's score was " + str(comp_score)


def main():
    ## Manages gameplay, allowing player to choose how many rounds to play
    ans = 'y'
    while ans == 'y':
        blackjack()
        print 
        ans = raw_input('Do you want to play again (y/n)? ')
        print 
    raw_input('Press the enter key to exit.')

main()
