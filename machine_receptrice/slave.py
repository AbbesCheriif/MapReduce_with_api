from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)

# Route pour traiter le texte reçu
@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get('text', '')

    # Fonction map pour compter les mots
    def map_word_count(text_chunk):
        words = text_chunk.split()
        return Counter(words)
   
    # Compter les mots dans la partie du texte reçue
    word_count = map_word_count(text)
   
    # Retourner les résultats sous forme de JSON
    return jsonify(word_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # API écoute sur le port 5000