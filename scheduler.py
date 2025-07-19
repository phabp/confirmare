import schedule
import time
from notifier import enviar_emails_do_dia

def tarefa_diaria():
    print("Executando tarefa programada: envio de e-mails da véspera")
    enviar_emails_do_dia()


schedule.every().day.at("11:00").do(tarefa_diaria)

print("⏰ Agendador iniciado. Aguardando o horário programado...")

while True:
    schedule.run_pending()
    time.sleep(60)
