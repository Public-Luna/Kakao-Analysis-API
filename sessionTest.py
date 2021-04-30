from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, template_folder='.') # 서버 생성

CORS(app) 
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'alsdkfjlasjfkl'

@app.route('/api/upload', methods=['POST'])
def index_router():
  upload_file = request.files['file']
  print(pd.read_csv(upload_file))
  
  # print(request.files)
  # print(session['upload'])
  # session['upload'] = True
  # session['file'] = request.data
  return 'OK'

# app.run(host='0.0.0.0', debug=True, port=3000)
app.run(host='127.0.0.1', debug=True, port=3000)