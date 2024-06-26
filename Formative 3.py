#!/usr/bin/env python
# coding: utf-8

# In[111]:


'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

# Problem 1

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    followers_from_member = list(social_graph[from_member]["following"])
    followers_to_member = list(social_graph[to_member]["following"])

    if to_member in followers_from_member and from_member in followers_to_member:
        return "friends"
    elif to_member in followers_from_member:
        return "follower"
    elif from_member in followers_to_member:
        return "followed by"
    else:
        return "no relationship"
    
    return relationship


# In[641]:


# Problem 2

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #HORIZONTAL
    for row in board:
        first_element = row[0]
        row_check = True
        
        for element in row:
            if element != first_element or element == '':
                row_check = False
                break
        if row_check:
            return first_element

    #VERTICAL    
    for i in range(len(board)): 
        first_element = board[0][i] # Checks element in the top row
        column_check = True
        
        for j in range(len(board)): # Checks element in that index
            if board[j][i] != first_element or board[j][i] == '':
                column_check = False
                break
        if column_check:
            return first_element

    #DIAGONAL (top right to bottom left)
    first_element = board[0][len(board)-1]
    diagonal_check = True

    for i in range(len(board)):
        if board[i][len(board)-1-i] != first_element or board[i][len(board)-1-i] == '':
            diagonal_check = False
            break
    if diagonal_check:
        return first_element

    #REVERSE DIAGONAL (top left to bottom right)
    first_element = board[0][0]
    reverse_diagonal_check = True

    for i in range(len(board)):
        if board[i][i] != first_element or board[i][i] == '':
            reverse_diagonal_check = False
            break
    if reverse_diagonal_check:
        return first_element

    return "NO WINNER"


# In[769]:


# Problem 3

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, destination), travel in route_map.items(): #route_map.items() returns key-value pairs. Each key is a tuple, value is a distance.
            if start == current_stop:
                total_time = total_time + route_map[(start, destination)]["travel_time_mins"] 
                current_stop = destination
                
                if current_stop == second_stop:
                    return total_time

