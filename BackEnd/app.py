from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# 解决跨域问题
CORS(app, supports_credentials=True)

@app.route("/action", methods=['POST'])
def for_action():
    return "<p>For Action!</p>"
