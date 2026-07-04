import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def main() -> None:
    X, y = make_classification(n_samples=200, n_features=4, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    print(f"Accuracy: {accuracy:.3f}")
    print("NumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)


if __name__ == "__main__":
    main()
