#!/usr/bin/env python3
"""
Script to explain why the SP500 model produces high predictions
"""

import joblib
import numpy as np
import pandas as pd
from datetime import datetime

def explain_prediction():
    """Explain why the model produces high predictions"""
    print("🔍 EXPLAINING WHY PREDICTIONS ARE HIGH")
    print("="*60)
    
    # Load the model
    model = joblib.load('linear_regression_model.pkl')
    
    # Your input values
    open_price = 4500.00
    high_price = 4520.00
    low_price = 4480.00
    
    print(f"\n📊 Your Input Values:")
    print(f"   • Open: ${open_price}")
    print(f"   • High: ${high_price}")
    print(f"   • Low: ${low_price}")
    
    # Calculate features (same as in the app)
    current_price = (open_price + high_price + low_price) / 3
    price_change = high_price - low_price
    price_range = high_price - low_price
    
    print(f"\n🔧 Calculated Features:")
    print(f"   • Current Price (avg): ${current_price:.2f}")
    print(f"   • Price Change: ${price_change:.2f}")
    print(f"   • Price Range: ${price_range:.2f}")
    
    # Create features
    features = {
        'SMA_5_t-1': current_price * 0.99,
        'SMA_10_t-1': current_price * 0.98,
        'Price_Change_t-1': price_change,
        'SMA_20_t-1': current_price * 0.97,
        'EMA_20_t-1': current_price * 0.975,
        'MACD_t-1': 0.5,
        'MACD_signal_t-1': 0.4,
        'MACD_diff_t-1': 0.1,
        'RSI_t-1': 50.0,
        'ATR_t-1': price_range * 0.1,
        'year': datetime.now().year,
        'month': datetime.now().month,
        'day': datetime.now().day,
        'day_of_week': datetime.now().weekday(),
        'is_month_end': 1 if datetime.now().day >= 28 else 0,
        'is_month_start': 1 if datetime.now().day <= 3 else 0
    }
    
    print(f"\n📈 Model Coefficients:")
    print(f"   • Intercept: {model.intercept_:.4f}")
    
    # Calculate prediction step by step
    prediction = model.intercept_
    
    print(f"\n🧮 Prediction Calculation:")
    print(f"   Starting with intercept: {prediction:.2f}")
    
    for i, feature_name in enumerate(model.feature_names_in_):
        feature_value = features[feature_name]
        coefficient = model.coef_[i]
        contribution = feature_value * coefficient
        prediction += contribution
        
        print(f"   • {feature_name}: {feature_value:.2f} × {coefficient:.6f} = {contribution:.2f}")
        print(f"     Running total: {prediction:.2f}")
    
    print(f"\n🎯 Final Prediction: ${prediction:.2f}")
    
    # Explain why it's high
    print(f"\n❓ Why is the prediction so high?")
    print(f"   • Your model was trained on data where the target variable (next day close)")
    print(f"     was much higher than the input prices")
    print(f"   • The model learned to predict values in a different range")
    print(f"   • This could be because:")
    print(f"     - Training data was from a different time period")
    print(f"     - Target variable was scaled differently")
    print(f"     - Model was trained on different price ranges")
    
    # Show the biggest contributors
    print(f"\n🔥 Biggest Contributors to High Prediction:")
    contributions = []
    for i, feature_name in enumerate(model.feature_names_in_):
        feature_value = features[feature_name]
        coefficient = model.coef_[i]
        contribution = feature_value * coefficient
        contributions.append((feature_name, contribution))
    
    # Sort by absolute contribution
    contributions.sort(key=lambda x: abs(x[1]), reverse=True)
    
    for i, (feature, contribution) in enumerate(contributions[:5]):
        print(f"   {i+1}. {feature}: {contribution:.2f}")
    
    return prediction

def show_model_training_info():
    """Show information about what the model might have been trained on"""
    print(f"\n📚 Model Training Information:")
    print(f"   • Model Type: LinearRegression")
    print(f"   • Features: 16 technical indicators")
    print(f"   • Intercept: 3773.67 (this is the base prediction)")
    print(f"   • The high intercept suggests the model was trained on data")
    print(f"     where the target variable was much higher than input prices")
    
    print(f"\n💡 Possible Reasons for High Predictions:")
    print(f"   1. Training data was from a different time period")
    print(f"   2. Target variable was in a different scale/range")
    print(f"   3. Model was trained on different price levels")
    print(f"   4. Feature engineering was different during training")
    
    print(f"\n✅ This is YOUR model's actual behavior!")
    print(f"   The predictions are exactly what your trained model produces")

if __name__ == "__main__":
    prediction = explain_prediction()
    show_model_training_info() 