#!/usr/bin/env python3
"""
Script to share your SP500 Predictor with friends using Cloudflare Tunnel
"""

import subprocess
import webbrowser
import time
import sys

def share_with_cloudflare():
    print("🌐 Setting up Cloudflare Tunnel for your SP500 Predictor...")
    print("=" * 60)
    
    try:
        # Start Cloudflare tunnel
        print("🚀 Starting Cloudflare tunnel...")
        tunnel_process = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:5000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a moment for tunnel to establish
        time.sleep(3)
        
        # Try to get the tunnel URL from output
        if tunnel_process.poll() is None:
            print("✅ Cloudflare tunnel is running!")
            print("🔗 Your app should be accessible via the Cloudflare tunnel URL")
            print("💡 Check the terminal output above for the public URL")
            
            print("\n📱 Your friends can now access your SP500 Predictor!")
            print("💡 They just need to:")
            print("   1. Use the Cloudflare tunnel URL")
            print("   2. Enter stock data (Open, High, Low)")
            print("   3. Get predictions!")
            
            print(f"\n⏹️  To stop sharing, press Ctrl+C")
            print("=" * 60)
            
            # Keep the tunnel open
            try:
                while True:
                    time.sleep(1)
                    if tunnel_process.poll() is not None:
                        break
            except KeyboardInterrupt:
                print("\n🛑 Stopping Cloudflare tunnel...")
                tunnel_process.terminate()
                print("✅ Tunnel stopped")
        else:
            print("❌ Failed to start Cloudflare tunnel")
            print("💡 Make sure cloudflared is installed and your Flask app is running!")
            
    except FileNotFoundError:
        print("❌ Cloudflared not found!")
        print("💡 Install it from: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    share_with_cloudflare() 