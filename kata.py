class TennisGame:

    def __init__(self,server_current_score,receiver_current_score):
        self.server_current_score = 0
        self.receiver_current_score = 0

    #def add_score(self,server_current_score,receiver_current_score, point_winner):
    def add_score(self,point_winner):
        # point_winner = 0 --> server wins the point
        # point_winner = 1 --> receiver wins the point
        if point_winner == 1:
            if self.receiver_current_score == 0:
                self.receiver_current_score = self.receiver_current_score + 15
            elif self.receiver_current_score == 15:
                self.receiver_current_score = self.receiver_current_score + 15
            elif self.receiver_current_score == 30:
                self.receiver_current_score = self.receiver_current_score + 10
            elif self.receiver_current_score == 40 and self.server_current_score != "A":
                if self.receiver_current_score == self.server_current_score:
                    self.receiver_current_score = "A"
                else:
                    self.receiver_current_score = "Win"
            elif self.server_current_score == "A":
                self.server_current_score=40
            else:
                self.receiver_current_score="Win"

        else:
            if self.server_current_score == 0:
                self.server_current_score = self.server_current_score + 15
            elif self.server_current_score == 15:
                self.server_current_score = self.server_current_score + 15
            elif self.server_current_score == 30:
                self.server_current_score = self.server_current_score + 10
            elif self.server_current_score == 40 and self.receiver_current_score != "A":    
                if self.server_current_score == self.receiver_current_score:
                    self.server_current_score = "A"
                else:
                    self.server_current_score = "Win"
            elif self.receiver_current_score == "A":
                self.receiver_current_score=40
            else:
                self.server_current_score="Win"
            
            
        return self.server_current_score,self.receiver_current_score