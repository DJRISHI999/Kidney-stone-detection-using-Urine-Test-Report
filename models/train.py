import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

# Load the dataset
def load_dataset(file_path):
    return pd.read_csv(file_path)

# Preprocess the dataset
def preprocess_data(df):
    # Drop the serial number column and any rows with missing values
    df = df.dropna().drop(columns=['Unnamed: 0'])
    X = df.drop('target', axis=1)
    y = df['target']
    return X, y

# Train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Save the model
def save_model(model, file_path):
    joblib.dump(model, file_path)

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, precision, recall, f1, cm

if __name__ == "__main__":
    # Load and preprocess the dataset
    df = load_dataset('data/kidney-stone-dataset.csv')
    X, y = preprocess_data(df)
    
    # Train the model
    model, X_test, y_test = train_model(X, y)
    
    # Save the model
    save_model(model, 'models/kidney_stone_model.pkl')
    
    # Evaluate the model
    accuracy, precision, recall, f1, cm = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")
    print(f"Confusion Matrix:\n{cm}")