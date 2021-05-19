from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='.') # 서버 생성

CORS(app) 
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'alsdkfjlasjfkl'

@app.route('/api/upload', methods=['POST'])
def index_router():
  upload_file = request.files['file']
  df = pd.read_csv(upload_file)
  file_key = str(uuid.uuid1())
  
  df.to_csv(os.path.join('store', file_key+'.csv'))

  return jsonify({
    "file": {
      'file_key': file_key
    },
    "valid": True
  })

@app.route('/api/test', methods=['GET'])
def test_router():
  # return render_template('index.html')
  if 'file_key' in request.args:
    file_key = request.args['file_key']
    print(pd.read_csv(os.path.join('store', file_key+'.csv')))

  # 데이터를 분석한 코드

  return jsonify({
    "chart": {
      "title": "비속어 사용",
      "labels": ["나영채", "신재규", "이운호"],
      "data": [10, 20, 30]
    }
  })

# app.run(host='0.0.0.0', debug=True, port=3000)
app.run(host='127.0.0.1', debug=True, port=3000)