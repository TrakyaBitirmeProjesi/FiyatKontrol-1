import main
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def index():
    return flask.render_template("index.html")

@app.route("/results")
def results():
    return flask.render_template("results.html",migros_data = main.migros_checker(flask.request.args.get('product-name')),carrefoursa_data = main.carrefoursa_checher(flask.request.args.get('product-name')))

@app.route("/carrefoursa")
def carrefoursa_api():
    if flask.request.args.get('product-name'):
        return flask.jsonify(main.carrefoursa_checher(flask.request.args.get('product-name')))
    else:
        return flask.abort(404)

@app.route("/migros")
def migros_api():
    if flask.request.args.get('product-name'):
        return flask.jsonify(main.migros_checker(flask.request.args.get('product-name')))
    else:
        return flask.abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80,debug = True)
