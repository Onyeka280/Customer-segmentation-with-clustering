from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def create_preprocessor(numeric_features):
    scaler = RobustScaler()
    preprocessor = ColumnTransformer(transformers=[
        ('num', scaler, numeric_features)
    ])
    return preprocessor
