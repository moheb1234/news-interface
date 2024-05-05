from flask import Flask , request 
import requests
import flask

app = Flask(__name__)


@app.route('/news/<parameters>')
def news(parameters):
    response = requests.get('https://newsapi.org/v2/everything?'+parameters)
    response.raise_for_status
    res = flask.jsonify(response.json())
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
    
    
if __name__ == '__main__':
    app.run(debug=True)
        