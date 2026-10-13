import random
import art

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1 #setting the cpu score to an number so that the variable is not undefined for the while loop that lets the cpu draw a card
    user_score = -1


    def deal_card():
        """This function is designed to pick a random card from the cards array. Assuming infinite cards and no probability"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        card = random.choice(cards)
        return card

    def calculate_score(hand):
        """This function takes a list of cards as the input and returns  the sum of all the cards in the list as the score.
        Uses the sum() function."""
        score = sum(hand)
        #print(score)
        if (score == 21) and (len(hand) == 2):
            return 0

        if (score > 21) and (11 in hand):
            hand.remove(11)
            hand.append(1)

        return score

    def compare(u_score, c_score):
        """This function compares the user and computer scores. The if, elif, else statements evaluate from top down in order. """
        if u_score == c_score:
            return "It's a draw!"
        elif c_score == 0:
            return "You lose"
        elif u_score == 0:
            return "You got a blackjack! You win!"
        elif u_score > 21:
            return "You busted. You lose."
        elif c_score > 21:
            return "The computer busted. You win!"
        elif u_score > c_score:
            return "You win!"
        else:
            return "You lose."

    is_game_over = False

    for deal in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_new_card = input("Do you want to draw another card? Comment 'yes' or 'no': ").lower()

            if draw_new_card == 'yes':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                #print(f"User cards: {user_cards}, current score: {user_score}")
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and your final score: {user_score} ")
    print(f"Computer's final hand: {computer_cards} and the computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no' ") == 'yes':
    print("\n" * 20)
    play_game()
