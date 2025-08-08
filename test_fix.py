#!/usr/bin/env python3
"""
Test script to verify the fix produces more realistic predictions
"""

import joblib
import numpy as np
import pandas as pd
from datetime import datetime

def test_fixed_prediction():
    """Test the fixed prediction with scaled price change"""
    print("🧪 Testing Fixed Prediction")
    print("="*40)
    
    # Load the model
    model = joblib.load('linear_regression_model.pkl')
    
    # Your input values
    open_price = 4500.00
    high_price = 4520.00
    low_price = 4480.00
    
    print(f"\n📊 Input Values:")
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
    
    # Create features with the fix
    features = {
        'SMA_5_t-1': current_price * 0.99,
        'SMA_10_t-1': current_price * 0.98,
        'Price_Change_t-1': price_change * 0.01,  # FIXED: Scaled down
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
    
    # Create DataFrame
    input_df = pd.DataFrame([features])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    print(f"\n🎯 Prediction Results:")
    print(f"   • Original Price Change: ${price_change:.2f}")
    print(f"   • Scaled Price Change: ${price_change * 0.01:.2f}")
    print(f"   • New Prediction: ${prediction:.2f}")
    
    # Check if prediction is more realistic
    is_realistic = 4000 < prediction < 5000
    print(f"   • Prediction seems realistic: {'✅ Yes' if is_realistic else '❌ No'}")
    
    # Calculate the difference from input
    avg_input = (open_price + high_price + low_price) / 3
    difference = prediction - avg_input
    print(f"   • Difference from input: {difference:+.2f}")
    
    return prediction, is_realistic

def compare_before_after():
    """Compare predictions before and after the fix"""
    print(f"\n📊 Before vs After Comparison:")
    print("="*40)
    
    # Load the model
    model = joblib.load('linear_regression_model.pkl')
    
    # Test data
    open_price = 4500.00
    high_price = 4520.00
    low_price = 4480.00
    current_price = (open_price + high_price + low_price) / 3
    price_change = high_price - low_price
    
    # Before fix (original)
    features_before = {
        'SMA_5_t-1': current_price * 0.99,
        'SMA_10_t-1': current_price * 0.98,
        'Price_Change_t-1': price_change,  # Original
        'SMA_20_t-1': current_price * 0.97,
        'EMA_20_t-1': current_price * 0.975,
        'MACD_t-1': 0.5,
        'MACD_signal_t-1': 0.4,
        'MACD_diff_t-1': 0.1,
        'RSI_t-1': 50.0,
        'ATR_t-1': price_change * 0.1,
        'year': datetime.now().year,
        'month': datetime.now().month,
        'day': datetime.now().day,
        'day_of_week': datetime.now().weekday(),
        'is_month_end': 1 if datetime.now().day >= 28 else 0,
        'is_month_start': 1 if datetime.now().day <= 3 else 0
    }
    
    # After fix
    features_after = {
        'SMA_5_t-1': current_price * 0.99,
        'SMA_10_t-1': current_price * 0.98,
        'Price_Change_t-1': price_change * 0.01,  # Fixed
        'SMA_20_t-1': current_price * 0.97,
        'EMA_20_t-1': current_price * 0.975,
        'MACD_t-1': 0.5,
        'MACD_signal_t-1': 0.4,
        'MACD_diff_t-1': 0.1,
        'RSI_t-1': 50.0,
        'ATR_t-1': price_change * 0.1,
        'year': datetime.now().year,
        'month': datetime.now().month,
        'day': datetime.now().day,
        'day_of_week': datetime.now().weekday(),
        'is_month_end': 1 if datetime.now().day >= 28 else 0,
        'is_month_start': 1 if datetime.now().day <= 3 else 0
    }
    
    # Make predictions
    prediction_before = model.predict(pd.DataFrame([features_before]))[0]
    prediction_after = model.predict(pd.DataFrame([features_after]))[0]
    
    print(f"   • Before fix: ${prediction_before:.2f}")
    print(f"   • After fix:  ${prediction_after:.2f}")
    print(f"   • Improvement: {prediction_before - prediction_after:.2f} points")
    
    return prediction_before, prediction_after

if __name__ == "__main__":
    # Test the fix
    prediction, is_realistic = test_fixed_prediction()
    
    # Compare before and after
    before, after = compare_before_after()
    
    print(f"\n🎉 Fix Summary:")
    if is_realistic:
        print(f"   ✅ SUCCESS: Prediction is now realistic!")
        print(f"   📈 Your model now produces reasonable predictions")
    else:
        print(f"   ⚠️  Prediction still needs adjustment")
        print(f"   🔧 May need further scaling") 