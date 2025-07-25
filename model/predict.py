import pandas as pd
import pickle
import os

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')

# Import the ML model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# We mentioned it manually but generally the model version comes from a MLFlow software
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probablities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    
    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all the classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }