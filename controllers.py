import main
import flask
import knn_alogritma
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

@app.route("/yapay_knn")
def yapay_api1():
        return flask.jsonify(knn_alogritma.yapay_knn_fonksiyon(flask.request.args.get('liste')))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80,debug = True)