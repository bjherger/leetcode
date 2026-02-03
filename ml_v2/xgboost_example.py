import xgboost
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

iris = load_iris()

iris_data = iris.data
iris_target = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.2, random_state=42)

model = xgboost.XGBClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions)

# Compute precision, recall, and f1 score (weighted for multiclass)
print(precision_score(y_test, predictions, average="weighted"))
print(recall_score(y_test, predictions, average="weighted"))
print(f1_score(y_test, predictions, average="weighted"))