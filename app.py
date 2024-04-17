from flask import Flask , request
import requests

app = Flask(__name__)


@app.route('/news/<parameters>')
def news(parameters):
    response = requests.get('https://newsapi.org/v2/everything?'+parameters)
    response.raise_for_status
    return response.json()
    
    
if __name__ == '__main__':
    app.run()
        