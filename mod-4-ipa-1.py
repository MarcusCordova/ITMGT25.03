def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
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
    from_member_following = social_graph[from_member]["following"]
    to_member_following = social_graph[to_member]["following"]
    if (to_member in from_member_following) and (from_member in to_member_following):
        return "friends"
    elif to_member in from_member_following:
        return "follower"
    elif from_member in to_member_following:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.
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
    board_size = len(board)
    winner = "NO WINNER"
    for column in range(board_size):
        vertical_symbols = set()
        for row in board:
            vertical_symbols.add(row[column])
        if len(vertical_symbols) == 1 and not ("" in vertical_symbols):
            winner = list(vertical_symbols)[0]
    for row in board:
        horizontal_symbols = set()
        for column in row:
            horizontal_symbols.add(column)
        if len(horizontal_symbols) == 1 and not ("" in horizontal_symbols):
            winner = list(horizontal_symbols)[0]
    diagonal_symbols = set()
    for count in range(board_size):
        diagonal_symbols.add(board[count][count])
    if len(diagonal_symbols) == 1 and not ("" in diagonal_symbols):
        winner = list(diagonal_symbols)[0]
    diagonal_symbols = set()
    for count in range(board_size):
        diagonal_symbols.add(board[board_size - 1 - count][board_size - 1 - count])
    if len(diagonal_symbols) == 1 and not ("" in diagonal_symbols):
        winner = list(diagonal_symbols)[0]
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.
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
    travel_times = [route_map[list(route_map.keys())[0]]["travel_time_mins"]]
    travel_order = [list(route_map.keys())[0][0]]
    next_stop = list(route_map.keys())[0][1]
    route_map_temp = route_map.copy()
    route_map_temp.pop(list(route_map.keys())[0])
    while len(route_map_temp) != 0:
        for key in route_map_temp.copy():
            if key[0] == next_stop:
                travel_times.append(route_map_temp[key]["travel_time_mins"])
                travel_order.append(key[0])
                next_stop = key[1]
                route_map_temp.pop(key)
    first_stop = travel_order.index(first_stop)
    second_stop = travel_order.index(second_stop)
    time = 0
    if second_stop < first_stop:
        for travel_time in travel_times[first_stop:]:
            time = time + travel_time
        for travel_time in travel_times[0:second_stop]:
            time = time + travel_time
    else:
        for travel_time in travel_times[first_stop:second_stop]:
            time = time + travel_time
    return time
