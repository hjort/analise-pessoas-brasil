# -*- coding: utf-8 -*-
# encoding=utf8

# Aplicação Web e API REST

from platform import python_version
print('Python Versão:', python_version())

import re
import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

def obter_primeiro_nome(str):
    if str:
        return re.split("\s", str)[0].upper()

MAIOR_QTDE_LETRAS = 16

def obter_array_letras(str):
    if not str:
        return None
    rev = str[::-1]
    anome = []
    for i in range(MAIOR_QTDE_LETRAS):
        x = ord(rev[i]) - 64 if len(rev) > i else 0
        anome.append(x)
    return anome

app = Flask(__name__)

@app.before_first_request
def carregar_modelo():
    app.preditor = load('./modelos/modelo-genero-nome-XGB-nomes-pf.joblib.bz2')
    
@app.route("/")
def index():
    return render_template('index.html', previsao = "")

@app.route('/prever', methods = ['POST'])
def prever():
    nome = request.form['nome']
    print("=> nome:", nome)

    # extrair primeiro nome e obter array de letras invertido
    anome = obter_array_letras(obter_primeiro_nome(nome))

    # prever o gênero a partir do nome
    if anome:
        tipo = app.preditor.predict(np.asarray([anome]))[0]
    else:
        tipo = None

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

