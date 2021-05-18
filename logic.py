import random
from messages import msg
import os

ROCK = "R"
PAPER = "P"
SCISSOR = "S"
EXIT = "E"

RPS = ["R", "P", "S", "K", "L", "E"]
bRPS = ["R", "P", "S", "K", "L"]


def botElection():
    bot = random.choice(bRPS)
    return bot


def userInput():
    intro = "j"
    while intro not in RPS:
        print(msg["toExit"])
        intro = str(
            input(msg["intro"]))
        intro = intro.upper()
    return intro


def makingTheResult(user, bot):
    finalResult = str(user + bot)
    return finalResult
