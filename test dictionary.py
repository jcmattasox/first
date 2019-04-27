# test for iterating through dictionary
# JC Matteson





games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict 
       printing  how many games each person has won,
       pluralize 'game' based on number.       
    """
    for i in games_won:     # set loop condition
        if games_won[i] != 1:  # argument for if games is pluralized
            print (i +  ' has won ' + str(games_won[i])+ ' games')
        else:
            print (i +  ' has won ' + str(games_won[i])+ ' game')
        
    
print_game_stats(games_won) # output
