import requests
import html2text
import re


def descargar_pagina(url):
    '''
    Lee paginas web y las convierte a texto
    '''
    page = requests.get(url)
    content = html2text.html2text(page.text)
    return content


def contar_palabras(texto):
    '''
    Calcular la frecuencia de aparicion de N palabras en HTML
    '''
    frec = {}
    texto = re.sub('[^\w\s]+', '', texto)
    for w in texto.lower().split():
        if len(w) > 3:
            frec[w] = frec.get(w, 0) + 1
    frec_sorted = sorted(frec.items(), key=lambda x: x[1], reverse=True)
    return frec_sorted
