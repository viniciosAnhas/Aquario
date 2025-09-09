import os
from flask import current_app
from dotenv import load_dotenv

def ligar_motor_automatico(app):
    """
    Função para ligar o motor automaticamente
    """
    with app.app_context():
        try:
            from routes.motor_routes import motor_on
            
            result = motor_on()
            print("✅ Motor ligado automaticamente no horário agendado")
            return result
        except Exception as e:
            print(f"❌ Erro ao ligar motor automaticamente: {e}")
            return {"error": str(e)}

def desligar_motor_automatico(app):
    """
    Função para desligar o motor automaticamente
    """
    with app.app_context():
        try:
            from routes.motor_routes import motor_off
            result = motor_off()
            print("✅ Motor DESLIGADO automaticamente no horário agendado")
            return result
        except Exception as e:
            print(f"❌ Erro ao desligar motor automaticamente: {e}")
            return {"error": str(e)}

def iniciar_agendamentos(scheduler, app):
    """
    Configura todos os agendamentos de ligar e desligar
    """
    try:
        ligar_hora = int(os.getenv('LIGAR_HORA'))
        ligar_minuto = int(os.getenv('LIGAR_MINUTO'))
        ligar_segundo = int(os.getenv('LIGAR_SEGUNDO'))

        desligar_hora = int(os.getenv('DESLIGAR_HORA'))
        desligar_minuto = int(os.getenv('DESLIGAR_MINUTO'))
        desligar_segundo = int(os.getenv('DESLIGAR_SEGUNDO'))
        
        @scheduler.task('cron', id='ligar_motor_diario', 
                       hour=ligar_hora, minute=ligar_minuto, second=ligar_segundo)
        def tarefa_ligar_motor():
            ligar_motor_automatico(app)
        
        @scheduler.task('cron', id='desligar_motor_diario', 
                       hour=desligar_hora, minute=desligar_minuto, second=desligar_segundo)
        def tarefa_desligar_motor():
            desligar_motor_automatico(app)
        
        print(f"🕐 Agendador configurado:")
        print(f"   - ✅ Ligar motor: {ligar_hora:02d}:{ligar_minuto:02d}:{ligar_segundo:02d}")
        print(f"   - 🔴 Desligar motor: {desligar_hora:02d}:{desligar_minuto:02d}:{desligar_segundo:02d}")
        
    except ValueError as e:
        print(f"❌ Erro na configuração do agendamento: Valores inválidos no .env - {e}")
    except Exception as e:
        print(f"❌ Erro ao configurar agendamento: {e}")