from flask import request, jsonify
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize

from settings import app


@app.route('/tokenize', methods=['POST'])
def tokenize():
    if 'text' in request.json and request.json['text'] != '':
        return jsonify({'tokens': word_tokenize(request.json['text'])})
    return {'error': 'Please, input text'}


@app.route('/pos_tag', methods=['POST'])
def tag_pos():
    if 'text' in request.json and request.json['text'] != '':
        return jsonify({'tags': pos_tag(word_tokenize(request.json['text']))})
    return {'error': 'Please, input text'}


@app.route('/ner', methods=['POST'])
def ner():
    if 'text' in request.json and request.json['text'] != '':
        return jsonify({'chunks': ne_chunk(pos_tag(word_tokenize(request.json['text'])))})
    return {'error': 'Please, input text'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')