#!/usr/bin/env python3
"""
Script to share your SP500 Predictor with friends using ngrok
"""

from pyngrok import ngrok
import webbrowser
import time
import os

def share_app():
    print("🌐 Setting up public access for your SP500 Predictor...")
    print("=" * 50)
    
    try:
        # Create a public URL using ngrok
        public_url = ngrok.connect(5000)
        print(f"✅ Public URL created: {public_url}")
        print(f"🔗 Share this link with your friends: {public_url}")
        
        # Open the URL in browser
        print("🌍 Opening in browser...")
        webbrowser.open(public_url)
        
        print("\n📱 Your friends can now access your SP500 Predictor!")
        print("💡 They just need to:")
        print("   1. Click the link you share")
        print("   2. Enter stock data (Open, High, Low)")
        print("   3. Get predictions!")
        
        print(f"\n⏹️  To stop sharing, press Ctrl+C")
        print("=" * 50)
        
        # Keep the tunnel open
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping public access...")
        ngrok.kill()
        print("✅ Public access stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure your Flask app is running first!")

if __name__ == "__main__":
    share_app() 