from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando correctamente"

@app.route("/respuesta", methods=["POST"])
def responder():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    
    # Aquí puedes reemplazar esta respuesta por una lógica real
    return jsonify({"respuesta": f"Tu pregunta fue: {pregunta}"})
