import random

numPlayer = int(input("Input number of players: "))
player = []

for i in range(0, numPlayer):
    playCard = []
    print("\n\n----Player {0} turn----".format(i + 1))
    # init 2 first cards
    cards = 2
    total = 0
    playCard.append(random.randint(1, 11))
    playCard.append(random.randint(1, 11))
    total = playCard[0] + playCard[1]
    print("player {0} has 2 cards: [{1}] [{2}] (total: {3})".format(i+1, playCard[0], playCard[1], total))
    # hit more cards
    for card in range(0, 3):
        action = input("Hit more card? (Y/N): ")
        if action == "Y" or action == "y":
            cards += 1
            playCard.append(random.randint(1, 11))
            total += playCard[cards-1]
            print("New card is [{0}] (total: {1})".format(playCard[cards-1], total))
            if total > 21:
                break
        elif action == "N" or action == "n":
            break
    # result of player
    print("Player {0} end turn with {1} cards: ".format(i+1, cards), end = "")
    print(playCard, end = "")
    if total > 21:
        print(" Total: {0} (Over)\n".format(total))
    else:
        print(" Total: {0}\n".format(total))
    player.append(total)

# Check the winner
winner = 1
winnerScore = player[0]
print("---------------------------")
for p in range(0, numPlayer):
    overStr = ""
    if player[p] > 21:
        overStr = " (Over)"
    print("Player {0} score: {1}{2}".format(p+1, player[p], overStr))
    if winnerScore > player[p] and winnerScore <= 21:
        winner = (p + 1)
print("The winner is player {0} with score {1}".format(winner, winnerScore))