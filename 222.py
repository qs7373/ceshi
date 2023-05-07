from PIL import ImageTk
import os
import tkinter as tk
from tkinter import Canvas
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk

from PIL import Image


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("牌位打印")
        self.geometry("1600x900")
        
        self.default_bg_color = "#FAF9DE"  # 秋麒麟
        self.configure(bg=self.default_bg_color)
        
        # 构建图标文件路径
        root_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(root_dir, "logo.ico")
        
        # 打开并缩放图标文件
        img = Image.open(icon_path)
        img = img.resize((100, 100), resample=Image.LANCZOS)
        
        # 创建PhotoImage对象
        icon = ImageTk.PhotoImage(img)
        
        # 设置窗口图标
        self.iconphoto(True, icon)
        self.icon = icon
        
        # 创建画布组件
        self.canvas = Canvas(self, width=600, height=800)
        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.canvas.configure(bg=self.default_bg_color)
        
        # 在这里添加代码以加载图像
        desired_size = (25, 25)
        
        self.image1 = Image.open("icons/icon1.png")
        self.photo_image1 = ImageTk.PhotoImage(self.image1.resize(desired_size, Image.LANCZOS))
        
        self.image2 = Image.open("icons/icon2.png")
        self.photo_image2 = ImageTk.PhotoImage(self.image2.resize(desired_size, Image.LANCZOS))
        
        self.image3 = Image.open("icons/icon3.png")
        self.photo_image3 = ImageTk.PhotoImage(self.image3.resize(desired_size, Image.LANCZOS))
        
        self.image4 = Image.open("icons/icon4.png")
        self.photo_image4 = ImageTk.PhotoImage(self.image4.resize(desired_size, Image.LANCZOS))
        
        self.image5 = Image.open("icons/icon5.png")
        self.photo_image5 = ImageTk.PhotoImage(self.image5.resize(desired_size, Image.LANCZOS))
        
        self.image6 = Image.open("icons/icon6.png")
        self.photo_image6 = ImageTk.PhotoImage(self.image6.resize(desired_size, Image.LANCZOS))
        
        self.image7 = Image.open("icons/icon7.png")
        self.photo_image7 = ImageTk.PhotoImage(self.image7.resize(desired_size, Image.LANCZOS))
        
        self.image8 = Image.open("icons/icon8.png")
        self.photo_image8 = ImageTk.PhotoImage(self.image8.resize(desired_size, Image.LANCZOS))
        
        self.image9 = Image.open("icons/icon9.png")
        self.photo_image9 = ImageTk.PhotoImage(self.image9.resize(desired_size, Image.LANCZOS))
        
        # 创建自定义按钮样式
        style = ttk.Style()
        style.configure("WeChat.TButton",
                        background="#009900",
                        foreground="#F5DE83",
                        font=("宋体", 15, "bold"),
                        relief="raised",
                        padding=(6, 5),
                        borderwidth=2,
                        bordercolor="#F5DE83")
        
        # 创建导航菜单栏 Frame
        nav_bar = tk.Frame(self)
        nav_bar.grid(row=0, column=0, sticky="nsew")
        nav_bar.configure(bg=self.default_bg_color)  # 设置导航菜单栏背景颜色
        
        # 创建菜单栏
        self.menu_bar = tk.Menu()
        
        # 添加一个空白菜单项，设为不可用状态
        self.menu_bar.add_command(label="版本号v 1.0   版权：QingShan+Chatgtp  ", state="disabled")
        
        # 创建主题菜单
        bg_menu = tk.Menu(self.menu_bar, tearoff=0)
        bg_menu.add_command(label="更换背景图片", image=self.photo_image1, compound="left",
                            command=self.change_background_image)
        bg_menu.add_command(label="更换背景颜色", compound="left", command=self.change_background_color)
        theme_button = ttk.Button(nav_bar, text="主题", image=self.photo_image1, style="WeChat.TButton",
                                  compound="left",
                                  command=self.open_theme)
        theme_button.grid(row=0, column=0, sticky="nsew")
        
        # 将主题添加到菜单栏
        theme_button = ttk.Button(nav_bar, text="主题", image=self.photo_image1, style="WeChat.TButton",
                                  compound="left", command=self.open_theme)
        theme_button.grid(row=0, column=0, sticky="w")
        
        # 创建文件菜单
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="导入数据", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.quit)
        file_button = ttk.Button(nav_bar, text="文件", image=self.photo_image2, style="WeChat.TButton", compound="left",
                                 command=self.open_file)
        file_button.grid(row=0, column=1, sticky="nsew")
        
        # 添加文件到菜单栏
        file_button = ttk.Button(nav_bar, text="文件", image=self.photo_image2, style="WeChat.TButton", compound="left",
                                 command=self.open_file)
        file_button.grid(row=0, column=1, sticky="w")
        
        # 创建牌位功能菜单
        plaque_menu = tk.Menu(self.menu_bar, tearoff=0)
        plaque_menu.add_command(label="输入牌位信息", image=self.photo_image3, compound="left",
                                command=self.open_plaque)
        plaque_menu.add_command(label="退出", image=self.photo_image3, compound="left", command=self.quit)
        plaque_button = ttk.Button(nav_bar, text="牌位", image=self.photo_image3, style="WeChat.TButton",
                                   compound="left", command=self.open_plaque)
        plaque_button.grid(row=0, column=2, sticky="nsew")
        
        # 将牌位功能添加到菜单栏
        Plaque_button = ttk.Button(nav_bar, text="牌位", image=self.photo_image3, style="WeChat.TButton",
                                   compound="left", command=self.open_plaque)
        Plaque_button.grid(row=0, column=2, sticky="w")
        
        # 创建排版设计功能菜单
        layout_menu = tk.Menu(self.menu_bar, tearoff=0)
        layout_menu.add_command(label="排版设计", image=self.photo_image4, compound="left", command=self.open_Layout)
        layout_menu.entryconfig(0, image=self.photo_image4)
        layout_button = ttk.Button(nav_bar, text="排版", image=self.photo_image4, style="WeChat.TButton",
                                   compound="left", command=self.open_Layout)
        layout_button.grid(row=0, column=3, sticky="nsew")
        
        # 将排版设计功能添加到菜单栏
        layout_button = ttk.Button(nav_bar, text="排版", image=self.photo_image4, style="WeChat.TButton",
                                   compound="left", command=self.open_Layout)
        layout_button.grid(row=0, column=3, sticky="w")
        
        # 创建打印机菜单
        print_menu = tk.Menu(self.menu_bar, tearoff=0)
        print_menu.add_command(label="连接打印机", image=self.photo_image5, compound="left",
                               command=self.open_print)
        print_menu.entryconfig(0, image=self.photo_image5)
        print_button = ttk.Button(nav_bar, text="打印机", image=self.photo_image5, style="WeChat.TButton",
                                  compound="left", command=self.open_print)
        print_button.grid(row=0, column=4, sticky="nsew")
        
        # 将打印机添加到菜单栏
        print_button = ttk.Button(nav_bar, text="打印机", image=self.photo_image5, style="WeChat.TButton",
                                  compound="left", command=self.open_print)
        print_button.grid(row=0, column=4, sticky="w")
        
        # 创建查询菜单
        query_button = tk.Menu(self.menu_bar, tearoff=0)
        query_button.add_command(label="数据查询", image=self.photo_image6, compound="left",
                                 command=self.open_query)
        query_button.entryconfig(0, image=self.photo_image5)
        query_button = ttk.Button(nav_bar, text="查询", image=self.photo_image6, style="WeChat.TButton",
                                  compound="left", command=self.open_query)
        query_button.grid(row=0, column=5, sticky="nsew")
        
        # 将查询加到菜单栏
        query_button = ttk.Button(nav_bar, text="查询", image=self.photo_image6, style="WeChat.TButton",
                                  compound="left", command=self.open_query)
        query_button.grid(row=0, column=5, sticky="w")
        
        # 创建数据库菜单
        database_button = tk.Menu(self.menu_bar, tearoff=0)
        database_button.add_command(label="数据库连接", image=self.photo_image7, compound="left",
                                    command=self.open_database)
        database_button.entryconfig(0, image=self.photo_image5)
        database_button = ttk.Button(nav_bar, text="数据库", image=self.photo_image7, style="WeChat.TButton",
                                     compound="left", command=self.open_database)
        database_button.grid(row=0, column=6, sticky="nsew")
        
        # 将数据库菜单添加到菜单栏
        database_button = ttk.Button(nav_bar, text="数据库", image=self.photo_image7, style="WeChat.TButton",
                                     compound="left", command=self.open_database)
        database_button.grid(row=0, column=6, sticky="w")
        
        # 创建设置菜单
        settings_button = tk.Menu(self.menu_bar, tearoff=0)
        settings_button.add_command(label="基本设置", image=self.photo_image8, compound="left",
                                    command=self.open_settings)
        settings_button.entryconfig(0, image=self.photo_image5)
        settings_button = ttk.Button(nav_bar, text="设置", image=self.photo_image8, style="WeChat.TButton",
                                     compound="left", command=self.open_settings)
        settings_button.grid(row=0, column=7, sticky="nsew")
        
        # 将设置添加到菜单栏
        settings_button = ttk.Button(nav_bar, text="设置", image=self.photo_image8, style="WeChat.TButton",
                                     compound="left", command=self.open_Settings)
        settings_button.grid(row=0, column=7, sticky="w")
        
        # 创建更新菜单
        update_button = tk.Menu(self.menu_bar, tearoff=0)
        update_button.add_command(label="检查更新", image=self.photo_image9, compound="left",
                                  command=self.check_for_update)
        update_button.entryconfig(0, image=self.photo_image5)
        update_button = ttk.Button(nav_bar, text="更新", image=self.photo_image9, style="WeChat.TButton",
                                   compound="left", command=self.check_for_update)
        update_button.grid(row=0, column=8, sticky="nsew")
        
        # 将更新菜单添加到菜单栏
        update_button = ttk.Button(nav_bar, text="更新", image=self.photo_image9, style="WeChat.TButton",
                                   compound="left", command=self.check_for_update)
        update_button.grid(row=0, column=8, sticky="w")
        
        # 设置主窗口的菜单栏
        # 将导航菜单栏添加到主窗口
        self.grid_columnconfigure(0, weight=1)
        self.config(menu=self.menu_bar)
    
    def center_window(self, window):
        window.update_idletasks()
        # 添加代码块缩进
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def change_background_image(self):
        file_path = filedialog.askopenfilename(parent=self, filetypes=[("Image files", ".png;.jpg;.jpeg;.gif")])
        
        if file_path:
            self.bg_image = tk.PhotoImage(file=file_path)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
    
    def change_background_color(self):
        color = colorchooser.askcolor(parent=self)[1]
        
        if color:
            self.configure(bg=color)
            self.default_bg_color = color  # 更新默认背景颜色
            self.nav_bar.configure(bg=color)  # 更新导航菜单栏的背景颜色
        
        self.center_window(self)
        
        self.config(menu=self.menu_bar)


    def open_theme(self):
        theme_window = theme(self)  # 将 self 作为参数传递
        theme_window.mainloop()


    def open_file(self):
        file_window = file(self)  # 将 self 作为参数传递
        file_window.mainloop()


    def open_settings(self):
        settings_window = Settings(self)  # 将 self 作为参数传递
        settings_window.mainloop()
    def open_Settings(self):
        Settings_window = Settings(self)
        Settings_window.mainloop()

    def open_plaque(self):
        plaque_window = plaque(self)
        plaque_window.mainloop()


    def open_Layout(self):
        Layout_window = Layout(self)
        Layout_window.mainloop()


    def open_print(self):
        print_window = PrintConnector(self)  # 创建PrintConnector类的新实例
        print_window.mainloop()


    def open_query(self):
        query_button_window = query(self)
        query_button_window.mainloop()


    def open_database(self):
        database_window = Database(self)
        database_window.mainloop()


    def open_Settings(self):
        Settings_window = Settings(self)
        Settings_window.mainloop()


    def check_for_update(self):
        database_window = update(self)
        database_window.mainloop()
    # 在这里添加检查更新的逻辑
    

# 在这里添加排版布局功能窗口的代码
class theme(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("主题")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
    # 在这里添加
    
class file(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("文件")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
    # 在这里添加
    
class plaque(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("牌位编写")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
        
class Layout(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("排版设计")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
     
class PrintConnector(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("打印机列表")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
    # 在这里添加打印机窗口的代码


class query(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("信息查询")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
    # 在这里添加查询窗口的代码


class Database(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("数据库")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
    
    # 在这里添加数据库窗口的代码


class Settings(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("基本设置")
        self.geometry("850x700")  # 设置窗口宽度为850像素，高度为700像素
        parent.center_window(self)  # 添加这一行
        # 在这里添加设置窗口的代码
        
        # 创建保存按钮
        save_button = tk.Button(self, text="保存", command=self.save_settings)
        save_button.pack()
        
        # 创建关闭按钮
        close_button = tk.Button(self, text="关闭", command=self.destroy)
        close_button.pack()


        self.setLayout(layout)


def save_settings(self):
    # 在这里添加保存设置的逻辑
    pass


class update(tk.Toplevel):
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
    app = MainApplication()
    app.mainloop()
