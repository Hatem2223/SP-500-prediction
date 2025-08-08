#!/usr/bin/env python3
"""
Setup script for global access to SP500 Predictor
"""

import requests
import socket
import webbrowser
import time

def get_public_ip():
    """Get your public IP address"""
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except:
        return "Could not determine public IP"

def get_local_ip():
    """Get your local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "192.168.8.127"  # Fallback

def setup_global_access():
    print("🌍 Setting up GLOBAL ACCESS for your SP500 Predictor")
    print("=" * 60)
    
    # Get IP addresses
    public_ip = get_public_ip()
    local_ip = get_local_ip()
    
    print(f"📍 Your Local IP: {local_ip}")
    print(f"🌐 Your Public IP: {public_ip}")
    print()
    
    print("🚀 STEP-BY-STEP GUIDE FOR GLOBAL ACCESS:")
    print("=" * 60)
    
    print("1️⃣  PORT FORWARDING SETUP:")
    print("   • Access your router admin (usually http://192.168.1.1)")
    print("   • Find 'Port Forwarding' or 'Virtual Server'")
    print("   • Add new rule with these settings:")
    print(f"     - External Port: 5000")
    print(f"     - Internal IP: {local_ip}")
    print(f"     - Internal Port: 5000")
    print(f"     - Protocol: TCP")
    print()
    
    print("2️⃣  FIREWALL SETUP:")
    print("   • Open Windows Firewall")
    print("   • Allow Python/Flask on port 5000")
    print("   • Or temporarily disable firewall for testing")
    print()
    
    print("3️⃣  TEST YOUR SETUP:")
    print("   • Ask a friend to try: http://[YOUR_PUBLIC_IP]:5000")
    print(f"   • Example: http://{public_ip}:5000")
    print()
    
    print("4️⃣  ALTERNATIVE: FREE TUNNEL SERVICES")
    print("   • Try LocalTunnel again: lt --port 5000")
    print("   • Or use ngrok (requires free signup)")
    print("   • Or use Cloudflare Tunnel")
    print()
    
    print("🔧 TROUBLESHOOTING:")
    print("   • Make sure your computer stays on")
    print("   • Check if your ISP blocks port 5000")
    print("   • Try different ports (8080, 3000)")
    print()
    
    print("📱 WHAT YOUR FRIENDS WILL SEE:")
    print("   • Beautiful SP500 prediction interface")
    print("   • Simple form to enter stock data")
    print("   • Instant predictions for next day")
    print("   • Works on phones, tablets, computers")
    print()
    
    print("💡 PRO TIPS:")
    print("   • Test on your phone first")
    print("   • Keep your computer running")
    print("   • Consider using a domain name")
    print("   • Set up SSL for security")
    
    print("=" * 60)
    print("🎯 Your SP500 Predictor will be accessible GLOBALLY!")
    
    # Offer to open router admin
    choice = input("\n❓ Want to open router admin page? (y/n): ").lower()
    if choice == 'y':
        webbrowser.open("http://192.168.1.1")
        webbrowser.open("http://192.168.0.1")

if __name__ == "__main__":
    setup_global_access() 