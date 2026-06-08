from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Features: [Hours Studied, Attendance %]
X = [[2, 50], [8, 90], [1, 40], [9, 95], [4, 70], [7, 85]]
# Labels: 0 = Fail, 1 = Pass
y = [0, 1, 0, 1, 0, 1]

# Train a Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for a new student who studied 6 hours with 80% attendance
prediction = model.predict([[6, 80]])
print("Prediction (0=Fail, 1=Pass):", prediction[0])