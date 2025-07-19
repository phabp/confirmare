from flask import Flask, render_template, request, redirect
import psycopg2
from flask_mail import Mail, Message

print("Rodando o arquivo:", __file__)

app = Flask(__name__)
app.config.from_pyfile('config.py')

mail = Mail(app)  


conn = psycopg2.connect(
    host="localhost",
    database="consultorio",
    user="postgres",
    password="Firework05142310!"
)

@app.route('/')
def home():
    print("Rota '/' acessada")
    return render_template('paginainicial.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        whatsapp = request.form['whatsapp']
        data = request.form['data']    
        hora = request.form['hora']    

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO consultas (nome, email, whatsapp, data, hora) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, whatsapp, data, hora)
        )
        conn.commit()
        cur.close()

        if email:
            try:
                msg = Message(
                    subject="Confirmação de Consulta",
                    recipients=[email],
                    body=f"Olá, {nome}!\n\nSua consulta está confirmada para o dia {data} às {hora}.\n\nConsultório XYZ"
                )
                mail.send(msg)
                print("E-mail enviado para:", email)
            except Exception as e:
                print("Erro ao enviar e-mail:", e)
        
        return redirect('/cadastrar')

    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)
