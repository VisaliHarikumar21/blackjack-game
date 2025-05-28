# Import necessary modules
from art import logo
import sys, random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deal_card = lambda: random.choice(cards_deck)

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif user_score == 0:
        return "Win! Win! Blackjack"
    elif computer_score == 0:
        return "You Lose. Computer has blackjack"
    elif user_score > 21 and computer_score > 21:
        return "You both went over. It's a draw"
    elif computer_score > 21:
        return "You win. Computer went over 21."
    elif user_score > 21:
        return "You went over 21. So computer wins."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You Lose!"

def play_blackjack():
    user_cards = []
    computer_cards = []
    print("\n"* 20)
    is_game_over = False
    print(logo)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_scores(user_cards)
    computer_score = calculate_scores(computer_cards)
    while not is_game_over:
        print(f"    Your cards: {user_cards}, current_score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            hit_or_stand = input("Do you wanna 'hit' or 'stand'?").lower()
            if hit_or_stand == 'hit':
                user_cards.append(deal_card())
                user_score = calculate_scores(user_cards)
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    return

while True:
    play_game = input("Do you wanna play blackjack game? Type 'yes' or 'no' or 'exit': ").lower()
    if play_game == 'yes':
        play_blackjack()
    else:
        sys.exit()
