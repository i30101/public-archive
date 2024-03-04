from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, auc
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# generate a synthetic dataset for binary classification
X, y = make_classification(n_samples=1000, n_classes=2, weights=[0.9, 0.1], random_state=42)

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fit a logistic regression model on the training data
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# predict the class probabilities for the testing data
y_pred_prob = lr_model.predict_proba(X_test)[:, 1]

# compute the precision, recall, and thresholds for the precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)

# compute the area under the precision-recall curve (AUC)
auc_score = auc(recall, precision)

# plot the precision-recall curve
plt.plot(recall, precision, label='Precision-Recall curve (AUC = {:.2f})'.format(auc_score))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall curve')
plt.legend()
plt.show()
