from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS
import pandas as pd

# 세션에 저장하긴 힘들어보임

app = Flask(__name__, template_folder='.') # 서버 생성

CORS(app) 
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'alsdkfjlasjfkl'

@app.route('/api/upload', methods=['POST'])
def index_router():
  upload_file = request.files['file']
  df = pd.read_csv(upload_file)
  # print(request.files)
  # print(session['upload'])
  # session['upload'] = True
  # session['file'] = df.to_dict('list')
  # f.save()
  return jsonify({
    "file": {
      
    },
    "valid": True
  })

@app.route('/api/test', methods=['GET'])
def test_router():
  # return render_template('index.html')
  print(pd.DataFrame(session['file']))
  return jsonify({
    "chart": {
      "title": "비속어 사용",
      "labels": ["나영채", "신재규", "이운호"],
      "data": [10, 20, 30]
    }
  })

# app.run(host='0.0.0.0', debug=True, port=3000)
app.run(host='127.0.0.1', debug=True, port=3000)