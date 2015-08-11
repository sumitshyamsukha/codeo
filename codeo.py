#!/usr/bin/python3
import subprocess
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    languages = {'python':'.py', 'python3':'.py', 'java':'.java', 'c_cpp':'.cpp'}
    code, inputText, lang = request.json['text'], request.json['input'], request.json['language']

    if lang == 'java' and os.path.isfile('Main.class'):
        os.remove('Main.class')

    fileName = 'Main' + languages[lang]
    file = open(fileName, "w")
    file.write(code)
    file.close()


    output = None
    if lang == 'java':
        compile = subprocess.Popen(["javac", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["java", "Main"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())
    elif lang == 'python' or lang=='python3':
        output = subprocess.Popen([lang, fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())
    else:
        compile = subprocess.Popen(["g++", fileName], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = subprocess.Popen(["./a.out"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=inputText.encode())

    fix = output[0].decode('ascii')
    err = output[1].decode('ascii')
    o = {'param': 'out', 'val': fix}
    e = {'param': 'err', 'val': err}

    
    if fix is not None and fix!='':
        return jsonify(o)
    else:
        return jsonify(e)


if __name__ == '__main__':
    app.run(debug=True)
