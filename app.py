from flask import Flask, request, jsonify, send_file
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


@app.route("/api/huffman-text-encode")
def huffmanTextEncode():
    return jsonify({
        "title": "Huffman Text Encode",
    })


@app.route("/api/huffman-text-decode")
def huffmanTextDecode():
    return jsonify({
        "title": "Huffman Text Decode",
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
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
