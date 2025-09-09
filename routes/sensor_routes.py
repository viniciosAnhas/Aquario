import random
from flask import Blueprint, jsonify

sensor_bp = Blueprint('sensor', __name__)

@sensor_bp.route('/sensor/nivelagua', methods=['GET'])
def agua_level():
    """
    Consultar nível de água (simulado)
    ---
    tags:
      - Sensor
    responses:
      200:
        description: Retorna nível de água em porcentagem
    """
    try:
        nivelAgua = random.randint(0, 100)
        return jsonify({
            "nivelAgua": f"{nivelAgua}%"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500