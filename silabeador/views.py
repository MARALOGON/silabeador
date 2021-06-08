from silabeador import app
from silabeador.tools import pilengua
from flask import jsonify
import requests

@app.route("/pilengua/<frase>")
def enlenguapi(frase):
    respuesta = pilengua(frase)
    d = {
        'original': frase, 
        'pilengua': respuesta
    }
    return jsonify(d)


@app.route("/pelicula/<palabra>")
def pelicula(palabra):
    url = "http://www.omdbapi.com/?s={}&apikey=b8d84844"

    resultado = requests.get(url.format(palabra))
    if resultado.status_code == 200:
        peliculas = resultado.json() #Dvuelve un diccionario del resultado, que contiene todas las peliculas que aparecen con la busqueda
        if peliculas['Response'] == "False":
            return jsonify({'status': "Error", "msg": "No se han encontrado resultados"})

        return jsonify({"Peliculas": peliculas["Search"], 'status': "Success"})
