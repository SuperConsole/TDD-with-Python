class BowlingGame:
    score=0

    def get_total_score(self):
        return self.score
    
    def record_shot(self, point):
        self.score += point
