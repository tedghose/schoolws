import flask
import os
from flask import Flask
#from flask.ext.session import Session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    print(flask.request.data)
    if not flask.session.get('logged_in'):
        #return flask.render_template('static/login.html')
        return flask.redirect("dir/login.html", code=302)
    else:
        return "Hello from Cisco"

@app.route('/login', methods=['POST'])
def do_admin_login():
    print(flask.request.form)
    if flask.request.form['p'] == 'password' and flask.request.form['u'] == 'admin':
        flask.session['logged_in'] = True
    else:
        flask.flash('wrong password!')
    return hello()

@app.route('/dir/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
    print('>>> Path: '+path)
    if not os.path.isfile(os.path.join('static', path)):
        path = os.path.join('static', 'index.html')
    return flask.send_from_directory('static', path)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess = flask.session
    #sess.init_app(app)

    app.debug = True
    app.run()
