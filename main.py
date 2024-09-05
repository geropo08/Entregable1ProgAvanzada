from funciones import *
import leer_csv
if __name__ == "__main__":

    datos = leer_csv.leer_csv('JEOPARDY_CSV.csv')
    preguntas = preguntas_random(datos)
    bind(juego,bind(juego,bind(juego,bind(juego,bind(juego,unit(preguntas))))))