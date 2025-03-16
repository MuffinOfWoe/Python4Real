import random
import time

##### OMG !!! I create a deception game
# Deception game similar to One-Night!
# Initial characters can be small subset. 8 types total?
#### Cool future ideas - multiple rounds (Round 1 'mutes' people so they cant talk!")

# Deck is a class, contains all the cards
# SelectedCards is a method, we pick the exact cards we want for the game.
# Cards are a class with their name, lore, action, Team (Good, Bad). Allows duplicates!

# Game starts with deck process. random function for assigning cards to people and 3 to middle.

# Phase 1 of game, we have player 1 look at their card, then click a button to hide it. THen player 2 comes
# preses a key to reveal their card.

# The last player to reveal their card, completes the cycle and starts the game!
# Night event happens. Go in order of players (Can't have viewing your own card as a thing yet!)
# Post Night, all wake up. Discuss! Start 5 minute timer.
# Timer ends (Play a sound? How do we play a sound?) Each player takes turn secretly voting.
# After all Votes, determine who is voted off the island.

# Can the theme be an island? Vote someone off the island! Ship wrecked on an island.
# Villain is an island native who wants you all to leave! I like this concept.

# islandNative If alone, look at 1 card in the middle.
# captain Look at one other players card
# firstMate If there is a captain, you see their card!
# mechanic Swap 2 players cards
# tourist Do Nothing
# cook Swap your card with the middle
# musician



class Cards:
    def __init__(self):
        self.name = "Default Card Name."
    # Later this could contain card size and image info

class Player:
    def __init__(self):
        self.name = "Default Player Name"
        self.wins = 0
        self.currentCharacter = "Default Current Character"

class NativeIslander(Cards):
    name = "NativeIslander"
    team = "Bad"

    @classmethod
    def action(cls):
        print("Conduct mischief! Your goal is to deceive the crew and hide.")

    def lore(cls):
        print("Here is my awesome story...")


class Tourist(Cards):
    name = "Tourist"
    team = "Good"

    @classmethod
    def action(cls):
        print("Being a tourist is boring. Just... chill until morning.")

    def lore(cls):
        print("Tourist Lore goes here...")


class Captain(Cards):
    name = "Captain"
    team = "Good"

    @classmethod
    def action(cls):
        target = int(input("Type in the player # you wish to reveal!"))
        print(f"Player {target} is the {allPlayers[target-1].name} !")
        time.sleep(2)

    def lore(cls):
        print("Captain Lore goes here...")


class Mechanic(Cards):
    name = "Mechanic"
    team = "Good"

    @classmethod
    def action(cls):
        target1 = int(input("Select a player to swap their card with another."))
        target2 = int(input("Select a second player to complete the swap."))
        holdtarget1 = allPlayers[target1-1]
        holdtarget2 = allPlayers[target2-1]
        allPlayers[target1-1] = holdtarget2
        allPlayers[target2-1] = holdtarget1

    def lore(self):
        print("Mechanic Lore goes here...")


def clearscreenandsleep():
    time.sleep(2)
    print("\n" * 100)


def cardOptions():
    for card in deckOptions:
        print(card.name)

while True:
    try:
        numberOfPlayers = int(input("How many players are there? "))
        break
    except ValueError:
        print("That's not a # !!!")


deckOptions = [Mechanic, Captain, NativeIslander, Tourist]

# Future TODO we prompt to keep deck, or create a new one after each round

print("Card Options: ")
cardOptions()

gameDeck = []
numberCardsInMiddle = 1
cardsInMiddle = []
numberOfCards = numberOfPlayers + numberCardsInMiddle

#Our assertion is broken =( Figure this out later....
while numberOfCards > len(gameDeck):
    try:
        currentCardChoiceString = input("Type the name of a card to add to the deck ")
        for card in deckOptions:
            i = 0
            if currentCardChoiceString in card.name:
                gameDeck.append(card)
            else:
                i += 1
            if i == len(deckOptions):
                assert (currentCardChoiceString in card.name)
    except AssertionError:
        print("You must enter one of the following card options:")
        cardOptions()

random.shuffle(gameDeck)

allPlayers = []

while numberCardsInMiddle > 0:
    cardsInMiddle.append(gameDeck[-1])
    numberCardsInMiddle =- 1

for card in cardsInMiddle:
     gameDeck.remove(card)

for card in gameDeck:
    allPlayers.append(card)

clearscreenandsleep()
print("Its time to start the game!")
time.sleep(1)
print("All players except player 1, step away and close your eyes!")
clearscreenandsleep()
print(f"Player 1, Wakeup! You are the {allPlayers[0].name}.")
allPlayers[0].action()
clearscreenandsleep()
print(f"Player 2, Wakeup! You are the {allPlayers[1].name}.")
allPlayers[1].action()
clearscreenandsleep()
print(f"Player 3, Wakeup! You are the {allPlayers[2].name}.")
allPlayers[2].action()
clearscreenandsleep()

print(f"{allPlayers[0].name} and {allPlayers[1].name} and {allPlayers[2].name}")

'''TODO 
Isolate original roles... another variable!
Timer and voting phase.
use loop for our action phase dependant on number of players - cards in middle.
assign players to an object to award points.
after round, allow new deck building.


'''

#Perform our Action! Use our class action here...

# Class action - Look at the name of a card first.
# Class action - How do we swap items in lists? We
# Note swapping breaks our above logic for player names... we need a second list LOL


# allPlayers[0].name = "New Name Goes here!!!!"
# print(allPlayers[0].name)
# print(allPlayers[0].wins)
# print(allPlayers[0].currentCharacter)


# Use a switch statement like this to determine the winning team
# match a.team:
#     case "Bad":
#         print("Team is Bad!")
#     case "Good":
#         print("Team is Good!")
#     case "Unique":
#         print("Team is Unique!")