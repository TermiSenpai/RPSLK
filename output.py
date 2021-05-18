from messages import msg
from bestoArt import art

victory = ["RS", "RL", "SP", "SL", "PR", "PK", "KS", "KR", "LK", "LP"]


def Compare(bot, user, result):
    election = {
        "bot": bot,
        "user": user
    }
    text = msg["userSelect"].format(**election)
    # bot y usuario eligen lo mismo
    if bot == user:
        print(art[user])
        print(art[bot])
        print(msg["draw"])
        print(text)
        return 2
    # usuario elige Rock y el bot Scissor
    elif result in victory:
        print(art[user])
        print(art[bot])
        print(msg["win"])
        print(text)
        return 0
    else:
        print(art[user])
        print(art[bot])
        print(msg["lose"])
        print(text)
        return 1
