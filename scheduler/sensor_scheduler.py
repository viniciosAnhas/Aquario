import os
import random
import mysql.connector
from mysql.connector import Error
from flask import current_app

def conectar_banco():
    """Conecta ao banco de dados MySQL"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")
        return None

def inserir_nivel_agua(app):
    """Gera e insere o nível de água no banco"""
    with app.app_context():
        try:
            nivel_agua = random.randint(0, 100)
            
            connection = conectar_banco()
            if connection:
                cursor = connection.cursor()

                query = "INSERT INTO NIVELAGUA (NIVEL, DATA) VALUES (%s, SYSDATE())"
                cursor.execute(query, (nivel_agua,))
                connection.commit()
                
                print(f"✅ Nível de água inserido: {nivel_agua}%")
                
                cursor.close()
                connection.close()
                
                return {"nivel_agua": nivel_agua, "status": "inserido_no_banco"}
            else:
                return {"error": "Falha na conexão com o banco"}
                
        except Error as e:
            print(f"❌ Erro ao inserir no banco: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"❌ Erro geral: {e}")
            return {"error": str(e)}

def iniciar_agendamento_sensor(scheduler, app):
    """Configura o agendamento do sensor"""
    try:
        intervalo = int(os.getenv('SENSOR_INTERVAL'))
        
        @scheduler.task('interval', id='coletar_nivel_agua', minutes=intervalo)
        def tarefa_coletar_nivel():
            inserir_nivel_agua(app)
        
        print(f"🕐 Agendador do sensor configurado - Coleta a cada {intervalo} minutos")
        
    except Exception as e:
        print(f"❌ Erro ao configurar agendamento do sensor: {e}")