from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando correctamente"

@app.route('/respuesta', methods=['POST'])
def respuesta():
    data = request.get_json()
    if not data or 'pregunta' not in data:
        return jsonify({'error': 'Solicitud inválida. Se requiere el campo "pregunta".'}), 400

    pregunta = data['pregunta']
    
    # Lógica de respuesta, puede ser IA o algo fijo de prueba
    respuesta = f"Has preguntado: {pregunta}"

    return jsonify({'respuesta': respuesta})
