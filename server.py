# -*- coding: utf-8 -*-
import io
import oss2
import json
import xmlrpc.client
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  file_object = io.open('index.html','r', encoding='UTF-8')
  return file_object.read()

@app.route('/control')
def control():
  file_object = io.open('control.html','r', encoding='UTF-8')
  return file_object.read()

# 登录服务器获取服务器信息
@app.route('/getState/<ip>/<port>/<username>/<password>')
def getState(ip, port, username, password):
  server = xmlrpc.client.Server('http://' + username + ':' + password + '@' + ip + ':' + port +'/RPC2')
  return json.dumps(server.supervisor.getState())

@app.route('/getAllProcessInfo/<ip>/<port>/<username>/<password>')
def getAllProcessInfo(ip, port, username, password):
  server = xmlrpc.client.Server('http://' + username + ':' + password + '@' + ip + ':' + port +'/RPC2')
  return json.dumps(server.supervisor.getAllProcessInfo())

@app.route('/stopProcess/<ip>/<port>/<username>/<password>/<name>')
def stopProcess(ip, port, username, password, name):
  server = xmlrpc.client.Server('http://' + username + ':' + password + '@' + ip + ':' + port +'/RPC2')
  return json.dumps(server.supervisor.stopProcess(name, True))

@app.route('/startProcess/<ip>/<port>/<username>/<password>/<name>')
def startProcess(ip, port, username, password, name):
  server = xmlrpc.client.Server('http://' + username + ':' + password + '@' + ip + ':' + port +'/RPC2')
  return json.dumps(server.supervisor.startProcess(name, True))

if __name__ == '__main__':
  print('程序正在监听5001端口!')
  app.run(host='0.0.0.0', port=5001)