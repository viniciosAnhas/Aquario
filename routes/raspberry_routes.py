import subprocess
from flask import Blueprint, jsonify

raspberry_bp = Blueprint('raspberry', __name__)

@raspberry_bp.route('/raspberry/temperatura', methods=['GET'])
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

@raspberry_bp.route('/raspberry/memoria', methods=['GET'])
def raspberry_memory():
    """
    Consultar uso de memória do Raspberry Pi
    ---
    tags:
      - Raspberry
    responses:
      200:
        description: Retorna informações de memória
    """
    try:
        memory_info = subprocess.check_output(["free", "-h"]).decode("utf-8").strip()
        
        lines = memory_info.split('\n')
        memory_data = {
            "raw_output": memory_info,
            "parsed": {}
        }
        
        if len(lines) >= 2:
            headers = lines[0].split()
            values = lines[1].split()
            
            memory_data["parsed"] = {
                "total": values[1],
                "used": values[2],
                "free": values[3],
                "shared": values[4] if len(values) > 4 else "N/A",
                "buff_cache": values[5] if len(values) > 5 else "N/A",
                "available": values[6] if len(values) > 6 else "N/A"
            }
        
        return jsonify(memory_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500