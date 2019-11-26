class PuntuarAsalto:
    def __init__(self, sheriff):
        self.scores = []
        self.sheriff = sheriff

    def puntuar(self, score):
        self.scores.append(score)

    def execute(self):
        scoreTotal = 0
        scoresLength = self.scores.__len__()
        if(scoresLength > 0):
            for score in self.scores:
                scoreTotal += score

            scoreTotal = scoreTotal / scoresLength

        return scoreTotal
