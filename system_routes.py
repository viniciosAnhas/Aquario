import subprocess
from flask import Blueprint, jsonify

# Blueprint para rotas do sistema
system_bp = Blueprint('system', __name__)

@system_bp.route('/system/status', methods=['GET'])
def system_status():
    """
    Consultar temperatura e voltagem do Raspberry Pi
    ---
    tags:
      - Raspberry
    responses:
      200:
        description: Retorna temperatura e voltagem atuais
    """
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8").strip()
        volts = subprocess.check_output(["vcgencmd", "measure_volts"]).decode("utf-8").strip()
        return jsonify({
            "temperature": temp,
            "voltage": volts
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
