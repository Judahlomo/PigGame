import random

def roll():
    minVal = 1
    maxVal = 6
    roll = random.randint(minVal, maxVal)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
    else: 
        print("Invalid, plaese try again.")

maxScore = 50
playerScores = [0 for _ in range(players)]


while max(playerScores) < maxScore:
    for playerIndex in range(players):
        print("\nPlayer ", playerIndex + 1, "begin!\n")
        print("Your Score is: ", playerScores[playerIndex], "\n" )
        currentScore = 0
        while True:
            shouldRoll = input("Would you like to roll (Y or N)?")
            if shouldRoll.lower() != 'y':
                break
                
            value = roll()
            if value == 1:
                print("You rolled a one, you're cooked buddy.")
                currentScore = 0
                break
            else:
                print("Roll: ", value)
                currentScore += value
            print ("Your Score is: ", currentScore)
    
    playerScores[playerIndex] += currentScore
    print("Your Score is: ", playerScores[playerIndex])

    maxScore = max(playerScores)
    winningPlayer = playerScores.index(maxScore)
    print("Player: ", winningPlayer + 1, " is SUPERSONIC LEGEND with a score of " , maxScore, " !")


            

