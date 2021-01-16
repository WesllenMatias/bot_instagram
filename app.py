from instabot import *
import config
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agendador.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contas(db.Model):

    __tabname__='contas'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    conta = db.Column(db.String)
    usuario = db.Column(db.String)
    passwd = db.Column(db.String)

    def __init__(self,conta,usuario,passwd):
        self.conta = conta
        self.usuario = usuario
        self.passwd = passwd

class Postagem():

    __tabname__='postagem'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    data_post = db.Column(db.Date)
    hora_post = db.Column(db.Time)
    legenda = db.Column(db.String)
    titulo = db.Column(db.String)

    def __init__(self,data_post,hora_post,legenda,titulo):
        self.data_post = data_post
        self.hora_post = hora_post
        self.legenda = legenda
        self.titulo = titulo

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contas')
def contas():
    return render_template('contas.html')

@app.route('/postagem')
def postagem():
    return render_template('postagem.html')

@app.route("/get_contas",methods=['GET','POST'])
def get_contas():
    if request.method == "POST":
        conta = request.form.get("conta")
        usuario = request.form.get("usuario")
        passwd = request.form.get("passwd")

        if conta and usuario and passwd:
            g_contas = Contas(conta,usuario,passwd)
            db.session.add(g_contas)
            db.session.commit()
    
    return redirect("/")

@app.route("/get_postagem",methods=['GET','POST'])
def get_postagem():
    if request.method == "POST":
        data_post = request.form.get("data_post")
        hora_post = request.form.get("hora_post")
        legenda = request.form.get("legenda")
        titulo = request.form.get("titulo")

        if data_post and hora_post and legenda and titulo:
            g_postagem = Postagem(data_post,hora_post,legenda,titulo)
            db.session.add(g_postagem)
            db.session.commit()

    return redirect("/")

    

if __name__ == "__main__":
    app.run(debug=True)