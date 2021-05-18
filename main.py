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


answer = ["Y", "N"]
FILE = "puntuaciones.json"

SAVE_ON_EXIT = False
SAVE_EACH_CYCLE = True

# diccionario de archivo de guardado
gameStats = None


def saveGame():
    # creo un archivo de guardado
    with open(FILE, "w") as outfile:
        json.dump(gameStats, outfile, indent=4)


def readSaveFile():
    # lectura del archivo de guardado
    if os.path.isfile(FILE):
        with open(FILE, "r") as readFile:
            puntuaciones = json.load(readFile)
            if player not in puntuaciones:
                print(msg["notPlayerExist"])
                puntuaciones[player] = {"games": 0,
                                        "wins": 0, "loses": 0, "draws": 0}
                print(puntuaciones[player])
            return puntuaciones
    else:
        return {player: {"games": 0, "wins": 0, "loses": 0, "draws": 0}}


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
    
    if SAVE_ON_EXIT:
        saveGame()
    clearScreen()
    elapsedTime = (time.time() - startTime)
    seconds = {"seconds": elapsedTime}
    print(msg["time"].format(**seconds))
    
    
    """{var1}".format({"var1":"foo"})
    msg["elapsedTime"].format({"elapsedTime": elapsedTime})
    """
    
    input()
    clearScreen()
    print(msg["exit"])
    input()
    clearScreen()
    exit()


def main():
    # fileExists()
    while True:
        # Generación del valor para el bot
        botMain = logic.botElection()
        # Introducción del valor del usuario
        myInput = logic.userInput()
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
        if SAVE_EACH_CYCLE:
            saveGame()
        # imprimimos los datos en pantalla
        print(json.dumps(gameStats[player], indent=4))
        input(msg["continue"])
        # borramos la pantalla para mayor comodidad del usuario
        clearScreen()

startTime = time.time()

clearScreen()
player = str(input(msg["jugador"]))
gameStats = readSaveFile()

main()
