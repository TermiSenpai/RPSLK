'''
piedra papel tijeras lagarto spok

TO DO LIST:
    - Multiusuario => Preguntar nombre
    - Multiplayer
    - Graficos => mejorar graficos en consola con texto
    - Anticheats
    - IA
    - Discord / Telegram / Whatsapp
    - Stats por mail
    - Animaciones
    - Audio
    - tutorial
    - Online

    
    tiempo de ejecucion
    cantidad de teclas (total, buenas)
    salvar stats
    recuperar stats
'''
import time
import json
import os
import sys
import time
import logic
import output
from messages import msg

global totalKeys
global totalGoodKeys
totalKeys = 0
totalGoodKeys = 0

RPS = ["R", "P", "S", "K", "L", "E"]
answer = ["Y", "N"]
FILE = "Saves.json"
totalTime = 0.0


SAVE_ON_EXIT = True
SAVE_EACH_CYCLE = True

# diccionario de archivo de guardado
gameStats = None
metrics = None


def userInput():
    intro = "j"
    while intro not in RPS:
        print(msg["toExit"])
        intro = str(
            input(msg["intro"]))
        intro = intro.upper()
        # totalKeys += 1
    # totalGoodKeys += 1
    return intro


def saveGame():
    # creo un archivo de guardado
    with open(FILE, "w") as outfile:
        json.dump(gameStats, outfile, indent=4)


def readSaveFile():
    # lectura del archivo de guardado
    if os.path.isfile(FILE):
        # Si existe, se lee el archivo
        with open(FILE, "r") as readFile:
            gameStats = json.load(readFile)
            # Si el jugador no se encuentra dentro del archivo se crea un espacio para él
            if player not in gameStats:
                print(msg["notPlayerExist"])
                gameStats[player] = {"games": 0,
                                        "wins": 0, "loses": 0, "draws": 0, }
                metrics[player] = {"Seconds": elapsedTime,
                                        "totalSeconds": totalTime, "totalKeys": 0,
                                        "totalGoodKeys": 0}
                print(gameStats[player])
            return gameStats
    else:
        return {player: {"games": 0, "wins": 0, "loses": 0, "draws": 0, "time": elapsedTime,
                        "totalTime": totalTime, "totalKeys": 0, "totalGoodKeys": 0}}


def updateGameStats(result):
    # se suma el resultado de la partida
    gameStats[player]["games"] += 1
    # gameStats[player]["totalKeys"] = gameStats[player]["totalKeys"] + logic.totalKeys
    # gameStats[player]["totalGoodKeys"] = gameStats[player]["totalGoodKeys"] + totalGoodKeys
    if result == 0:
        # gameStats[["wins"]] += 1
        gameStats[player]['wins'] += 1
    elif result == 1:
        # gameStats[["loses"]] += 1
        gameStats[player]['loses'] += 1
    elif result == 2:
        # gameStats[["draws"]] += 1
        gameStats[player]['draws'] += 1


def clearScreen():
    os.system("cls")


def closeGame():
    clearScreen()
    # Actualizo el tiempo de juego en la partida actual
    gmTime = updateTimeStats()
    # Actualizo el tiempo total del jugador
    updateTotalTimeStats()
    print(msg["time"])
    print(time.strftime("\t%H:%M:%S", gmTime))

    if SAVE_ON_EXIT:
        saveGame()

    """{var1}".format({"var1":"foo"})
    msg["elapsedTime"].format({"elapsedTime": elapsedTime})
    """

    input()
    clearScreen()
    print(msg["exit"])
    input()
    clearScreen()
    exit()


def updateTimeStats():
    elapsedTime = (time.time() - startTime)
    gameStats[player]['time'] = elapsedTime
    return time.gmtime(elapsedTime)


def updateTotalTimeStats():
    elapsedTime = (time.time() - startTime)
    totalTime = gameStats[player]['totalTime']
    totalTime = totalTime + elapsedTime
    gameStats[player]['totalTime'] = totalTime


def playerNameInput():
    playerName = str(input(msg["jugador"]))
    playerName = playerName.upper()
    # totalKeys += 1
    # totalGoodKeys += 1
    return playerName

def main():
    # fileExists()
    while True:
        # Generación del valor para el bot
        botMain = logic.botElection()
        # Introducción del valor del usuario
        myInput = userInput()
        # Creamos un valor para poder comparar
        victoryCompare = logic.makingTheResult(myInput, botMain)
        # comprobamos y aseguramos la elección del usuario
        if myInput == "E":
            closeGame()
        # Mostrar si el usuario gana o pierde
        game = output.Compare(botMain, myInput, victoryCompare)
        # abrimos y escribimos datos en el archivo de guardado
        # SaveManager.SaveManager().autosave(game)
        updateGameStats(game)
        updateTimeStats()
        if SAVE_EACH_CYCLE:
            saveGame()
        # imprimimos los datos en pantalla
        print(json.dumps(gameStats[player], indent=4))
        input(msg["continue"])
        # borramos la pantalla para mayor comodidad del usuario
        clearScreen()


startTime = time.time()
elapsedTime = (time.time() - startTime)


clearScreen()
player = playerNameInput()
gameStats = readSaveFile()

main()
