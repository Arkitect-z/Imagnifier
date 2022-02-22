import sys
import os
import threading

from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtGui import QIcon
# 导入QT
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

from flask import Flask, request
from flask_cors import CORS

# 打开后端端口
flask_app = Flask(__name__)
# 解决跨域问题
CORS(flask_app, supports_credentials=True)

# 用于图片上传时返回200
@flask_app.route("/action", methods=['POST'])
def for_action():
    return "<p>For Action!</p>"

# 用于接收上传文件数据
@flask_app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./test.png')

def flask_thread():
    flask_app.run(debug=False, host='127.0.0.1', port=5000)

# 使用pyqt5多线程来显示页面
class LoadWeb(QThread):
    def __init__(self):
        super(LoadWeb, self).__init__()

    def run(self):
        print("use thread")


class MainWindow(QMainWindow):

    def __init__(self):
        # 对继承自父类的属性进行初始化
        super(MainWindow, self).__init__()
        # 用父类的初始化方法来初始化继承的属性
        self.browser = QWebEngineView()
        self.initUI()

    def initUI(self):
        # 将窗口设置为动图大小
        self.resize(1440, 900)
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.3)
        # 获取相对路径
        url = "http://localhost:3000/"
        # url = os.path.abspath(os.path.dirname(os.getcwd())) + '/Web/index.html'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

        # 添加窗口标题
        self.setWindowTitle("图片放大App")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/icon.ico"))
    # 创建一个主窗口
    mainWin = MainWindow()
    mainWin.setMinimumSize(1440, 900)
    # 显示
    mainWin.show()
    # 设置多线程，防止与主界面相互干扰
    upload_thread = threading.Thread(target=flask_thread)
    # 设置守护线程，使端口随系统关闭
    upload_thread.setDaemon(True)
    # 启动线程
    upload_thread.start()
    # 主循环
    sys.exit(app.exec_())