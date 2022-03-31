# 导入常用组件
import shutil
import sys
import os
import threading
import json

# 导入QT
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 导入flask
from flask import Flask, make_response, request
from flask_cors import CORS

# 导入放大器
import inference_realesrgan as realesrgan

# 设置任务栏图标
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

UPLOAD_FOLDER = os.getcwd() + '/BackEnd/cache/image'
MAGNIFIED_FOLDER = os.getcwd() + '/BackEnd/cache/result/'
# 打开后端端口
flask_app = Flask(__name__)

# 支持跨域访问
CORS(flask_app, supports_credentials=True)

# 用于接收上传文件数据,button事件


@flask_app.route('/action', methods=['POST'])
def chosen_file():
    global percentage
    # 预防NameError
    data_form = request.form["sendData"]
    if data_form:
        if not os.path.exists(MAGNIFIED_FOLDER):
            os.makedirs(MAGNIFIED_FOLDER)
        # 前端传来待处理文件列表
        file_list = json.loads(data_form).get("_value")
        # 文件列表长度
        file_list_length = len(file_list)
        # 每处理完一个文件，进度条前进数量
        each_percentage = 80 / file_list_length
        for each_file in file_list:
            file_name = os.path.join(UPLOAD_FOLDER, each_file.get("name"))
            # 设置多线程，防止与主界面相互干扰
            magnifier = threading.Thread(
                target=image_magnifier, args=(file_name, each_percentage, ))
            # 设置守护线程，使端口随系统关闭
            magnifier.setDaemon(True)
            # 启动线程
            magnifier.start()
    return "For Get Chosen File!"

# 用于接收上传文件数据,upload事件


@flask_app.route('/upload', methods=['POST'])
def upload_file():
    global percentage
    percentage = 20
    # 预防NameError
    files = request.files.getlist("files")
    if files:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        for each_file in files:
            each_file.save(os.path.join(UPLOAD_FOLDER, each_file.filename))
    return "For Upload!"

# 前端获取后端处理状态


@flask_app.route('/state', methods=['GET'])
def get_percentage():
    global percentage
    # 防止进度条溢出
    if percentage > 100:
        percentage = 100
    return str(int(percentage))

# 前端显示图片


@flask_app.route('/cache/result/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'/cache/result/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response

# flask活动的多线程


def flask_thread():
    flask_app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)

# 清理cache的多线程


def clear_cache_thread():
    cache_file_path = os.getcwd() + "/BackEnd/cache/image/"
    cache_result_path = os.getcwd() + "/BackEnd/cache/result/"
    if os.path.exists(cache_file_path):
        shutil.rmtree(cache_file_path)
    if os.path.exists(cache_result_path):
        shutil.rmtree(cache_result_path)


def image_magnifier(file_name, each_percentage):
    global percentage
    parser = {
        'input_file_path': file_name,
        'output_file_path': MAGNIFIED_FOLDER,
        'model_name': 'RealESRGAN_x4plus',
        'face_enhance': False,
        'half': True,
        'extension': 'auto'
    }
    realesrgan.prepare_model(parser)
    percentage += each_percentage


class MainWindow(QMainWindow):

    def __init__(self):
        # 对继承自父类的属性进行初始化
        super(MainWindow, self).__init__()
        # 用父类的初始化方法来初始化继承的属性
        self.browser = QWebEngineView()
        self.initUI()

    def initUI(self):
        # 将窗口设置为动图大小
        self.resize(1680, 1050)
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.4)
        # 获取相对路径
        url = "http://localhost:3000/"
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

        # 添加窗口标题
        self.setWindowTitle("图片智能放大App")
        self.setWindowIcon(QIcon(os.getcwd() + "/BackEnd/logo.ico"))
        # icon = QIcon().addPixmap(QPixmap(os.getcwd() + "/BackEnd/logo.ico"), QIcon.Normal, QIcon.Off)
        # self.setWindowIcon(icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainWin = MainWindow()
    mainWin.setMinimumSize(1680, 1050)
    # 显示
    mainWin.show()
    # 在线程中清除缓存
    clear_cache = threading.Thread(target=clear_cache_thread)
    clear_cache.start()
    # 设置多线程，防止与主界面相互干扰
    upload_thread = threading.Thread(target=flask_thread)
    # 设置守护线程，使端口随系统关闭
    upload_thread.setDaemon(True)
    # 启动线程
    upload_thread.start()
    # 主循环
    sys.exit(app.exec_())
