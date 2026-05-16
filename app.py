import flask
from flask import session
import database
from flask import  render_template

app = flask.Flask(__name__)
app.secret_key = "sessão-teste"
database.criar_tabela()

@app.route('/')
def index():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if flask.request.method == "POST":
        nome = flask.request.form.get("nome")
        email = flask.request.form.get("email")
        senha = flask.request.form.get("senha")
        cargo = flask.request.form.get("cargo")
        database.cadastrar_usuario(nome, email ,senha, cargo)
        return flask.redirect("/login")
    return flask.render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        senha = flask.request.form.get("senha")
        usuario = database.verificar_login(email, senha)
        if usuario:
            session['id'] = usuario[0]
            session['nome'] = usuario[1]
            session['cargo'] = usuario[4]
            return flask.redirect("/painel")
        return flask.render_template("login.html", erro="Email ou senha incorretos.")
    return flask.render_template("login.html")

@app.route("/painel")
def painel():
    if 'id' not in session:
        return flask.redirect("/login")
    return flask.render_template("painel.html", nome=session['nome'], cargo=session['cargo'])

@app.route("/logout")
def logout():
    session.clear()
    return flask.redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)