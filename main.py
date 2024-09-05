import funciones
import leer_csv
if __name__ == "__main__":

    datos = leer_csv.leer_csv('JEOPARDY_CSV.csv')
    preguntas = funciones.preguntas_random(datos)
    funciones.bind(funciones.juego,funciones.bind(funciones.juego,funciones.bind(funciones.juego,funciones.bind(funciones.juego,funciones.bind(funciones.juego,funciones.unit(preguntas))))))