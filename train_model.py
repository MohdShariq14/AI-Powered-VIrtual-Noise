# 🎯 This file will train the ML model using simulated data.

# train_model.py
from simulate_data import simulate_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Generate data
df = simulate_data(200)
X = df[['MQ2', 'MQ3', 'MQ135']]
y = df['Label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("Model trained and saved as 'model.pkl'")
# Show accuracy
y_pred = model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
