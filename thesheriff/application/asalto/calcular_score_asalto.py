class CalcularScoreAsalto:

    def __init__(self, asalto):
        self.asalto = asalto

    def execute(self):
        scoreTotal = 0
        scoresLength = self.asalto.scores.__len__()
        if(scoresLength > 0):
            for score in self.asalto.scores:
                scoreTotal += score

            scoreTotal = scoreTotal / scoresLength

        self.asalto.sheriff.actualizarScore(scoreTotal)
        return scoreTotal
