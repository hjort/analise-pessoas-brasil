import pandas as pd
import numpy as np

arquivo = 'afastamentos-nomes-sexo-preparado.pkl.bz2'

df = pd.read_pickle(arquivo)

X = df.drop(['SEXO'], axis=1) # tudo, exceto a coluna alvo
y = df['SEXO'] # apenas a coluna alvo
print('Forma dos dados originais:', X.shape, y.shape)

# dividir dados em treino e teste

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

print("Shapes:", X_train.shape, X_test.shape, y_train.shape, y_test.shape)

import autosklearn.classification

automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=10*60,
    per_run_time_limit=2*60,
    n_jobs=2,
    memory_limit=1024,
    seed=42,
    include_preprocessors=["no_preprocessing"]
)
automl.fit(X_train, y_train)

