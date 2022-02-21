import sys
import os

from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtGui import QIcon
# 导入QT
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


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
    # 主循环
    sys.exit(app.exec_())