from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "pub_75249f33d0835f242d1a6b0ca4c7e2ebe8174" 
NEWS_URL = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&category=politics&country=pk"

@app.route('/')
def home():
    response = requests.get(NEWS_URL)
    print(response.status_code, response.text)  
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('results', [])  
    else:
        articles = []
    
    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
