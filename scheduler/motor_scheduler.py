import os
from flask import current_app
from dotenv import load_dotenv

def ligar_motor_automatico():
    """
    Função para ligar o motor automaticamente
    """
    try:
        from routes.motor_routes import motor_on
        result = motor_on()
        print("✅ Motor ligado automaticamente no horário agendado")
        return result
    except Exception as e:
        print(f"❌ Erro ao ligar motor automaticamente: {e}")
        return {"error": str(e)}

def iniciar_agendamentos(scheduler):
    """
    Configura todos os agendamentos a partir das variáveis de ambiente
    """
    try:
        hora = int(os.getenv('AGENDAMENTO_HORA'))
        minuto = int(os.getenv('AGENDAMENTO_MINUTO'))

        @scheduler.task('cron', id='ligar_motor_diario', hour=hora, minute=minuto)
        def tarefa_agendada_motor():
            with current_app.app_context():
                ligar_motor_automatico()

        print(f"🕐 Agendador configurado - Motor será ligado às {hora:02d}:{minuto:02d} diariamente")

    except ValueError as e:
        print(f"❌ Erro na configuração do agendamento: Valores inválidos no .env - {e}")
    except Exception as e:
        print(f"❌ Erro ao configurar agendamento: {e}")