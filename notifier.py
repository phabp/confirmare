from flask import Flask
from flask_mail import Mail, Message
import psycopg2
from datetime import date, timedelta


app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)


conn = psycopg2.connect(
    host="localhost",
    database="consultorio",
    user="postgres",
    password="Firework05142310!"
)

def enviar_email(destinatario, nome, data, hora):
    with app.app_context():
        try:
            msg = Message(
                subject="Confirmação de Consulta",
                recipients=[destinatario],
                body=f"Olá, {nome}!\n\nSua consulta está confirmada para o dia {data} às {hora}.\n\nConsultório XYZ"
            )
            mail.send(msg)
            print(f"E-mail enviado para {destinatario}")
        except Exception as e:
            print(f"Erro ao enviar e-mail para {destinatario}: {e}")

def enviar_emails_do_dia():
    cur = conn.cursor()
    amanha = (date.today() + timedelta(days=1)).isoformat()

    cur.execute("SELECT nome, email, data, hora FROM consultas WHERE data = %s", (amanha,))
    consultas = cur.fetchall()
    cur.close()

    for nome, email, data_consulta, hora in consultas:
        if email:
            enviar_email(email, nome, data_consulta.strftime('%d/%m/%Y'), hora)
