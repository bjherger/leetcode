"""
Based on https://xgboost.readthedocs.io/en/stable/get_started.html
"""
from xgboost import XGBClassifier

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Read data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=.2)

# Create model instance

bst = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective='binary:logistic')

# Fit model
bst.fit(X_train, y_train)

print(bst)

# Make predictions
preds = bst.predict(X_test)

print(preds)