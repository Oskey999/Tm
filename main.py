#from flask import Flask, render_template
#https://pythonprogramming.net/sockets-tutorial-python-3/
import socket 

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(2)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))



# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template("index.html")

# def hello_world():
#     return 'Hello world!'