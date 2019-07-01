class BowlingGame:
    isLastFrame = False
    isSpare     = False
    lastScore   = 0
    score       = 0

    def get_total_score(self):
        return self.score
    
    def record_shot(self, pins):
        self.score += pins
        if self.isSpare:
            self.score += pins
            self.isSpare =   False
        if self.isLastFrame and self.lastScore + pins   ==  10:
            self.isSpare = True
        else:
            self.lastScore  = pins
        self.isLastFrame = not(self.isLastFrame)
