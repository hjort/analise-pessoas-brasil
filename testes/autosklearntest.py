import autosklearn
autosklearn.__version__

from sklearn.datasets import load_iris
data = load_iris()
X_train = data.data
y_train = data.target

import autosklearn.classification
automl = autosklearn.classification.AutoSklearnClassifier(
time_left_for_this_task=2*60,
per_run_time_limit=60,
n_jobs=2,
memory_limit=64,
seed=42,
include_preprocessors=["no_preprocessing"]
)
automl.fit(X_train, y_train)

