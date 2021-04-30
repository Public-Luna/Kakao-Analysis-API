from flask import Flask, jsonify, render_template # Flask = 메인, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='.') # 서버 생성

# run_with_ngrok(app) # 서버 우회 개방
CORS(app) # cross origin resource share ! 개방
app.config['JSON_AS_ASCII'] = False

# [GET/POST]/PUT/DELETE
# decorater AOP, DI
@app.route('/api/test', methods=['GET'])
def index_router():
  # return render_template('index.html')
  return jsonify({
    "chart": {
      "title": "비속어 사용",
      "labels": ["나영채", "신재규", "이운호"],
      "data": [10, 20, 30]
    }
  })
@app.route('/api/upload', methods=['POST'])
def upload_router():
  my_res.headers["Access-Control-Allow-Origin"] = "*"
  # return render_template('index.html')
  return jsonify({
    "file": {
      
    },
    "valid": true
  })


# app.run(host='0.0.0.0', debug=True, port=3000)
app.run(host='127.0.0.1', debug=True, port=3000)