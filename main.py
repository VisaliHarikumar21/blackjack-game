# Import necessary modules
import random, art, sys

in_game = True

# Values of the card
cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]

# calculates the score of the list elements
def calculate_score(cards):
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def clear_terminal():
    """
    Clears the terminal screen
    :return: Nothing
    """
    print("\n" * 100)

def select_winner(player_cards, computer_cards, user_score, computer_score):
    print(f"  Your final hand: {player_cards}, final score: {user_score}")

    while computer_score < 17:

        # Draw cards
        random_card = random.choice(cards_deck)
        computer_cards.append(random_card)
        computer_score = calculate_score(computer_cards)

    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Print the winner
    if user_score <= 21 and computer_score <= 21:
        if user_score > computer_score:
            print("You win! :)")
        elif computer_score > user_score:
            print("You are busted! Computer wins")
        else:
            print("It's a draw")
    elif user_score > 21 and computer_score <= 21:
        print('You went over 21. So computer wins!!!')
    else:
        print('You win!!! Computer went over 21 :)')

def play_blackjack():

    # Choose two random cards to begin the game
    player_cards = random.sample(cards_deck, 2)
    computer_cards = random.sample(cards_deck, 2)

    # Initial score of user and computer
    user_current_score = calculate_score(player_cards)
    computer_current_score = calculate_score(computer_cards)
    play_game = input("Do you wanna play blackjack game? Type 'yes' or 'no' or 'exit': ").lower()
    if play_game == 'exit':
        print(f"Quitting...................")
        sys.exit()
    else:
        if play_game == 'yes':
            clear_terminal()
            print(art.logo)
            while user_current_score < 21:
                print(f"    Your cards: {player_cards}, current_score: {user_current_score}")
                print(f"    Computer's first card: {computer_cards[0]}")
                choose_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if choose_another_card == 'y':
                    random_card = random.choice(cards_deck)
                    player_cards.append(random_card)
                    user_current_score = calculate_score(player_cards)
            select_winner(player_cards, computer_cards, user_current_score, computer_current_score)
        elif play_game == 'no':
            clear_terminal()
            select_winner(player_cards, computer_cards, user_current_score, computer_current_score)
        else:
            clear_terminal()
            print(f"Invalid input. Pass a valid input")

while in_game:
    play_blackjack()
