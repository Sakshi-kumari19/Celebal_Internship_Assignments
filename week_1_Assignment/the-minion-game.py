""" the-minion-game: A string game where players earn points by forming substrings starting with vowels or consonants. """

def minion_game(input_string):
    """
    Calculate and print the winner of the Minion Game based on substring rules.
    """
    vowels = 'AEIOU'
    player1_score = 0
    player2_score = 0
    string_length = len(input_string)
    
    
    for index in range(string_length):
        # number of substring starting with vowels
        if input_string[index] in vowels:
            player1_score += string_length - index
          
        # number of substring staring with consonants
        else:
            player2_score += string_length - index

    if player1_score > player2_score:
        print(f"Winner is player1 with Score {player1_score}")
    elif player2_score > player1_score:
        print(f"Winner is player2 with Score {player2_score}")
    else:
        print("Draw")

# Taking user input
string = input("Enter String : ")
minion_game(string)
