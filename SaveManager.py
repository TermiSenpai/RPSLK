class SaveManager():
    def autoSave(self, result):
        # leo el archivo de guardado
        puntuacion = self.readSaveFile()
        # comprobamos el resultado de la partida y se guarda en las variables
        if result == 0:
            puntuacion["wins"] += 1
        elif result == 1:
            puntuacion["loses"] += 1
        elif result == 2:
            puntuacion["draws"] += 1
        puntuacion["games"] += 1
        # Escribo la puntuación en el archivo de guardado
        with open("puntuacion.json", "w") as outfile:
            # Escribo el archivo de guardado
            json.dump(puntuacion, outfile)

    def readSaveFile():
        # lectura del archivo de guardado
        with open("puntuacion.json", "r") as readFile:
            puntuacion = json.load(readFile)
            return puntuacion
        
        
        
