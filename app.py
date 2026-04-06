from flask import Flask,render_template

app = Flask(__name__)

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)