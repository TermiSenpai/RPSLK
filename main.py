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
        updateTotalKeys()
    updateGoodKeys()
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
            puntuaciones = json.load(readFile)
            # Si el jugador no se encuentra dentro del archivo se crea un espacio para él
            if player not in puntuaciones:
                print(msg["notPlayerExist"])
                puntuaciones[player] = {"games": 0,
                                        "wins": 0, "loses": 0, "draws": 0, "time": elapsedTime,
                                        "totalTime": totalTime, "totalKeys": 0,
                                        "totalGoodKeys": 0}
                print(puntuaciones[player])
            return puntuaciones
    else:
        return {player: {"games": 0, "wins": 0, "loses": 0, "draws": 0, "time": elapsedTime,
                         "totalTime": totalTime, "totalKeys": 0, "totalGoodKeys": 0}}


def updateGameStats(result):
    # se suma el resultado de la partida
    gameStats[player]["games"] += 1
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
    gmActualTime = updateTimeStats()
    # Actualizo el tiempo total del jugador
    gmTotalTime = updateTotalTimeStats()

    # Muestro en pantalla el tiempo
    print(msg["time"])
    print(time.strftime("\t%H:%M:%S", gmActualTime))

    # Muestro en pantalla el tiempo total del jugador

    print(msg["totalTime"])
    print(time.strftime("\t%H:%M:%S", gmTotalTime))

    if SAVE_ON_EXIT:
        saveGame()
    # Espero a que el usuario quiera continuar
    input()
    clearScreen()
    print(msg["exit"])
    input()
    clearScreen()
    exit()


def updateTimeStats():
    # Tomo el tiempo total de la partida
    elapsedTime = (time.time() - startTime)
    # Guardo el valor
    gameStats[player]['time'] = elapsedTime
    # formateo el valor
    return time.gmtime(elapsedTime)


def updateTotalTimeStats():
    # calculo el tiempo que lleva en la partida
    elapsedTime = (time.time() - startTime)
    # Tomo el valor del archivo de guardado y lo guardo
    totalTime = gameStats[player]['totalTime']
    # Sumo el tiempo que había con el nuevo
    totalTime = totalTime + elapsedTime
    # Lo guardo en las estadisticas del jugador
    gameStats[player]['totalTime'] = totalTime
    return time.gmtime(totalTime)


def playerNameInput():
    # Input para que el jugador introduzca su nombre
    playerName = str(input(msg["jugador"]))
    # El nombre se guarda en mayúsculas
    playerName = playerName.upper()
    return playerName


def updateTotalKeys():
    gameStats[player]['totalKeys'] += 1


def updateGoodKeys():
    gameStats[player]['totalGoodKeys'] += 1


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
