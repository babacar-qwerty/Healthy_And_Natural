from flask import Flask,render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# CONFIGURATIONS DU SERVEUR MAIL:
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']= 'healthyandnatural221@gmail.com'
app.config['MAIL_PASSWORD']= 'ncub yqns lbzc oqmf'

mail = Mail(app)



@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/a_propos')
def info():
    return render_template('a_propos.html')

@app.route('/alimentaire')
def alimentaire():
    return render_template('alimentaire.html')

@app.route('/cosmétique')
def cosmetique():
    return render_template('cosmétique.html')

@app.route('/recettes')
def recettes():
    return render_template('recettes.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        sujet = request.form.get('sujet')
        message = request.form.get('message')

        # Création et envoi de l'email
        msg = Message(
            subject= f"Nouveau message de {nom}-{sujet}",
            sender= 'healthyandnatural221@gmail.com',recipients= ['healthyandnatural221@gmail.com']     
        )
        msg.body= f"""
                Nom: {nom}
                Téléphone: {telephone}
                Email: {email}
                Objet: {sujet}
                Message: {message}"""
        mail.send(msg)
        return render_template('contact.html', success=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)