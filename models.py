# models.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

def run_models(input_dict):
    # Example dummy response (replace with real inference using input_dict)
    return {
        "random_forest": {"accuracy": 0.95},
        "svm": {"accuracy": 0.91},
        "autoencoder": {"accuracy": 0.89}
    }
