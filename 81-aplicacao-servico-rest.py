# -*- coding: utf-8 -*-
# encoding=utf8

# Aplicação Web e API REST

from platform import python_version
print('Python Versão:', python_version())

import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

@app.before_first_request
def carregar_modelo():
    app.preditor = load('./modelos/modelo-genero-nome-XGB-nomes-pf.joblib.bz2')
    
@app.route("/")
def index():
    return render_template('index.html', previsao = "")

@app.route('/prever', methods = ['POST'])
def prever():
    dados = request.form['nome']

    tipo = dados

#    data = np.array([np.asarray(data, dtype = float)])
#    predictions = app.predictor.predict(data)

    if tipo == 0:
        genero = 'FEMININO'
    elif tipo == 1:
        genero = 'MASCULINO'
    else:
        genero = ''

    return render_template('index.html', previsao = genero)

def main():
    app.run(host = '0.0.0.0', port = 5000, debug = False)  

if __name__ == '__main__':
    main()

