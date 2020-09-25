from flask import Flask, request, jsonify, send_file, request
import classBased as cb
import json
hf = cb.Huffboth()

app = Flask(__name__)

###############################################################


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


@app.route('/home')
def index2():
    return "<h1>Welcome to Home server !!</h1>"


@app.route('/api/home')
def index3():
    return jsonify({
        "home": "This is home sweet home",
    })
###############################################################


@app.route("/api/huffman-text-encode", methods=["POST"])
def huffmanTextEncode():
    # print(request.get_json())
    obj = request.get_json()
    input = obj["payload"]
    # print(input)
    encoded = hf.Encode(input)
    return jsonify({
        "title": encoded,
    })


@app.route("/api/huffman-text-decode", methods=["POST"])
def huffmanTextDecode():
    # print(request.get_json())
    obj = request.get_json()
    input = obj["payload"]
    # print(input)
    decoded = hf.Decode(input)
    return jsonify({
        "title": decoded,
    })


@app.route('/encoded-uncompressed/<ID>')
def getEncodedUncompressedFile(ID):
    filename = f'uploads/image-{ID}.png'
    return send_file(filename, mimetype='image/png')


@app.route('/decoded/<ID>')
def getDecodedFile(ID):
    filename = f'uploads/image-{ID}.png'
    return send_file(filename, mimetype='image/png')


@app.route('/encoded-compressed/<ID>')
def getEncodedCompressedFile(ID):
    filename = f'uploads/image-{ID}.png'
    return send_file(filename, mimetype='image/png')


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.run(threaded=True, port=5000, debug=True)
