from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/preguntar', methods=['POST'])
def responder():
    data = request.get_json()
    pregunta = data.get('pregunta', '').lower()

    if "correo" in pregunta:
        respuesta = "Para abrir tu correo, ve a gmail.com y accede con tu cuenta."
    elif "word" in pregunta:
        respuesta = "Para abrir Word, haz clic en el botón de inicio y escribe Word."
    else:
        respuesta = "Lo siento, aún estoy aprendiendo sobre eso."

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run()
