# -*- coding: utf-8 -*-
# encoding=utf8

# Aplicação Web e API REST

# http://hjort.pythonanywhere.com/
# https://medium.com/@kaustuv.kunal/how-to-deploy-and-host-machine-learning-model-de8cfe4de9c5
# https://help.pythonanywhere.com/pages/Virtualenvs/
'''
mkvirtualenv --python=/usr/bin/python3.8 mysite2
workon mysite2
#source ~/.virtualenvs/mysite2/bin/activate
which python
deactivate
rmvirtualenv mysite2
'''

#curl 'http://localhost:5000/prever' -H 'Content-Type: application/json' -d '{"nome":"Leonor"}'
#curl 'http://hjort.pythonanywhere.com/prever' -H 'Content-Type: application/json' -d '{"nome":"Djalma"}'

from platform import python_version
print('Python Versão:', python_version())

import re
import numpy as np
from flask import Flask, request, jsonify, render_template
from json import loads, dumps
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
    app.preditor = load('./modelos/modelo-genero-nome-RF.joblib.bz2')
    
@app.route("/")
def index():
    return render_template('index.html', previsao = "")

@app.route('/prever', methods = ['POST'])
def prever():

    # receber requisições JSON ou HTML
    is_api = False
    if (request.content_type.startswith('application/json')):
        is_api = True
        data = request.get_data()
        dados = loads(data.decode("utf-8"))
        nome = dados['nome']
#        return json.loads(data.decode("utf-8"))
#        return dumps(loads(data))
#        return data
    else:
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

    # responder requisições via API REST (JSON) ou HTML
    if is_api:
        dados['genero'] = genero
        return jsonify(dados)
    else:
        return render_template('index.html', previsao = genero)

def main():
    app.run(host = '0.0.0.0', port = 5000, debug = False)  

if __name__ == '__main__':
    main()

