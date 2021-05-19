from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='.') # 서버 생성

CORS(app) 
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'alsdkfjlasjfkl'

# 로그파일 업로드
# 로그파일을 업로드하고 store폴더에 키로 저장한다.
# 수정방향 양방향 암호화가 가능하게 만들며 암호화 키를 유저쿠키에 가지고 있게 한다. (아직 개발되지 않음)
# 이후 해당 키를 이용한 요청은 해당 파일을 업로드한 유저로 간주하여 pandas를 이용한다.
# 서버에 저장되지 않으니 안정성이 보장된다 -> 더 재대로 하기위해선 JWT를 이용하는 방법도 있지만 가볍게 만드려고 한다.
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

# 테스팅
# 해당 파일 키를 이용하여 pandas객체를 가져오는 것이 가능한지 테스트 해보았다.
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