import random
from art import logo  # External ASCII art logo

def deal_card():
    """
    Returns a random card from the standard Blackjack deck.
    11 represents an Ace.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Calculates the total score of a hand.
    Returns 0 if the hand is a Blackjack (2 cards summing to 21).
    Converts Ace (11) to 1 if the score is over 21.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack!
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """
    Compares user and computer scores and returns the game result with emojis.
    """
    if u_score == c_score:
        return '🤝 Draw!'
    elif c_score == 0:
        return '💀 Computer wins with a Blackjack!'
    elif u_score == 0:
        return '🃏 User wins with a Blackjack!'
    elif u_score > 21:
        return '💥 User busts! Computer wins!'
    elif c_score > 21:
        return '💥 Computer busts! User wins!'
    elif u_score > c_score:
        return '🎉 User wins!'
    else:
        return '💻 Computer wins!'

def game():
    """
    Runs a full round of Blackjack between the user and the computer.
    Allows the user to draw cards, and computer draws until score >= 17.
    Ends the game on Blackjack or bust.
    """
    print(logo)

    # Initial hands
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    computer_score = -1
    user_score = -1
    flag = False

    # User's turn
    while not flag:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"🧑 Your cards: {user_cards}, current score: {user_score}")
        print(f"🤖 Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            flag = True
        else:
            d = input('Do you want another card? [y/n] ').lower()
            if d == 'y':
                user_cards.append(deal_card())
            elif d == 'n':
                flag = True

    # Computer draws until it reaches 17 or more
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n🧑 Your final hand: {user_cards}, final score: {user_score}")
    print(f"🤖 Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Loop to keep playing the game
flag2 = False
while not flag2:
    game_start = input('Do you want to start a new game? [y/n] ').lower()
    if game_start == 'y':
        print('\n'* 20) #Screen clear
        game()
    elif game_start == 'n':
        print('Goodbye!')
        flag2 = True
