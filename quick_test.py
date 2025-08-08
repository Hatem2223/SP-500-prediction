import joblib
import pandas as pd
from datetime import datetime

# Load model
model = joblib.load('linear_regression_model.pkl')

# Test with fixed features
features = {
    'SMA_5_t-1': 4455.0,
    'SMA_10_t-1': 4410.0,
    'Price_Change_t-1': 0.04,  # Fixed: 40 * 0.001
    'SMA_20_t-1': 4365.0,
    'EMA_20_t-1': 4387.5,
    'MACD_t-1': 0.5,
    'MACD_signal_t-1': 0.4,
    'MACD_diff_t-1': 0.1,
    'RSI_t-1': 50.0,
    'ATR_t-1': 4.0,
    'year': 2025,
    'month': 8,
    'day': 3,
    'day_of_week': 6,
    'is_month_end': 0,
    'is_month_start': 1
}

df = pd.DataFrame([features])
prediction = model.predict(df)[0]

print(f"Fixed prediction: ${prediction:.2f}")
print(f"Is realistic (4000-5000): {'Yes' if 4000 < prediction < 5000 else 'No'}")
print(f"Difference from input: {prediction - 4500:+.2f}") 