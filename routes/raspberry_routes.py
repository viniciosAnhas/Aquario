import subprocess
from flask import Blueprint, jsonify

raspberry_bp = Blueprint('raspberry', __name__)

@raspberry_bp.route('/raspberry/status', methods=['GET'])
def raspberry_status():
    """
    Consultar temperatura do Raspberry Pi
    ---
    tags:
      - Raspberry
    responses:
      200:
        description: Retorna temperatura
    """
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8").strip()
        return jsonify({
            "temperature": temp
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
