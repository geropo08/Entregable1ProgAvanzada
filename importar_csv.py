import csv
import random
from typing import List, Tuple, Callable

#Decorador que cobre la funcion principal, que muestra el numero de pregunta y los puntos que tenes luego de responder
def decorador(func: Callable) -> Callable:
    def wrapper(*args,**kwargs):
        print(f"Pregunta: {args[1]+1}")
        res= func(*args, **kwargs)
        if(res[1]==5):
            print(f"El juego ha terminado, usted consiguio {res[2]} puntos")
        else:
            print(f"Tenes {res[2]} puntos\n")
        return res
    return wrapper

#Funcion que lee el archivo .csv
def leer_csv(ruta_archivo: str) -> List[List[str]]:
    with open(ruta_archivo, mode='r', newline='', encoding='latin-1') as archivo:
        lector = list(csv.reader(archivo))
        #Solo solo agarra las columnas de pregunta, respuesta y categoria
        lector=list(map(lambda x: [x[5], x[6],x[3]], lector))
        return lector

#Generador, que agarra una categoria a traves de un Send y devuelve una respuesta random de la misma
def respuestas_por_categoria(preguntas:List[List[str]]):

    categoria = None
    while True:
        if categoria is None:
            categoria=yield
        else:
            answers=list(filter(lambda x: x[2]==categoria,preguntas))
            
            
            indice=random.sample(range(0, len(answers)), 2)
            
            yield answers[indice[0]][1]
            yield answers[indice[1]][1]
            
            categoria=yield

def recursion_respuestas(respuestas, acc: List[str], cat:List[str], preg:List[str]) -> List[str]:
    if(len(cat)==0):
        return acc
    
    next(respuestas)
    r1=respuestas.send(cat[0])
    r2=next(respuestas)
    
    if(preg[0]==r1 or preg[0]==r2):
        return recursion_respuestas(respuestas,acc,cat,preg)
    else:
        acc.append(r1)
        acc.append(r2)
        cat.pop(0)
        preg.pop(0)
        return recursion_respuestas (respuestas, acc, cat, preg)

    
def preguntas_random(preguntas:List[List[str]]) -> Tuple[List[List[str]], List[str]]:
    numeros=random.sample(range(0, len(preguntas)), 5)
    elementos_seleccionados = [preguntas[i] for i in numeros]
    categorias=[preguntas[i][2] for i in numeros]
    correctas=[preguntas[i][1] for i in numeros]

    respuestas=respuestas_por_categoria(preguntas)
    
    lista_respuestas_rand=recursion_respuestas(respuestas,[],categorias,correctas)
    #numeros2=random.sample(range(0, len(preguntas)), 10)
    #respuestas_random = [preguntas[i][6] for i in numeros2]


    
    return elementos_seleccionados, lista_respuestas_rand

def bind(func, tuple: Tuple[Tuple[List[List[str]], List[str]], int, int]):
    res = func(tuple[0],tuple[1],tuple[2])
    return res

def unit(preguntas: Tuple[List[List[str]]]) -> Tuple[Tuple[List[List[str]]], int, int]:
    return preguntas, 0,0




@decorador

def juego(preguntas:Tuple[List[List[str]], List[str]], contador:int, pts:int) -> str:
    opciones=[preguntas[0][contador][1],preguntas[1][0],preguntas[1][1]]
    random.shuffle(opciones)
    print(preguntas[0][contador][0]+"\n"+"Opciones: a-"+opciones[0]+" b-"+opciones[1]+" c-"+opciones[2])
    respuesta=input("Ingese una opcion: ")
    # Mapa de respuestas a las opciones
    opciones_map = {
        "a": opciones[0],
        "b": opciones[1],
        "c": opciones[2]
    }
    if respuesta in opciones_map and opciones_map[respuesta] == preguntas[0][contador][1]:
        pts += 10
        print("Respuesta Correcta!")
    else:
        print(f"Incorrecto! La respuesta era {preguntas[0][contador][1]}")
    preguntas[1].pop(0)
    preguntas[1].pop(0)
    contador+=1
    return preguntas, contador, pts



def main():
    datos = leer_csv('JEOPARDY_CSV.csv')
    preguntas = preguntas_random(datos)
    bind(juego,bind(juego,bind(juego,bind(juego,bind(juego,unit(preguntas))))))
    

    


if __name__ == "__main__":
    main()
