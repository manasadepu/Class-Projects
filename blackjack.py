'''
First I imported p1_random module. I then initialized my statistics variables.
Then I started my while loop to continuously run the game.
'''
import p1_random as p1

rng = p1.P1Random()

game_continue = True
game_num = 0
games_played = 0
player_win_count = 0
dealer_win_count = 0
tie_count = 0

while game_continue:
    # 1. set up initial message
    game_num += 1

    print("START GAME #", game_num)
    print('')
    player_hand = 0

    # 2. Deal a card to the player
    card = rng.next_int(13) + 1  # 11
    if card == 1:
        print("Your card is a ACE!")
    elif card == 11:
        print('Your card is a JACK!')
        card = 10
    elif card == 12:
        print('Your card is a QUEEN!')
        card = 10
    elif card == 13:
        print('Your card is a KING!')
        card = 10
    else:
        print(f'Your card is a {card}!')

    player_hand += card
    # print hand value information
    print('Your hand is:', player_hand)
    print('')

    # 3. keep asking users to choose menu option
    no_winners = True
    while no_winners:
        # as long as player hand is under 21, program will ask for input unless player holds hand
        while player_hand < 21:
            # print menu
            menu = '1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n'
            print(menu)
            # ask player to enter choice
            player_choice = int(input('Choose an option: '))
            if player_choice == 1:
                # deal a new card to the player
                # add the new card value to the player hand
                card = rng.next_int(13) + 1
                if card == 1:
                    print("Your card is a ACE!")
                elif card == 11:
                    print('Your card is a JACK!')
                    card = 10
                elif card == 12:
                    print('Your card is a QUEEN!')
                    card = 10
                elif card == 13:
                    print('Your card is a KING!')
                    card = 10
                else:
                    print(f'Your card is a {card}!')
                player_hand += card
                print('Your hand is:', player_hand)
                print('')
                '''
                In every if block that checks for win condition, statistics will be updated.
                Then no_winners will be set to False. This will create a new game.
                '''
                # check if player_hand is equal to 21 or greater than 21
                if player_hand == 21:
                    print('BLACKJACK! You win!\n')
                    games_played += 1
                    player_win_count += 1
                    no_winners = False
                    break

                # else if player_hand is greater than 21
                elif player_hand > 21:
                    print('You exceeded 21! You lose.')
                    games_played += 1
                    dealer_win_count += 1
                    no_winners = False
                    break
            elif player_choice == 2:
                # if player holds hand, draw card for dealer_card
                # Add card value to dealer_hand

                dealer_hand = 0
                dealer_card = rng.next_int(11) + 16
                dealer_hand += dealer_card
                print("Dealer's hand:", dealer_hand)
                print('Your hand is:', player_hand)
                print('')
                # If dealer_hand is greater than 21, player wins
                if dealer_hand > 21:
                    print('You win!\n')

                    player_win_count += 1
                    games_played += 1

                    no_winners = False
                    break
                # If dealer_hand is equal to 21, dealer wins
                elif dealer_hand == 21:
                    print('Dealer wins!')
                    dealer_win_count += 1
                    games_played += 1

                    no_winners = False
                    break
                # If dealer hand is less than 21, check to see for tie
                # If not tie check to see if player_hand or dealer_hand is greater
                elif dealer_hand < 21:
                    if dealer_hand == player_hand:
                        print("It's a tie! No one wins!")
                        tie_count += 1
                        games_played += 1

                        no_winners = False
                        break
                    elif dealer_hand > player_hand:
                        print('Dealer wins!')
                        dealer_win_count += 1
                        games_played += 1

                        no_winners = False
                        break
                    else:
                        print('You win!\n')
                        player_win_count += 1
                        games_played += 1

                        no_winners = False
                        break
            elif player_choice == 3:
                # If player asks for statistics, print statistics
                print('Number of Player wins:', player_win_count)
                print('Number of Dealer wins:', dealer_win_count)
                print('Number of tie games:', tie_count)
                print('Total # of games played is:', games_played)
                print(f'Percentage of Player wins: {round(player_win_count / games_played * 100, 2)}%')
            elif player_choice == 4:
                # If player chooses to exit, set both while loops to false and then break from loops.
                game_continue = False
                no_winners = False
                break
            else:
                # If input is not 1,2,3, or 4 print error message for player.
                # Then reprint menu with continue statement.
                print('Invalid input!')
                print('Please enter an integer value between 1 and 4.')
                continue
