import csv
import random
from itertools import islice
from typing import List, Tuple, Callable
from collections import Counter

def leer_csv(ruta_archivo: str) -> List[List[str]]:
    with open(ruta_archivo, mode='r', newline='', encoding='latin-1') as archivo:
        lector = list(csv.reader(archivo))
        lector=list(map(lambda x: [x[5], x[6],x[3]], lector))
        return lector

def recursion(respuestas, acc: List[str], cat:List[str]) -> List[str]:
    if(len(cat)==0):
        return acc
    
    next(respuestas)
    acc.append(respuestas.send(cat[0]))
    acc.append(next(respuestas))
    cat.pop(0)
    return recursion (respuestas, acc, cat)
    
def get_answers_by_category(preguntas):
    """
    Generator that yields answers based on the received category.
    """
    categoria = None
    while True:
        if categoria is None:
            categoria=yield
        else:
            # answers = [question for question in preguntas if question[3] == categoria]
            answers=list(filter(lambda x: x[2]==categoria,preguntas))
            
            
            indice=random.sample(range(0, len(answers)), 2)
            yield answers[indice[0]][1]
            yield answers[indice[1]][1]

            categoria=yield
            
    
datos = leer_csv('JEOPARDY_CSV.csv')
#respuestas = get_answers_by_category(datos)

#lista=recursion(respuestas,[],["THE COMPANY LINE","HISTORY"])

#print(lista)

column_index = 2
column_values = [row[column_index] for row in datos]

# Count occurrences
value_counts = Counter(column_values)
last_element = list(value_counts.items())[-1]
print(last_element)
count=0
for i in datos:
    if i[2]=="THE COMPANY LINE":
        count+=1
print(count)


#print(next(preguntas))
#print(preguntas.send("THE COMPANY LINE"))
#print(next(preguntas))

#print(next(preguntas))
#print(preguntas.send("HISTORY"))
#print(next(preguntas))



