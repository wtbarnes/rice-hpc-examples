"""
Train a random forest classifier with scikit-learn
Adapted from https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
"""
# Import needed packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


# Create some dummy data
X, y = make_classification(n_samples=1000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
# Initialize the classifier
clf = RandomForestClassifier(n_estimators=100, max_depth=2,
                             random_state=0)
# Train the model
clf.fit(X, y)

# Print important features
print(clf.feature_importances_)
# Classify some unseen data
print(clf.predict([[0, 0, 0, 0]]))
