'''
  This program was brought to by Track 2
  So that you can throw your life savings away
  by gambling.
'''
import random
# Create two cards with random values from 2 to 11
player_card1 = random.randint(2,12)
player_card2 = random.randint(2,12)
player2_card1 = random.randint(2,12)
player2_card2 = random.randint(2,12)
# inform the user of the current state of the cards
print("Player 1's current hand is " + str(player_card1) + " and " + str(player_card2))
print("player 2's curret hand is " + str(player2_card1) + " and " + str(player2_card2))
# Add the values of the cards
sum = player_card1 + player_card2
sum2 = player2_card1 + player2_card2
# check if the sum causes an immediate win or loss
if sum > 21:
    if sum2 > 21:
        print("It's a tie!")
    print("Bust! Player 1 loses.")
elif sum2 > 21:
    print("Bust! Player 2 loses.")
elif sum == 21:
    if sum2 == 21:
        print("Both players got Blackjack!")
    print("Blackjack! Player 1 wins!")
elif sum2 == 21:
    print("Blackjack! Player 2 wins!")
else:
    # use repetition to allow the user to continue to add to their sum
    player1_turn = True
    player2_turn = True
    while sum <= 21 and sum2 <= 21:
        if player1_turn:
            print("Player 1: Hit or stand? ")
            choice1 = input("Your choice? ")
            choice1 = choice1.lower()
            if choice1 == 'hit':
                new_card1 = random.randint(2,12)
                print("Your drew a " + str(new_card1))
                sum = sum + new_card1
                if sum > 21:
                    print("Bust! You lose.")
                    break
                elif sum == 21:
                    print("Blackjack! You win!")
                    break
            else:
                player1_turn = False
        elif player2_turn:
            print("Player 2: Hit or stand? ")
            choice2 = input("Your choice? ")
            choice2 = choice2.lower()
            if choice2 == 'hit':
                new_card2 = random.randint(2,12)
                print("Your drew a " + str(new_card2))
                sum2 = sum2 + new_card2
                if sum2 > 21:
                    print("Bust! You lose.")
                    break
                elif sum == 21:
                    print("Blackjack! You win!")
                    break
            else:
                player2_turn = False
        else:
            if sum2 > sum:
                print("Player 2 Wins!")
                break
            elif sum > sum2:
                print("Player 1 Wins!")
                break
            else:
                print("It's a tie!")
                break
                
