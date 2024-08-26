import csv
import random
from typing import List, Any, Tuple


def leer_csv(ruta_archivo: str) -> List[List[str]]:
    with open(ruta_archivo, mode='r', newline='', encoding='latin-1') as archivo:
        lector = csv.reader(archivo)
        return list(lector)

def preguntas_random(preguntas:List[List[str]], cantidad:int) -> Tuple[List[List[str]], List[str]]:
    numeros=random.sample(range(0, len(preguntas)), cantidad)
    elementos_seleccionados = [preguntas[i] for i in numeros]
    numeros2=random.sample(range(0, len(preguntas)), cantidad*2)
    respuestas_random = [preguntas[i][6] for i in numeros2]
    
    return elementos_seleccionados, respuestas_random

def bind(func, tuple: Tuple[int, str]):
    res = func(tuple[0])
    return res[0], tuple[1] + res[1]

def juego(res:Tuple[List[List[str]], List[str]], contador:int) -> str:
    opciones=preguntas_random()
    log="Pregunta: "+res[0][contador][5]+"\n"+"Opciones: "



def main():
    datos = leer_csv('JEOPARDY_CSV.csv')
    preguntas = preguntas_random(datos,5)
    print(len(preguntas[0]))
    print(preguntas[0])
    print(len(preguntas[1]))
    print(preguntas[1])


if __name__ == "__main__":
    main()
