import os
import sys
import pandas as pd
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMenu, QMenuBar, QFileDialog, QColorDialog
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QDesktopWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QVBoxLayout, QHBoxLayout, QGraphicsView, QGraphicsScene, \
    QPushButton, QMenu, QAction
from PyQt5.QtWidgets import QVBoxLayout, QSpacerItem
from PyQt5.QtCore import QByteArray, QBuffer
import tempfile
from PyQt5.QtGui import QPainter



class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口大小窗口标题
        self.setWindowTitle("牌位打印")
        self.setGeometry(0, 0, 1600, 900)

        # 计算窗口位置
        screen_geometry = QDesktopWidget().screenGeometry()
        x = int((screen_geometry.width() - self.width()) / 2)
        y = int((screen_geometry.height() - self.height()) / 2)
        self.move(x, y)

        self.horizontal_layout = QHBoxLayout()
        self.default_bg_color = "#FAF9DE"  # 秋麒麟
        self.setStyleSheet(f"background-color: {self.default_bg_color};")

        # 设置窗口图标
        root_dir = os.path.dirname(os.path.abspath(__file__))  # 获取程序根目录
        icon_path = os.path.join(root_dir, "logo.ico")  # 构建图标文件路径
        self.setWindowIcon(QIcon(icon_path))
        
        # 创建中心窗口
        self.center_widget = QWidget(self)
        self.setCentralWidget(self.center_widget)
        self.vertical_layout = QVBoxLayout(self.center_widget)
        
        # 创建背景图像组件
        self.background_view = QGraphicsView(self.center_widget)
        self.background_view.setGeometry(0, 0, self.width(), self.height())
        self.background_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.background_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.background_view.setRenderHint(QPainter.SmoothPixmapTransform)
        self.background_view.setRenderHint(QPainter.Antialiasing)
        self.background_view.setRenderHint(QPainter.HighQualityAntialiasing)
        self.background_view.setRenderHint(QPainter.TextAntialiasing)
        
        self.background_scene = QGraphicsScene(self.background_view)
        self.background_view.setScene(self.background_scene)

        # 创建画布组件
        self.canvas = QGraphicsView(self)
        self.canvas.setStyleSheet(f"background-color: {self.default_bg_color};")
        self.scene = QGraphicsScene()
        self.canvas.setScene(self.scene)
        self.canvas.setFixedSize(800, 600)  # 调整大小
        self.horizontal_layout.addWidget(self.canvas)
        self.vertical_layout.addLayout(self.horizontal_layout)

        # 在这里添加代码以加载图像
        desired_size = (50, 50)

        self.image1 = QPixmap("icons/icon1.png")
        self.image1 = self.image1.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image2 = QPixmap("icons/icon2.png")
        self.image2 = self.image2.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image3 = QPixmap("icons/icon3.png")
        self.image3 = self.image3.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image4 = QPixmap("icons/icon4.png")
        self.image4 = self.image4.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image5 = QPixmap("icons/icon5.png")
        self.image5 = self.image5.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image6 = QPixmap("icons/icon6.png")
        self.image6 = self.image6.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image7 = QPixmap("icons/icon7.png")
        self.image7 = self.image7.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image8 = QPixmap("icons/icon8.png")
        self.image8 = self.image8.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image9 = QPixmap("icons/icon9.png")
        self.image9 = self.image9.scaled(*desired_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # 创建自定义按钮样式
        self.my_button = QPushButton("My Button", self)
        self.my_button.setStyleSheet("background-color: #009900;"
                                     "color: #F5DE83;"
                                     "border: 30px solid #F5DE83;"
                                     "padding: 50px 50px;"
                                     "font-size: 24px;"
                                     "icon-size: 64px;")
        
        # 创建导航菜单栏
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("background-color: %s;" % self.default_bg_color)  # 设置导航菜单栏背景颜色
        self.menu_bar.setFont(QFont("宋体", 8))
        
        # 添加菜单栏
        self.setMenuBar(self.menu_bar)
        
        # 创建菜单
        menu_bar = self.menuBar()
        self.menu_bar.setFont(QFont("宋体", 16))
        
        # 添加一个空白菜单项，设为不可用状态
        self.blank_menu = QMenu("", self.menu_bar)
        self.blank_menu.setEnabled(False)
        self.menu_bar.addMenu(self.blank_menu)
        
        # 添加版本信息
        version_menu = QMenu(self.menu_bar)
        version_label = QLabel("版本号v 1.0   版权：QingShan+Chatgtp", version_menu)
        version_label.setStyleSheet("font-size: 12px;")
        version_layout = QHBoxLayout(version_menu)
        version_layout.setContentsMargins(0, 0, 0, 0)
        version_layout.addWidget(version_label, alignment=Qt.AlignRight)
        self.menu_bar.addMenu(version_menu)
        
        # 创建主题菜单
        self.theme_menu = QMenu("主题", self.menu_bar)
        theme_action = self.create_theme_action()
        self.theme_menu.addAction(theme_action)
        
        # 添加主题菜单到菜单栏
        self.menu_bar.addMenu(self.theme_menu)
        
        # 创建文件菜单
        self.file_menu = QMenu("文件", self.menu_bar)
        self.file_menu.setIcon(QIcon(self.image2))
        
        # 在这里添加文件的操作
        open_action = QAction("打开", self)
        open_action.triggered.connect(self.open_file)
        self.file_menu.addAction(open_action)
        
        # 添加文件到菜单栏
        self.menu_bar.addMenu(self.file_menu)
        
        # 创建牌位菜单
        self.plaque_menu = QMenu("牌位", self.menu_bar)
        self.plaque_menu.setIcon(QIcon(self.image3))
        
        # 添加牌位到菜单栏
        self.menu_bar.addMenu(self.plaque_menu)
        
        # 创建排版菜单
        self.layout_menu = QMenu("排版", self.menu_bar)
        self.layout_menu.setIcon(QIcon(self.image4))
        
        # 添加排版到菜单栏
        self.menu_bar.addMenu(self.layout_menu)
        
        # 创建打印机菜单
        self.print_menu = QMenu("打印机", self.menu_bar)
        self.print_menu.setIcon(QIcon(self.image5))
        
        # 添加主打印机到菜单栏
        self.menu_bar.addMenu(self.print_menu)
        
        # 创建查询菜单
        self.query_menu = QMenu("查询", self.menu_bar)
        self.query_menu.setIcon(QIcon(self.image6))
        
        # 添加查询到菜单栏
        self.menu_bar.addMenu(self.query_menu)
        
        # 创建数据库菜单
        self.database_menu = QMenu("数据库", self.menu_bar)
        self.database_menu.setIcon(QIcon(self.image7))
        
        # 添加数据库到菜单栏
        self.menu_bar.addMenu(self.database_menu)
        
        # 创建设置菜单
        self.settings_menu = QMenu("设置", self.menu_bar)
        self.settings_menu.setIcon(QIcon(self.image8))
        
        # 添加设置到菜单栏
        self.menu_bar.addMenu(self.settings_menu)
        
        # 创建更新菜单
        self.update_menu = QMenu("更新", self.menu_bar)
        self.update_menu.setIcon(QIcon(self.image9))
        
        # 添加更新到菜单栏
        self.menu_bar.addMenu(self.update_menu)
    
    def choose_image(self, file_path):
        # 使用QPixmap设置图像
        pixmap = QPixmap(file_path)
        self.background_image_item = QGraphicsPixmapItem(pixmap)
        self.background_scene.clear()
        self.background_scene.addItem(self.background_image_item)
    
    def choose_color(self, color):
        if color.isValid():
            self.default_bg_color = color.name()
            self.background_scene.clear()
            self.background_scene.setBackgroundBrush(QBrush(QColor(self.default_bg_color)))
    
    def create_theme_action(self):
        theme_action = QAction("主题", self)
        theme_action.setIcon(QIcon(self.image1))
        theme_action.triggered.connect(self.open_theme)
        return theme_action
    
    def center_window(self, window):
        screen_geometry = QDesktopWidget().screenGeometry()
        self.center_window(self)
    
        
    def change_background_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.gif)")

        if file_path:
            self.setStyleSheet(f"background-image: url({file_path}); background-repeat: no-repeat;")

    def change_background_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.default_bg_color = color.name()
            self.setStyleSheet(f"background-color: {self.default_bg_color};")
    
    def open_theme(self):
        self.theme_window = Theme(self, self)
        self.theme_window.show()
    
    def open_file(self):
        self.Layout_window = file(self)   # 将 self 作为参数传递
        self.Layout_window.show()
    
    def open_plaque(self):
        self.Layout_window = Layout(self)   # 将 self 作为参数传递
        self.Layout_window.show()
        
    def open_Layout(self):
        self.Layout_window = Layout(self)   # 将 self 作为参数传递
        self.Layout_window.show()

    def open_print(self):
        self.print_window = PrintConnector(self)   # 将 self 作为参数传递
        self.print_window.show()

    def open_query(self):
        self.query_button_window = Query(self)   # 将 self 作为参数传递
        self.query_button_window.show()

    def open_database(self):
        self.database_window = Database(self)   # 将 self 作为参数传递
        self.database_window.show()

    def open_Settings(self):
        self.Settings_window = Settings(self)   # 将 self 作为参数传递
        self.Settings_window.show()
 
    def check_for_update(self):
        # 创建更新窗口并显示
        self.update_window = Update(self)   # 将 self 作为参数传递
        self.update_window.show()


class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super(CustomButton, self).__init__(text, parent)
        
        # 设置自定义按钮样式
        font = QFont("宋体", 20, QFont.Bold)
        self.setFont(font)
        self.setFixedSize(200, 50)
        
        self.setAutoFillBackground(True)
        self.setPalette(self.create_palette())
        
        self.setStyleSheet("""
            CustomButton {
                background-color: #009900;
                color: #F5DE83;
                border: 2px solid #F5DE83;
                padding: 5px 6px;
            }
            CustomButton:pressed {
                background-color: #006600;
            }
        """)
    
    def create_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.Button, QColor("#009900"))
        palette.setColor(QPalette.ButtonText, QColor("#F5DE83"))
        return palette

class Theme(QWidget):
    def __init__(self, main_application, parent=None):
        super(Theme, self).__init__(parent)
        self.main_application = main_application
        self.setWindowTitle("主题设置")
        self.setGeometry(0, 0, 850, 700)

        # 创建布局
        self.layout = QVBoxLayout(self)

        # 创建按钮用于选择背景图片
        self.choose_image_button = QPushButton("选择图片", self)
        self.choose_image_button.clicked.connect(self.choose_image)

        # 创建按钮用于选择背景颜色
        self.choose_color_button = QPushButton("选择颜色", self)
        self.choose_color_button.clicked.connect(self.choose_color)

        # 添加占位符和按钮到布局
        self.layout.addItem(QSpacerItem(20, 100))
        self.layout.addWidget(self.choose_image_button)
        self.layout.addItem(QSpacerItem(20, 200))
        self.layout.addWidget(self.choose_color_button)
        self.layout.addItem(QSpacerItem(20, 100))
    
    def resize_image(image_path, target_width, target_height):
        original_image = QImage(image_path)
        resized_image = original_image.scaled(target_width, target_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return resized_image
    
    def apply_theme(self, style: str):
        self.main_application.setStyleSheet(style)
    
    def choose_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg *.gif)")
        if file_path:
            target_width = self.main_application.width()
            target_height = self.main_application.height()

            # 使用QPixmap对图像进行缩放
            pixmap = QPixmap(file_path)
            pixmap = QPixmap.fromImage(self.resize_image(file_path, target_width, target_height))

            # 将缩放后的图像保存到base64字符串中
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            pixmap.save(buffer, "PNG")
            base64_bytes = byte_array.toBase64()
            base64_str = str(base64_bytes, "utf-8")

            # 将缩放后的图像应用于样式表


    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.main_application.default_bg_color = color.name()
            self.main_application.choose_color(color)

        # 处理选择的图片路径，可以将图片路径保存到配置文件中

    def choose_color(self):
        color = QColorDialog.getColor()
        # 处理选择的颜色，可以将颜色保存到配置文件中
        
        # 在这里添加主题功能窗口的代码
    

class file(QWidget):
    def __init__(self, parent=None):
        super(file, self).__init__(parent)
        self.setWindowTitle("文件")
        self.setGeometry(0, 0, 850, 700)
        
        
        # 读取配置文件并获取文件路径
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.file_path = config.get('Paths', 'file_path', fallback='')
        
        # 创建按钮用于导入文件
        import_button = Button(self, text="导入文件", command=self.import_file)
        import_button.pack(pady=10)
        
        # 创建按钮用于预览数据
        preview_button = Button(self, text="预览数据", command=self.preview_data)
        preview_button.pack(pady=10)
        
        # 创建按钮用于打印数据
        print_button = Button(self, text="打印数据", command=self.print_data)
        print_button.pack(pady=10)
        
        # 创建按钮用于显示当前文件路径
        self.file_path_label = Label(self, text=self.file_path)
        self.file_path_label.pack(pady=10)
        
        # 创建一个新的按钮，用于列名转换
        rename_columns_button = Button(self, text="列名转换", command=self.rename_columns)
        rename_columns_button.pack(pady=10)
        
        # 创建按钮用于退出窗口
        exit_button = Button(self, text="退出", command=self.destroy)
        exit_button.pack(pady=10)
        
    def open_file_dialog(self):
        # 打开文件对话框，选择要导入的文件
        file_path = filedialog.askopenfilename()
        if file_path:
            # 读取文件，并将其转换为 Pandas DataFrame 格式
            self.data = pd.read_csv(file_path)
            # 在控制台输出数据预览信息
            print(self.data.head())
    
    def preview_data(self):
        # 创建新的窗口，用于展示预览数据的表格
        preview_window = tk.Toplevel(self.parent)
        preview_window.title("数据预览")
        
        # 创建 Pandas DataFrame 对象的表格，并将其添加到窗口中
        table = tk.Frame(preview_window)
        table.pack()
        
        # 添加表头
        headers = list(self.data.columns)
        for j, header in enumerate(headers):
            header_label = tk.Label(table, text=header, font=('Arial', 12, 'bold'))
            header_label.grid(row=0, column=j, padx=10, pady=5)
        
        # 添加表格数据
        for i, row in self.data.iterrows():
            for j, header in enumerate(headers):
                value = row[header]
                value_label = tk.Label(table, text=value)
                value_label.grid(row=i + 1, column=j, padx=10, pady=5)
        
        # 实例化排版类
        layout = YourLayoutClass()
    
        # 调用排版模块的预览功能
        all_names = []  # 这里添加你需要传递给排版模块的所有名字
        # ...
        preview_content = layout.preview_function(all_names)  # 使用排版模块的预览功能生成预览内容
    
        # 在预览窗口中显示预览内容
        preview_label = tk.Label(preview_window, text=preview_content, justify="left")
        preview_label.pack(pady=10)
    
        # 添加确认和取消按钮
        confirm_button = tk.Button(preview_window, text="确认", command=self.confirm_preview)
        confirm_button.pack(pady=10)
    
        cancel_button = tk.Button(preview_window, text="取消", command=preview_window.destroy)
        cancel_button.pack(pady=10)
    
    def import_file(self):
        self.open_file_dialog()  # 添加这一行
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            
            # 根据文件类型读取数据
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                self.data = pd.read_json(file_path)
            else:
                raise ValueError('Unsupported file format')
            
            # 列名转换
            column_map = {
                'file1': {'祈福人': 'name', '地址': 'address'},
                'file2': {'往生人': 'name1', '阳上人': 'name2', '地址': 'address'},
                'file3': {'祈福人': 'name', '地址': 'address'}
            }
            column_map = { }
            
            self.data = self.data.rename(columns=column_map)
            
            # 数据转换
            self.data = self._data_transform(self.data)
            
            # 数据验证
            if not self._data_validation(self.data):
                raise Exception('Data validation failed.')
        
    def _data_validation(self, data):
        """
            数据验证，验证数据是否符合要求
            :param data: 待验证的数据
            :return: 是否通过验证
            """
        # 进行数据验证操作，如验证数据是否缺失、是否符合数值范围等
        # 验证数据是否存在缺失值
        if data.isnull().sum().sum() > 0:
            print('存在缺失值')
            return False
            # 验证数据是否符合数值范围
            if (data['sales'] < 0).any():
                print('表格内容和模板匹配不上')
                return False
            return True
        
    
    def rename_columns(self):
        # 执行列名转换等操作
        # ...
        pass
    
    def print_data(self):
        # 打印数据
        if self.data is not None:
            # 实例化 PrintConnector 对象并调用打印方法
            pc = PrintConnector()
            pc.print_data(self.data)
        else:
            print("没有数据可以打印！")
    # 在这里添加文件功能窗口的代码
    
class plaque(QWidget):
    def __init__(self, parent=None):
        super(plaque, self).__init__(parent)
        self.setWindowTitle("牌位输入")
        self.setGeometry(0, 0, 850, 700)
        
        # 创建保存按钮
        save_button = QPushButton("保存", self)
        save_button.clicked.connect(self.plaque_function)
        self.vertical_layout.addWidget(save_button)
    
    # 在这里添加牌位功能窗口的代码
    
    def plaque_function(self):
        # 在这里添加保存功能的代码
        pass
    
    def print_data(self):
        # 连接打印机
        printer = Print()
        printer.connect()
        
        # 打印数据
        printer.print_data(data)
        
        
        # 断开连接
        printer.disconnect()

class Layout(QWidget):
    def __init__(self, parent=None):
        super(Layout, self).__init__(parent)
        self.setWindowTitle("排版设计")
        self.setGeometry(0, 0, 850, 700)

        # 在这里添加排版布局功能窗口的代码

class PrintConnector(QWidget):
    def __init__(self, parent=None):
        super(PrintConnector, self).__init__(parent)
        self.setWindowTitle("打印机列表")
        self.setGeometry(0, 0, 850, 700)

        # 在这里添加打印机窗口的代码

class Query(QWidget):
    def __init__(self, parent=None):
        super(Query, self).__init__(parent)
        self.setWindowTitle("信息查询")
        self.setGeometry(0, 0, 850, 700)

        # 在这里添加查询窗口的代码

class Database(QWidget):
    def __init__(self, parent=None):
        super(Database, self).__init__(parent)
        self.setWindowTitle("数据库")
        self.setGeometry(0, 0, 850, 700)

        # 在这里添加数据库窗口的代码

class Settings(QWidget):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.setWindowTitle("基本设置")
        self.setGeometry(0, 0, 850, 700)

        # 在这里添加设置窗口的代码

        # 创建布局
        layout = QVBoxLayout()

        # 创建保存按钮
        save_button = QPushButton("保存", self)
        layout.addWidget(save_button)

        # 创建关闭按钮
        close_button = QPushButton("关闭", self)
        layout.addWidget(close_button)

        self.setLayout(layout)
    
    def save_settings(self):
        # 在这里添加保存设置的逻辑
        pass
    
class update(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("自动更新")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        self.resizable(False, False)
        self.should_update = False  # 初始化 should_update 属性为 False
        parent.center_window(self)  # 添加这一行
        message = tk.Label(self,
                           text=f"A new version ({new_version}) is available. Do you want to download and install it?")
        message.pack(pady=20)

        # 创建两个按钮，一个用于下载更新，一个用于取消更新
        download_button = tk.Button(self, text="Download and Install", command=self.on_download_and_install, width=20,
                                    height=2, bg="red")
        
        download_button.pack(side="left", padx=20, pady=20)

        cancel_button = tk.Button(self, text="Cancel", command=self.on_cancel, width=20, height=2)
        cancel_button.pack(side="right", padx=20, pady=20)
    
    def on_download_and_install(self):
        self.should_update = True  # 用户选择更新
        self.destroy()
    
    def on_cancel(self):
        self.should_update = False  # 用户取消更新
        self.destroy()
    
    def download_and_install_update(self):
        self.destroy()
        updater_module = AutoUpdater('1.0.0')
        updater_module.download_update()
        updater_module.install_update()
    
    # 在这里添加更新窗口的代码

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建 QApplication 实例
    main_window = MainApplication()  # 创建程序主窗口
    main_window.show()  # 显示主窗口
    sys.exit(app.exec_())  # 运行应用程序，并等待退出

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
