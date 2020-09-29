def add_score(server_current_score, receiver_current_score, point_winner):
    # point_winner = 0 --> server wins the point
    # point_winner = 1 --> receiver wins the point
    if point_winner == 1:
        if receiver_current_score == 0:
            receiver_current_score = receiver_current_score + 15
        elif receiver_current_score == 15:
            receiver_current_score = receiver_current_score + 15
        elif receiver_current_score == 30:
            receiver_current_score = receiver_current_score + 10
        elif receiver_current_score == 40:    
            if receiver_current_score == server_current_score:
                receiver_current_score = A
            else:
                receiver_current_score = Win
    else:
         if server_current_score == 0:
            server_current_score = server_current_score + 15
         elif server_current_score == 15:
            server_current_score = server_current_score + 15
         elif server_current_score == 30:
            server_current_score = server_current_score + 10
         elif server_current_score == 40:    
            if server_current_score == receiver_current_score:
                server_current_score = A
            else:
                server_current_score = Win
        
    return server_current_score,receiver_current_score