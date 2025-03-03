

LOCATIONS = ['Study', 'H1', 'Hall', 'H2', 'Lounge', 
             'H3','','H4','','H5',
             'Library', 'H6', 'Billiard Room', 'H7', 'Dining Room',
             'H8','','H9','','H10',
              'Conservatory', 'H11', 'Ballroom', 'H12','Kitchen']

PLAYER_LOCATIONS = {'Study':"", 'H1':"", 'Hall':"", 'H2':"MS", 'Lounge':"",
                    'H3':"PP", 'H4':"", 'H5':"CM", 
                    'Library':"", 'H6':"", 'Billiard Room':"", 'H7':"",'Dining Room':"",
                    'H8':"MP", 'H9':"", 'H10':"", 
                    'Conservatory':"", 'H11':"MG", 'Ballroom':"", 'H12':"MW",'Kitchen':"",
                    '':''}



def draw_board(players):
    size = 5  # Size of the game board (5x5)
    # Loop through each row and column to draw the board
    location_count = 0
    print("-" * 85)
    for row in range(size):
        str_row = ""
        if row % 2 != 0:
            str_row += "-" * 85 + "\n"
        for col in range(size):
            str_row += "|" + LOCATIONS[row*5 + col].center(15) + "|"
        str_row += "\n"
        for col in range(size):
            str_row += "|" + players[LOCATIONS[row*5 + col]].center(15) + "|"

        if row % 2 != 0:
            str_row += "\n" + "-" * 85 
                
        
        
        print(str_row)  # New line after each row
    print("-" * 85)


#draw_board(PLAYER_LOCATIONS)