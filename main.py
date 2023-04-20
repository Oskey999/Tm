from flask import Flask, render_template
#https://pythonprogramming.net/sockets-tutorial-python-3/
import socket





app = Flask(__name__)
@app.route('/')
# def home():
#     return render_template("index.html")

def hello_world():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    msg = s.recv(1024)
    msg.decode("utf-8")
    return msg