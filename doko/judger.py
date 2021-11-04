class DokoJudger:
    def judgeTrick(round, gameState):
        numCards = 4
        trick = gameState[:round*numCards]
        if len(trick) != numCards:
            print("Trick != 4")
        highestCard = 0
        for i in range(1,numCards):
            if not trick[highestCard].higher(trick[i]): highestCard = i

        return highestCard, trick


    def judgeGame(player):
        points = 0
        for trick in player.tricks:
            for card in trick:
                if card.number == 'A': points += 11
                if card.number == '10': points += 10
                if card.number == 'K': points += 4
                if card.number == 'Q': points += 3
                if card.number == 'J': points += 2
        return points
