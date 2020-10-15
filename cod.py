import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def numeros_primos():

    limite = 100
    c = 1
    inicio = 1
    numero = 3

    primos = "2, "

    while inicio < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            inicio += 1
            if(inicio % 10 == 0):
                primos = primos + "<br>"
        numero += 1

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)











































  





   

