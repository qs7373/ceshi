import os
import sys

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QWidget, QStackedWidget
from PyQt5.QtCore import QObject, pyqtSignal

class Ui_MainWindow(object):
    def __init__(self):
        # 主界面初始化
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # 一级菜单栏初始化
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_8 = QtWidgets.QMenu(self.menubar)
        self.menu_9 = QtWidgets.QMenu(self.menubar)
        # 二级菜单栏初始化
        self.actionRGB_histogram = QtWidgets.QAction(MainWindow)
        self.action = QtWidgets.QAction(MainWindow)
        self.actionDAISY = QtWidgets.QAction(MainWindow)
        self.actionEHD = QtWidgets.QAction(MainWindow)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.actionVGG = QtWidgets.QAction(MainWindow)
        self.actionResNet = QtWidgets.QAction(MainWindow)
        # 界面布局
        self.Layout = QVBoxLayout(self.centralwidget)  # 垂直布局
        # stackedWidget初始化
        self.stackedWidget = QStackedWidget()
        
        # 在这里添加代码以加载图像
        desired_size = (60, 60)
        self.icon1 = QIcon("icons/icon1.png")
        self.icon2 = QIcon("icons/icon2.png")
        self.icon3 = QIcon("icons/icon3.png")
        self.icon4 = QIcon("icons/icon4.png")
        self.icon5 = QIcon("icons/icon5.png")
        self.icon6 = QIcon("icons/icon6.png")
        self.icon7 = QIcon("icons/icon7.png")
        self.icon8 = QIcon("icons/icon8.png")
        self.icon9 = QIcon("icons/icon9.png")
    
    def setupUi(self, MainWindow):
        # 创建界面
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 873)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 初始化图标
        self.icon1 = QtGui.QIcon("icons/icon1.png")
        self.icon2 = QtGui.QIcon("icons/icon2.png")
        self.icon3 = QtGui.QIcon("icons/icon3.png")
        self.icon4 = QtGui.QIcon("icons/icon4.png")
        self.icon5 = QtGui.QIcon("icons/icon5.png")
        self.icon6 = QtGui.QIcon("icons/icon6.png")
        self.icon7 = QtGui.QIcon("icons/icon7.png")
        self.icon8 = QtGui.QIcon("icons/icon8.png")
        self.icon9 = QtGui.QIcon("icons/icon9.png")
        
        # 设置一级菜单栏
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 80))
        self.menubar.setFixedHeight(40)
        self.menubar.setObjectName("menubar")
        
        stylesheet = '''
        QMenuBar::item {
            background-color: #F0F0F0;
            border: 1px solid #C0C0C0;
            border-radius: 5px;
            padding: 15px;
        }
        QMenuBar::item:selected {
            background-color: #C0C0C0;
            border-color: #808080;
            border-radius: 3px;
        }
        QMenuBar::item:separator {
            width: 10px;
        }
        '''
        
        # 使用样式表设置菜单栏样式
        self.menubar.setStyleSheet(stylesheet)
        
        # 创建一级菜单
        self.menu = self.createMenu("主题", self.icon1, "主题")
        self.menu_2 = self.createMenu("文件", self.icon2, "文件")
        self.menu_3 = self.createMenu("牌位", self.icon3, "牌位")
        self.menu_4 = self.createMenu("排版", self.icon4, "排版")
        self.menu_5 = self.createMenu("排版", self.icon5, "排版")
        self.menu_6 = self.createMenu("查询", self.icon6, "查询")
        self.menu_7 = self.createMenu("数据库", self.icon7, "数据库")
        self.menu_8 = self.createMenu("设置", self.icon8, "设置")
        self.menu_9 = self.createMenu("更新", self.icon9, "更新")
        
        # 将菜单添加到菜单栏
        self.menubar.addMenu(self.menu)
        self.menubar.addMenu(self.menu_2)
        self.menubar.addMenu(self.menu_3)
        self.menubar.addMenu(self.menu_4)
        self.menubar.addMenu(self.menu_5)
        self.menubar.addMenu(self.menu_6)
        self.menubar.addMenu(self.menu_7)
        self.menubar.addMenu(self.menu_8)
        self.menubar.addMenu(self.menu_9)
        
        # 创建QToolBar用于自定义菜单布局
        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setObjectName("toolbar")
        self.toolbar.setVisible(False)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        
        MainWindow.setMenuBar(self.menubar)
        # 设置菜单项之间的间隔
        self.menubar.setStyleSheet("QMenu::item { spacing: 100px; }")
        
        # 二级菜单栏布置
        self.actionRGB_histogram.setObjectName("actionRGB_histogram")
        self.action.setObjectName("action")
        self.actionDAISY.setObjectName("actionDAISY")
        self.actionEHD.setObjectName("actionEHD")
        self.action_2.setObjectName("action_2")
        self.actionVGG.setObjectName("actionVGG")
        self.actionResNet.setObjectName("actionResNet")
        self.menu.addAction(self.actionRGB_histogram)
        self.menu_2.addAction(self.action)
        self.menu_3.addAction(self.actionDAISY)
        self.menu_3.addAction(self.actionEHD)
        self.menu_3.addAction(self.action_2)
        self.menu_4.addAction(self.actionVGG)
        self.menu_4.addAction(self.actionResNet)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())
        
        # 布局添加stackedWidget控件
        self.Layout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        # 设置主界面面板：
        self.form = QWidget()
        self.formLayout = QHBoxLayout(self.form)  # 水平布局
        self.label0 = QLabel()
        self.label0.setText("欢迎使用寺院牌位打印系统！")
        self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label0.setAlignment(Qt.AlignCenter)
        self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
        self.label0.setStyleSheet("color: black; background-color: #D2B48C;")
        self.formLayout.addWidget(self.label0)  # 添加控件

        # 设置第1个面板：
        self.form1 = QWidget()
        self.formLayout1 = QHBoxLayout(self.form1)  # 水平布局
        self.label1 = QLabel()
        self.label1.setText("主题")
        self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout1.addWidget(self.label1)

        # 设置第2个面板：
        self.form2 = QWidget()
        self.formLayout2 = QHBoxLayout(self.form2)
        self.label2 = QLabel()
        self.label2.setText("Gabor")
        self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout2.addWidget(self.label2)
        # 设置第3个面板：
        self.form3 = QWidget()
        self.formLayout3 = QHBoxLayout(self.form3)
        self.label3 = QLabel()
        self.label3.setText("DAISY")
        self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout3.addWidget(self.label3)
        # 设置第4个面板：
        self.form4 = QWidget()
        self.formLayout4 = QHBoxLayout(self.form4)
        self.label4 = QLabel()
        self.label4.setText("EHD")
        self.label4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout4.addWidget(self.label4)
        # 设置第5个面板：
        self.form5 = QWidget()
        self.formLayout5 = QHBoxLayout(self.form5)
        self.label5 = QLabel()
        self.label5.setText("HOG")
        self.label5.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout5.addWidget(self.label5)
        # 设置第6个面板：
        self.form6 = QWidget()
        self.formLayout6 = QHBoxLayout(self.form6)
        self.label6 = QLabel()
        self.label6.setText("VGG")
        self.label6.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label6.setAlignment(Qt.AlignCenter)
        self.label6.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout6.addWidget(self.label6)
        # 设置第7个面板：
        self.form7 = QWidget()
        self.formLayout7 = QHBoxLayout(self.form7)
        self.label7 = QLabel()
        self.label7.setText("ResNet")
        self.label7.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label7.setAlignment(Qt.AlignCenter)
        self.label7.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout7.addWidget(self.label7)
        # 设置第8个面板：
        self.form8 = QWidget()
        self.formLayout8 = QHBoxLayout(self.form8)
        self.label8 = QLabel()
        self.label8.setText("ResNet")
        self.label8.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label8.setAlignment(Qt.AlignCenter)
        self.label8.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout8.addWidget(self.label8)
        # 设置第9个面板：
        self.form9 = QWidget()
        self.formLayout9 = QHBoxLayout(self.form9)
        self.label9 = QLabel()
        self.label9.setText("ResNet")
        self.label9.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label9.setAlignment(Qt.AlignCenter)
        self.label9.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout9.addWidget(self.label9)
        # 这里可以设置其他面板
			
        # stackedWidget添加各种界面用于菜单切换
        self.stackedWidget.addWidget(self.form)
        self.stackedWidget.addWidget(self.form1)
        self.stackedWidget.addWidget(self.form2)
        self.stackedWidget.addWidget(self.form3)
        self.stackedWidget.addWidget(self.form4)
        self.stackedWidget.addWidget(self.form5)
        self.stackedWidget.addWidget(self.form6)
        self.stackedWidget.addWidget(self.form7)
        self.stackedWidget.addWidget(self.form8)
        self.stackedWidget.addWidget(self.form9)
		
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # 添加其他界面到stackedWidget
    
    # 添加一个辅助方法来创建带有自定义样式的菜单
    def createMenu(self, title, icon, text):
        menu = QtWidgets.QMenu(title, MainWindow)
        menu.setIcon(icon)
        menu.setTitle(text)
        return menu
     
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 窗口名称
        MainWindow.setWindowTitle(_translate("MainWindow", "牌位打印"))
        # 设置窗口图标
        root_dir = os.path.dirname(os.path.abspath(__file__))  # 获取程序根目录
        icon_path = os.path.join(root_dir, "logo.ico")  # 构建图标文件路径
        MainWindow.setWindowIcon(QIcon(icon_path))
        # 一级目录
        self.menu.setTitle(_translate("MainWindow", "主题"))
        self.menu_2.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "牌位"))
        self.menu_4.setTitle(_translate("MainWindow", "排版"))
        self.menu_5.setTitle(_translate("MainWindow", "排版"))
        self.menu_6.setTitle(_translate("MainWindow", "查询"))
        self.menu_7.setTitle(_translate("MainWindow", "数据库"))
        self.menu_8.setTitle(_translate("MainWindow", "设置"))
        self.menu_9.setTitle(_translate("MainWindow", "更新"))

        
        # 二级目录
        # 主题方法1：程序背景
        self.actionRGB_histogram.setText(_translate("MainWindow", "选择图片"))
        self.actionRGB_histogram.triggered.connect(self.gotoThemeWin)
        # 主题方法2：程序颜色
        self.actionRGB_histogram.setText(_translate("MainWindow", "选择颜色"))
        self.actionRGB_histogram.triggered.connect(self.gotoThemeWin)
        # 主题方法3：保存
        self.actionRGB_histogram.setText(_translate("MainWindow", "保存"))
        self.actionRGB_histogram.triggered.connect(self.gotoThemeWin)
        # 主题方法4：恢复默认
        self.actionRGB_histogram.setText(_translate("MainWindow", "恢复默认"))
        self.actionRGB_histogram.triggered.connect(self.gotoThemeWin)
        # Texture方法1：Gabor滤波
        self.action.setText(_translate("MainWindow", "Gabor 滤波"))
        self.action.triggered.connect(self.gotoTexWin)
        # shape方法1：DAISY算子
        self.actionDAISY.setText(_translate("MainWindow", "DAISY 算子"))
        self.actionDAISY.triggered.connect(self.gotoDaisyWin)
        # shape方法2：EHD
        self.actionEHD.setText(_translate("MainWindow", "边缘直方图描述符（EHD）"))
        self.actionEHD.triggered.connect(self.gotoEHDWin)
        # shape方法3：HOG
        self.action_2.setText(_translate("MainWindow", "方向梯度直方图（HOG）"))
        self.action_2.triggered.connect(self.gotoHOGWin)
        # deep-learning方法1：VGG
        self.actionVGG.setText(_translate("MainWindow", "VGG"))
        self.actionVGG.triggered.connect(self.gotoVGGWin)
        # deep-learning方法2：ResNet
        self.actionResNet.setText(_translate("MainWindow", "ResNet"))
        self.actionResNet.triggered.connect(self.gotoResWin)

        # 菜单栏触发每个界面调用函数
    def on_button1_clicked(self):
        QMessageBox.information(self.form1, "消息", "您点击了按钮！")
    def gotoThemeWin(self):
        self.stackedWidget.setCurrentIndex(1)
    def gotoTexWin(self):
        self.stackedWidget.setCurrentIndex(2)
    def gotoDaisyWin(self):
        self.stackedWidget.setCurrentIndex(3)
    def gotoEHDWin(self):
        self.stackedWidget.setCurrentIndex(4)
    def gotoHOGWin(self):
        self.stackedWidget.setCurrentIndex(5)
    def gotoVGGWin(self):
        self.stackedWidget.setCurrentIndex(6)
    def gotoResWin(self):
        self.stackedWidget.setCurrentIndex(7)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     MainWindow = QtWidgets.QMainWindow()
     ui = Ui_MainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     sys.exit(app.exec_())


