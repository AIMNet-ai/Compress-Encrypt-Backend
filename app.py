from flask import Flask, request, jsonify, send_file, request
from werkzeug.utils import secure_filename
import os
import classBased as cb
import json
hf = cb.Huffboth()

decode_dir = 'decoded'
encodedCompressed_dir = 'encodedCompressed'
encodedUncompressed_dir = 'encodedUncompressed'

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
        "output": encoded,
    })


@app.route("/api/huffman-text-decode", methods=["POST"])
def huffmanTextDecode():
    # print(request.get_json())
    obj = request.get_json()
    input = obj["payload"]
    # print(input)
    decoded = hf.Decode(input)
    return jsonify({
        "output": decoded,
    })

###############################################################


@app.route('/api/upload-normal-file', methods=["POST"])
def uploadNormalFile():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(decode_dir, secure_filename(f.filename)))
        return 'normal file uploaded successfully'
    return "Normal File Upload Route"


@app.route('/api/upload-encoded-compressed-file', methods=["POST"])
def getEncodedCompressedFile():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(encodedCompressed_dir, secure_filename(f.filename)))
        return 'binary file uploaded successfully'
    return "Binary File Upload Route"

###############################################################


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
