import random
from messages import msg
import os

ROCK = "R"
PAPER = "P"
SCISSOR = "S"
EXIT = "E"


bRPS = ["R", "P", "S", "K", "L"]


def botElection():
    bot = random.choice(bRPS)
    return bot


def makingTheResult(user, bot):
    finalResult = str(user + bot)
    return finalResult
