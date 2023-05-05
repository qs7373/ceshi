# # -*- coding: utf-8 -*-
"""
This module defines the Settings class, which can be used to load and save
configuration settings to a file.
"""

import configparser
import shutil
import sqlite3
import sys
import tempfile
import tkinter as tk
import urllib
from tkinter import messagebox
from urllib.request import urlopen
import urllib.request
import psycopg2 as psycopg2
import requests
from flask import Flask, request
from matplotlib import pyplot as plt
import zipfile
import urllib.request
import PyQt5
import matplotlib.pyplot as plt



# 向指定URL发送POST请求
def send_post_request(url, data):
    response = requests.post(url, data=data)
    return response.text

# 创建主窗口
root = tk.Tk()
root.title("牌位打印")
root.geometry("400x300")
root.configure(bg="#E5E5E5")

app = Flask(__name__)

@app.route('/吉祥')
def hello():
    name = request.args.get('name', '')
    return f'Hello, {name}!'

class Settings:
    def __init__(self, config_file='settings.ini'):
        self.load_settings(config_file)
    
    def load_settings(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        self.font_dir = self.config.get('Font', 'dir')
        self.font_size = self.config.getint('Font', 'size')
        self.font_spacing = self.config.getfloat('Font', 'spacing')
        self.line_spacing = self.config.getfloat('Font', 'line_spacing')
        self.paper_width = self.config.getint('Paper', 'width')
        self.paper_height = self.config.getint('Paper', 'height')
        self.is_landscape = self.config.getboolean('Paper', 'is_landscape')
        self.is_text_landscape = self.config.getboolean('Paper', 'is_text_landscape')
        self.background_image = self.config.get('Background', 'image')
        self.background_color = self.config.get('Background', 'color')
        self.logo_image = self.config.get('Logo', 'image')
        self.local_ip = self.config.get('Network', 'local_ip')
        self.remote_address = self.config.get('Network', 'remote_address')
        self.cloud_print_address = self.config.get('Network', 'cloud_print_address')
        self.network_printer_address = self.config.get('Network', 'network_printer_address')
        self.watermark_image = self.config.get('Watermark', 'image')
        self.db_address = self.config.get('Database', 'address')
        
        settings = Settings()
        
        config_value = settings.config
        
        # 初始化数据库连接
        if self.db_address.startswith('sqlite'):
            self.db = Database('sqlite', self.db_address.split('//')[-1])
        elif self.db_address.startswith('mysql'):
            parts = self.db_address.split('//')[-1].split(':')
            host, port = parts[0], int(parts[1])
            database = parts[2].split('/')[0]
            username, password = parts[2].split('/')[1].split(':')
            self.db = Database('mysql', host, port, database, username, password)
        elif self.db_address.startswith('postgresql'):
            parts = self.db_address.split('//')[-1].split(':')
            host, port = parts[0], int(parts[1])
            database = parts[2].split('/')[0]
            username, password = parts[2].split('/')[1].split(':')
            self.db = Database('postgres', host, port, database, username, password)
        else:
            raise ValueError(f"Unsupported database address: {self.db_address}")
        
        self.db.initialize_database()
    
    def load_settings(self, config_file='settings.ini'):
        # 初始化配置文件
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        # 加载字体设置
        self.font_dir = self.config.get('Font', 'dir')
        self.font_size = self.config.getint('Font', 'size')
        self.font_spacing = self.config.getint('Font', 'spacing')
        self.line_spacing = self.config.getint('Font', 'line_spacing')
        
        # 加载纸张设置
        self.paper_width = self.config.getint('Paper', 'width')
        self.paper_height = self.config.getint('Paper', 'height')
        self.is_landscape = self.config.getboolean('Paper', 'is_landscape')
        self.is_text_landscape = self.config.getboolean('Paper', 'is_text_landscape')
        
        # 加载界面设置
        self.background_image = self.config.get('UI', 'background_image')
        self.background_color = self.config.get('UI', 'background_color')
        self.logo_image = self.config.get('UI', 'logo_image')
        
        # 加载打印设置
        self.local_ip = self.config.get('Print', 'local_ip')
        self.remote_address = self.config.get('Print', 'remote_address')
        self.cloud_print_address = self.config.get('Print', 'cloud_print_address')
        self.network_printer_address = self.config.get('Print', 'network_printer_address')
        self.watermark_image = self.config.get('Print', 'watermark_image')
        
        # 加载数据库设置
        self.db_address = self.config.get('Database', 'address')
    
    def save_settings(self, config_file='settings.ini'):
        # 保存配置文件
        with open(config_file, 'w') as f:
            self.config.write(f)
    
    def set_font_dir(self, font_dir):
        # 设置字体目录
        self.font_dir = font_dir
        self.config['Font']['dir'] = font_dir
    
    def set_font_size(self, font_size):
        # 设置字体大小
        self.font_size = font_size
        self.config['Font']['size'] = str(font_size)
    
    def set_font_spacing(self, font_spacing):
        # 设置字体间距
        self.font_spacing = font_spacing
        self.config['Font']['spacing'] = str(font_spacing)
    
    def set_line_spacing(self, line_spacing):
        # 设置行距
        self.line_spacing = line_spacing
        self.config['Font']['line_spacing'] = str(line_spacing)
    
    def set_paper_size(self, width, height):
        # 设置纸张大小
        self.paper_width = width
        self.paper_height = height
        self.config['Paper']['width'] = str(width)
        self.config['Paper']['height'] = str(height)
    
    def set_orientation(self, is_landscape):
        # 设置纸张方向
        self.is_landscape = is_landscape
        self.config['Paper']['is_landscape'] = str(is_landscape)
    
    def set_text_orientation(self, is_text_landscape):
        # 设置文字方向
        self.is_text_landscape = is_text_landscape
        self.config['Paper']['is_text_landscape'] = str(is_text_landscape)
    
    def set_background_image(self, image_path):
        # 设置背景图片
        self.background_image = image_path
        self.config['UI']['background_image'] = image_path
    
    def set_background_color(self, color):
        # 设置背景颜色
        self.background_color = color
        self.config['UI']['background_color'] = color
    
    def set_logo_image(self, image_path):
        # 设置Logo图片
        self.logo_image = image_path
        self.config['UI']['logo_image'] = image_path
    
    def set_local_ip(self, ip):
        # 设置局域网地址
        self.local_ip = ip
        self.config['Print']['local_ip'] = ip
    
    def set_remote_address(self, address):
        # 设置远程连接地址
        self.remote_address = address
        self.config['Print']['remote_address'] = address
    
    def set_cloud_print_address(self, address):
        # 设置云打印地址
        self.cloud_print_address = address
        self.config['Print']['cloud_print_address'] = address
    
    def set_network_printer_address(self, address):
        # 设置网络打印机地址
        self.network_printer_address = address
        self.config['Print']['network_printer_address'] = address
    
    def set_watermark_image(self, image_path):
        # 设置水印图片
        self.watermark_image = image_path
        self.config['Print']['watermark_image'] = image_path
    
    def set_db_address(self, db_address):
        # 设置数据库地址
        self.db_address = db_address
        self.config['Database']['address'] = db_address
    
    def set_default_settings(self):
        # 恢复默认设置
        import configparser
        self.config = configparser.ConfigParser()
        self.config['Font'] = {
            'dir': 'C:/Windows/Fonts',
            'size': '12',
            'spacing': '0',
            'line_spacing': '1'
        }
        self.config['Paper'] = {
            'width': '595',
            'height': '842',
            'is_landscape': 'False',
            'is_text_landscape': 'False'
        }
        self.config['UI'] = {
            'background_image': '',
            'background_color': 'white',
            'logo_image': ''
        }
        self.config['Print'] = {
            'local_ip': '',
            'remote_address': '',
            'cloud_print_address': '',
            'network_printer_address': '',
            'watermark_image': ''
        }
        self.save_settings()
        self.load_settings()


# 实例
settings = Settings()
settings.load_settings()
print(settings.font_dir)
print(settings.font_size)
settings.set_font_dir('C:/Windows/Fonts')
settings.set_font_size(14)
settings.save_settings()


class InputFunction:
    def __init__(self):
        self.project1_names = []
        self.project2_names = []
        self.project3_names = []

        self.project_list = [
            {
                'name': '消灾延寿',
                'content': '佛光普照（）长生禄位',
                'input_type': 'name'
            },
            {
                'name': '往生超荐',
                'content': '佛力超荐（）莲位，阳上人（）',
                'input_type': 'name'
            },
            {
                'name': '其它祈福',
                'content': '姓名（），地址（）',
                'input_type': 'name'
            }
        ]

        self.data = []

    def add_project(self, name, content, input_type):
        # 添加新项目
        self.project_list.append({
            'name': name,
            'content': content,
            'input_type': input_type
        })

    def remove_project(self, name):
        # 移除项目
        for project in self.project_list:
            if project['name'] == name:
                self.project_list.remove(project)

    def input_data(self, project_name, data):
        # 输入数据
        for project in self.project_list:
            if project['name'] == project_name:
                if project['input_type'] == 'name':
                    names = data.split(' ')
                    for name in names:
                        self.data.append({'name': name})
                elif project['input_type'] == 'address':
                    address = data.strip()
                    for d in self.data:
                        d['address'] = address
                break

    def clear_data(self):
        # 清除数据
        self.data = []

    def get_data(self):
        # 获取输入的数据
        return self.data

    def get_project_names(self, project_name):
        # 获取某个项目的名字列表
        if project_name == '消灾延寿':
            return self.project1_names
        elif project_name == '往生超荐':
            return self.project2_names
        elif project_name == '其它祈福':
            return self.project3_names
        else:
            return []

    def add_name_to_project1(self, name):
        self.project1_names.append(name)

    def add_name_to_project2(self, name1, name2):
        self.project2_names.append((name1, name2))

    def add_name_to_project3(self, name, address):
        self.project3_names.append({'name': name, 'address': address})

    def create_input_window(self):
        # 创建输入窗口
        input_window = tk.Toplevel()
        input_window.title('输入窗口')

        for i, project in enumerate(self.project_list):
            # 创建项目名称的标签
            project_label = tk.Label(input_window, text=project['name'])
            project_label.grid(row=i, column=0)

            # 创建第一个项目的输入框和下拉菜单
            project1_label = tk.Label(input_window, text='消灾延寿')
            project1_label.grid(row=0, column=0)
            project1_input_var = tk.StringVar()
            project1_input_entry = tk.Entry(input_window, textvariable=project1_input_var)
            project1_input_entry.grid(row=0, column=1)
            project1_options = ['佛光普照（）长生禄位']
            project1_dropdown_var = tk.StringVar()
            project1_dropdown = tk.OptionMenu(input_window, project1_dropdown_var, *project1_options)
            project1_dropdown.grid(row=0, column=2)
            project1_confirm_button = tk.Button(input_window, text='确认', command=lambda: self.add_name_to_project1(project1_input_var.get().split()))
            project1_confirm_button.grid(row=0, column=3)

            # 创建第二个项目的输入框和下拉菜单
            project2_label = tk.Label(input_window, text='往生超荐')
            project2_label.grid(row=1, column=0)
            project2_input_var1 = tk.StringVar()
            project2_input_entry1 = tk.Entry(input_window, textvariable=project2_input_var1)
            project2_input_entry1.grid(row=1, column=1)
            project2_input_var2 = tk.StringVar()
            project2_input_entry2 = tk.Entry(input_window, textvariable=project2_input_var2)
            project2_input_entry2.grid(row=1, column=2)
            project2_options = ['佛力超荐（）莲位', '阳上人（）']
            project2_dropdown_var = tk.StringVar()
            project2_dropdown = tk.OptionMenu(input_window, project2_dropdown_var, *project2_options)
            project2_dropdown.grid(row=1, column=3)
            project2_confirm_button = tk.Button(input_window, text='确认', command=lambda: self.add_name_to_project2(project2_input_var1.get(), project2_input_var2.get()))
            project2_confirm_button.grid(row=1, column=4)

            # 创建第三个项目的输入框和下拉菜单
            project3_label = tk.Label(input_window, text='其它祈福')
            project3_label.grid(row=2, column=0)
            project3_input_var1 = tk.StringVar()
            project3_input_entry1 = tk.Entry(input_window, textvariable=project3_input_var1)
            project3_input_entry1.grid(row=2, column=1)
            project3_input_var2 = tk.StringVar()
            project3_input_entry2 = tk.Entry(input_window, textvariable=project3_input_var2)
            project3_input_entry2.grid(row=2, column=2)
            project3_options = ['姓名（）地址（）']
            project3_dropdown_var = tk.StringVar()
            project3_dropdown = tk.OptionMenu(input_window, project3_dropdown_var, *project3_options)
            project3_dropdown.grid(row=2, column=3)
            project3_confirm_button = tk.Button(input_window, text='确认', command=lambda: self.add_name_to_project3(project3_input_var1.get(), project3_input_var2.get()))
            project3_confirm_button.grid(row=2, column=4)

            # 创建关闭窗口按钮
            close_button = tk.Button(input_window, text='关闭', command=input_window.destroy)
            close_button.grid(row=3, column=2)

# 示例用法
input_module = InputFunction()
input_module.create_input_window()

import json
from tkinter import filedialog


def import_file():
    # 导入文件，返回文件路径
    file_path = filedialog.askopenfilename()
    return file_path


class PrintFunction:
    def __init__(self):
        self.print_data = None
        self.print_range = (0, 0)  # 打印范围
        self.margin_left = 0  # 左边距
        self.margin_right = 0  # 右边距
        self.header = ""  # 页眉
        self.footer = ""  # 页脚
        self.print_rule = {}  # 打印规则
        self.preview_data = ""  # 打印预览数据

    def set_print_range(self, start, end):
        self.print_range = (start, end)

    def set_margin(self, left, right):
        self.margin_left = left
        self.margin_right = right

    def set_header(self, header):
        self.header = header

    def set_footer(self, footer):
        self.footer = footer

    def set_print_rule(self, rule):
        self.print_rule = rule
        # 更新打印预览数据
        self.preview_data = self.format_data()
    
    @staticmethod
    def import_data(file_path):
        # 根据文件路径导入数据
        # 这里需要根据文件类型来导入数据，示例中假设导入的是txt文件
        with open(file_path, 'r') as f:
            data = f.read()
        return data

    def format_data(self):
        # 根据打印规则格式化数据，返回打印预览数据
        # 示例中假设格式化方式为按行输出，每行一个数据项
        data = ""
        for k, v in self.print_rule.items():
            data += "\n" + k + ": "
            for i, item in enumerate(v):
                data += item
                if i < len(v) - 1:
                    data += ", "
        return data

    def set_preview_data(self, data):
        self.preview_data = data

    def preview(self):
        # 预览打印效果
        preview_window = tk.Toplevel()
        preview_window.title("打印预览")
        preview_window.geometry("400x400")
        tk.Label(preview_window, text=self.preview_data).pack()
        tk.Button(preview_window, text="打印", command=self.print_data).pack()

    def update_print_log(self):
        # 更新打印日志，示例中省略实现
        pass

    def custom_print_rule(self):
        # 自定义打印规则，支持JSON格式
        rule_window = tk.Toplevel()
        rule_window.title("自定义打印规则")
        rule_window.geometry("400x400")
        tk.Label(rule_window, text="请输入打印规则：").pack()
        rule_text = tk.Text(rule_window, height=10)
        rule_text.pack()
        tk.Button(rule_window, text="保存", command=lambda: self.set_print_rule(json.loads(rule_text.get("1.0", "end")))).pack()
    
    def custom_print_layout(self):
        # 自定义打印排版布局
        layout_window = tk.Toplevel()
        layout_window.title("自定义打印布局")
        layout_window.geometry("400x400")
        tk.Label(layout_window, text="请设置排版样式：").pack()
        
        # 布局样式列表
        layout_options = ['品字型', '九宫格', '田字型', 'T型', '凸型']
        
        # 排版样式下拉菜单
        layout_variable = tk.StringVar(layout_window)
        layout_variable.set(layout_options[0])  # 默认选中第一个
        tk.OptionMenu(layout_window, layout_variable, *layout_options).pack()
        
        # 自定义排版布局
        layout_text = tk.Text(layout_window, height=10)
        layout_text.pack()
        
        # 根据排版样式更新排版布局
        def update_layout():
            selected_layout = layout_variable.get()
            if selected_layout == '品字型':
                layout_text.delete("1.0", "end")
                layout_text.insert("1.0", "╋\n┃\n╋")
            elif selected_layout == '九宫格':
                layout_text.delete("1.0", "end")
                layout_text.insert("1.0",
                                   "┏━┳━┳━┓\n┃　　　　　　　　　　　　　　　　　　　　　　　　　　　　　┃\n┣━╋━╋━┫\n┃　　　　　　　　　　　　　　　　　　　　　　　　　　　　　┃\n┣━╋━╋━┫\n┃　　　　　　　　　　　　　　　　　　　　　　　　　　　　　┃\n┗━┻━┻━┛")
            elif selected_layout == '田字型':
                layout_text.delete("1.0", "end")
                layout_text.insert("1.0", "┏━━━┳━━━┓\n┃　　　┃　　　┃\n┣━━━╋━━━┫\n┃　　　┃　　　┃\n┗━━━┻━━━┛")
            elif selected_layout == 'T型':
                layout_text.delete("1.0", "end")
                layout_text.insert("1.0", "┏━━━┓\n┃　　　┃\n┃　　　┃\n┃　　　┃\n┣━━━╋━━━┫\n┃　　　┃\n┃　　　┃\n┃　　　┃\n┗━━━┛")
            elif selected_layout == '凸型':
                layout_text.delete("1.0", "end")
                layout_text.insert("1.0",
                                   "┏━━━┳━━━┳━━━┓\n┃　　　┃　　　┃　　　┃\n┃　　　┃　　　┃　　　┃\n┣━━━╋━━━╋━━━┫\n┃　　　┃　　　┃　　　┃\n┃　　　┃　　　┃　　　┃\n┗━━━┻━━━┻━━━┛")
        
        # 更新排版布局
        tk.Button(layout_window, text="更新布局", command=update_layout).pack()
        
        # 保存排版布局
        tk.Button(layout_window, text="保存布局",
                  command=lambda: self.set_preview_data(layout_text.get("1.0", "end"))).pack()
        tk.Button(layout_window, text="保存",
                  command=lambda: self.set_print_layout(layout_text.get("1.0", "end"))).pack()
        
        def print_data(data):
            for row in data:
                print(row)
                # 打印数据
                # 实现省略，需要根据打印预览数据和打印设置进行实际打印操作
        self.update_print_log()
        messagebox.showinfo(title="提示", message="打印完成！")
        
        def custom_print_layout_custom(self):
            # 自定义打印排版布局
            custom_window = tk.Toplevel()
            custom_window.title("自定义打印布局")
            custom_window.geometry("400x400")
            
            # 创建自定义布局选择框
            custom_frame = tk.Frame(custom_window, padx=10, pady=10)
            custom_frame.pack()
            
            tk.Label(custom_frame, text="请选择布局：").grid(row=0, column=0)
            
            # 定义布局选项
            layout_options = [
                ("单栏", 1),
                ("双栏", 2),
                ("三栏", 3)
            ]
            
            # 创建布局选项按钮
            layout_choice = tk.IntVar()
            for option, value in layout_options:
                tk.Radiobutton(custom_frame, text=option, variable=layout_choice, value=value).grid(row=value, column=0)
            
            # 自定义栏数
            tk.Label(custom_frame, text="请输入栏数：").grid(row=4, column=0)
            col_num = tk.Entry(custom_frame)
            col_num.grid(row=4, column=1)
            
            # 自定义栏宽
            tk.Label(custom_frame, text="请输入栏宽（以英寸为单位）：").grid(row=5, column=0)
            col_width = tk.Entry(custom_frame)
            col_width.grid(row=5, column=1)
            
            # 自定义栏间距
            tk.Label(custom_frame, text="请输入栏间距（以英寸为单位）：").grid(row=6, column=0)
            col_gap = tk.Entry(custom_frame)
            col_gap.grid(row=6, column=1)
            
            # 保存按钮
            tk.Button(custom_window, text="保存", command=custom_window.destroy).pack()
    
    def set_print_layout(self, param):
        pass


import subprocess


class PrintConnector:
    def __init__(self):
        self.printers = {}

    def detect_local_printers(self):
        # 检测本地打印机
        if platform.system() == "Windows":
            # Windows 平台使用 wmic 命令获取打印机列表
            result = subprocess.run("wmic printer get name", capture_output=True, text=True)
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line and line != "Name":
                    self.printers[line] = {"name": line, "type": "local", "location": ""}
        elif platform.system() == "Linux":
            # Linux 平台使用 lpstat 命令获取打印机列表
            result = subprocess.run("lpstat -a", capture_output=True, text=True, shell=True)
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line:
                    self.printers[line] = {"name": line, "type": "local", "location": ""}
        elif platform.system() == "Darwin":
            # macOS 平台使用 lpstat 命令获取打印机列表
            result = subprocess.run("lpstat -a", capture_output=True, text=True, shell=True)
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line:
                    self.printers[line] = {"name": line, "type": "local", "location": ""}
    
    def detect_network_printers(self):
        # 检测局域网内的打印机
        if platform.system() == "Windows":
            # Windows 平台使用 net view 命令获取网络共享列表
            result = subprocess.run("net view", capture_output=True, text=True)
            for line in result.stdout.split("\n"):
                if line.startswith("\\\\"):
                    # 如果共享名称以两个反斜杠开头，说明是网络共享
                    name = line.split()[0].strip("\\")
                    self.printers[name] = {"name": name, "type": "network", "location": ""}
        elif platform.system() == "Linux":
            # Linux 平台使用 smbtree 命令获取网络共享列表
            result = subprocess.run("smbtree -N", capture_output=True, text=True, shell=True)
            for line in result.stdout.split("\n"):
                if line.startswith("\\\\"):
                    # 如果共享名称以两个反斜杠开头，说明是网络共享
                    name = line.split()[0].strip("\\")
                    self.printers[name] = {"name": name, "type": "network", "location": ""}

    def detect_printers(self):
        # 检测所有可用的打印机
        self.detect_local_printers()
        self.detect_network_printers()

    def print_file(self, file_path, printer_name=None, copies=1):
        # 打印文件
        if not printer_name:
            # 如果没有指定打印机名称，就使用默认打印机
            printer_name = self.get_default_printer()
        if platform.system() == "Windows":
            # Windows 平台使用 start 命令打印文件
            subprocess.run(f'start /b /wait "" "notepad.exe" /p "{file_path}" /pt "{printer_name}"')
        elif platform.system() == "Linux":
            # Linux 平台使用 lpr 命令打印文件
            subprocess.run(f'lpr -P "{printer_name}" -# {copies} "{file_path}"', shell=True)
        elif platform.system() == "Darwin":
            # macOS 平台使用 lp 命令打印文件
            subprocess.run(f'lp -d "{printer_name}" -n {copies} "{file_path}"', shell=True)
    
    def print_text(self, text, printer_name=None, copies=1):
        # 打印文本
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write(text)
            temp_file_path = temp_file.name
        self.print_file(temp_file_path, printer_name, copies)
        os.unlink(temp_file_path)
    
    @staticmethod
    def get_default_printer(self):
        # 获取默认打印机名称
        if platform.system() == "Windows":
            result = subprocess.run("wmic printer where Default='TRUE' get Name", capture_output=True, text=True)
            return result.stdout.strip().split("\n")[1].strip()
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            result = subprocess.run("lpstat -d", capture_output=True, text=True, shell=True)
            return result.stdout.strip().split(":")[1].strip()
    
    def install_printer_driver(self, driver_path):
        # 安装打印机驱动
        if platform.system() == "Windows":
            subprocess.run(f'rundll32 printui.dll,PrintUIEntry /ia /K /u /f "{driver_path}"', shell=True)
        elif platform.system() == "Linux":
            subprocess.run(f'sudo dpkg -i "{driver_path}"', shell=True)
        elif platform.system() == "Darwin":
            subprocess.run(f'sudo installer -pkg "{driver_path}" -target /', shell=True)
    
    def connect_remote_printer(self, printer_address, username=None, password=None):
        # 连接远程打印机
        if platform.system() == "Windows":
            # Windows 平台使用 net use 命令连接网络打印机
            if username and password:
                subprocess.run(f'net use "\\\\{printer_address}" /user:{username} "{password}"', shell=True)
            else:
                subprocess.run(f'net use "\\\\{printer_address}"', shell=True)
        elif platform.system() == "Linux":
            # Linux 平台使用 smbclient 命令连接网络打印机
            if username and password:
                subprocess.run(f'smbclient -U {username}%{password} "\\\\{printer_address}"', shell=True)
            else:
                subprocess.run(f'smbclient "\\\\{printer_address}"', shell=True)
    
    def print_cloud_file(self, file_url, printer_name=None, copies=1):
        # 从云端打印文件
        # 下载文件
        file_name = os.path.basename(file_url)
        with urlopen(file_url) as response, open(file_name, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        self.print_file(file_name, printer_name, copies)
        os.unlink(file_name)
    
    def bluetooth_print_file(self, file_path, printer_mac_address):
        # 使用 Bleak 库连接蓝牙打印机并打印文件
        import asyncio
        from bleak import BleakClient
        uuid_print_data = "0000fff1-0000-1000-8000-00805f9b34fb"
        
        async def print_with_bleak():
            async with BleakClient(printer_mac_address) as client:
                with open(file_path, "rb") as f:
                    await client.write_gatt_char(UUID_PRINT_DATA, f.read())
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(print_with_bleak())


import datetime

class PrintJob:
    def __init__(self, job_id, document_name, printer_name, status="Queued", creation_time=None):
        self.job_id = job_id
        self.document_name = document_name
        self.printer_name = printer_name
        self.status = status
        self.creation_time = creation_time if creation_time is not None else datetime.datetime.now()

class PrintSettings:
    def __init__(self):
        self.print_queue = []
        self.print_log = []

    def view_print_queue(self):
        # 查看打印队列
        if self.print_queue:
            print("Printing queue:")
            for job in self.print_queue:
                print(job)
        else:
            print("No jobs in printing queue.")

    def cancel_print_job(self, job_id):
        # 取消打印任务
        for job in self.print_queue:
            if job["id"] == job_id:
                self.print_queue.remove(job)
                print(f"Print job {job_id} cancelled.")
                break
        else:
            print(f"No print job with id {job_id} found.")

    def pause_print_job(self, job_id):
        # 暂停打印任务
        for job in self.print_queue:
            if job["id"] == job_id:
                job["status"] = "Paused"
                print(f"Print job {job_id} paused.")
                break
        else:
            print(f"No print job with id {job_id} found.")
            
    def resume_print_job(self, job_id):
        # 恢复打印任务
        for job in self.print_queue:
            if job["id"] == job_id:
                job["status"] = "Queued"
                print(f"Print job {job_id} resumed.")
                break
        else:
            print(f"No print job with id {job_id} found.")
            
    def view_print_log(self):
        # 查看打印日志
        if self.print_log:
            print("Print log:")
            for log in self.print_log:
                print(log)
        else:
            print("No log entries.")
            
    def search_print_log(self, query):
        # 查询打印日志
        results = []
        for log in self.print_log:
            if query in log["description"]:
                results.append(log)
        if results:
            print(f"Search results for '{query}':")
            for log in results:
                print(log)
        else:
            print(f"No results found for '{query}'.")
    
    def generate_statistics(self):
        # 生成统计分析图
        print_stats = {}
        for job in self.print_log:
            printer_name = job.printer_name
            status = job.status
            if printer_name not in print_stats:
                print_stats[printer_name] = {"Queued": 0, "Paused": 0, "Cancelled": 0, "Printed": 0}
            if status == "Queued":
                print_stats[printer_name]["Queued"] += 1
            elif status == "Paused":
                print_stats[printer_name]["Paused"] += 1
            elif status == "Cancelled":
                print_stats[printer_name]["Cancelled"] += 1
            elif status == "Printed":
                print_stats[printer_name]["Printed"] += 1
        print("Printing statistics:")
        for printer_name, stats in print_stats.items():
            print(f"{printer_name}: {stats}")
        
        # 生成统计分析图
        x_axis = list(print_stats.keys())
        printed_values = [stats["Printed"] for stats in print_stats.values()]
        cancelled_values = [stats["Cancelled"] for stats in print_stats.values()]
        paused_values = [stats["Paused"] for stats in print_stats.values()]
        plt.bar(x_axis, printed_values, label="Printed")
        plt.bar(x_axis, cancelled_values, label="Cancelled", bottom=printed_values)
        plt.bar(x_axis, paused_values, label="Paused",
                bottom=[sum(pair) for pair in zip(printed_values, cancelled_values)])
        plt.legend()
        plt.show()


import threading
from typing import Any, List, Tuple

# 根据需要选择数据库模块
# import sqlite3  # 使用SQLite
import mysql.connector  # 使用MySQL
# import psycopg2  # 使用PostgreSQL

class Database:
    def __init__(self, db_type: str, db_host: str, db_port: int, db_name: str, db_user: str, db_password: str):
        self.db_path = None
        self.db_type = db_type
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

        # 初始化数据库连接
        if db_type == "sqlite":
            self.conn = sqlite3.connect(db_name, check_same_thread=False)
            self.cursor = self.conn.cursor()
            self.lock = threading.Lock()
        elif db_type == "mysql":
            self.conn = mysql.connector.connect(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_password,
            )
            self.cursor = self.conn.cursor
        elif db_type == "postgres":
            self.conn = psycopg2.connect(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_password,
            )
            self.cursor = self.conn.cursor()
            self.lock = threading.Lock()
        
    
    def initialize_database(self):
        # 创建表格和初始化数据
        with self.lock:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS functions
                                (id SERIAL PRIMARY KEY, name TEXT,
                                content TEXT, module TEXT, platform TEXT,
                                description TEXT, created_at TIMESTAMP)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS constants
                                (id SERIAL PRIMARY KEY, name TEXT,
                                value TEXT, module TEXT, platform TEXT,
                                description TEXT, created_at TIMESTAMP)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS variables
                                (id SERIAL PRIMARY KEY, name TEXT,
                                value TEXT, module TEXT, platform TEXT,
                                description TEXT, created_at TIMESTAMP)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS print_logs
                                (id SERIAL PRIMARY KEY,
                                job_id INTEGER, description TEXT,
                                created_at TIMESTAMP)""")
            self.conn.commit()

    def query(self, query_str: str, params: Tuple = ()) -> List[Tuple]:
        # 查询数据库中的数据，并返回结果
        with self.lock:
            self.cursor.execute(query_str, params)
            return self.cursor.fetchall()

    def insert(self, table: str, columns: Tuple[str], values: Tuple) -> int:
        # 将新数据插入到数据库中
        with self.lock:
            columns_str = ",".join(columns)
            values_placeholder = ",".join(["%s" for _ in range(len(values))])
            query_str = f"INSERT INTO {table} ({columns_str}) VALUES ({values_placeholder})"
            self.cursor.execute(query_str, values)
            self.conn.commit()
            return self.cursor.lastrowid

    def update(self, table: str, columns_values: List[Tuple[str, Any]], where_clause: str, where_params: Tuple = ()):
        # 更新数据库中的数据
        with self.lock:
            if self.db_type == 'sqlite':
                set_clause = ",".join([f"{cv[0]}=?" for cv in columns_values])
            elif self.db_type in ['mysql', 'postgresql']:
                set_clause = ",".join([f"{cv[0]}=%s" for cv in columns_values])
            else:
                raise ValueError(f"Unsupported database type: {self.db_type}")
            query_str = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            params = tuple([cv[1] for cv in columns_values] + list(where_params))
            self.cursor.execute(query_str, params)
            self.conn.commit()

    def delete(self, table: str, where_clause: str, where_params: Tuple = ()):
        # 删除数据库中的数据
        with self.lock:
            query_str = f"DELETE FROM {table} WHERE {where_clause}"
            self.cursor.execute(query_str, where_params)
            self.conn.commit()
    
    def backup(self, backup_path: str):
        # 备份数据库到指定路径
        with self.lock:
            with open(backup_path, 'wb') as backup_file:
                cursor = self.conn.cursor()
                schema_rows = cursor.execute("SELECT sql FROM sqlite_master WHERE type='table'")
                schema = "\n".join(
                    line for row in schema_rows if row is not None for line in row if line.startswith("CREATE"))
                backup_file.write(bytes(schema, "utf-8"))
    
    def restore_database(self, backup_path):
        # 从备份文件中恢复数据库
        try:
            if self.db_type == 'sqlite':
                self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            elif self.db_type == 'mysql':
                # TODO: MySQL 连接实现
                pass
            elif self.db_type == 'postgresql':
                # TODO: PostgreSQL 连接实现
                pass
            else:
                raise ValueError(f"Unsupported database type: {self.db_type}")
            self.cursor = self.conn.cursor()

            with open(backup_path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    self.cursor.execute(line)

            self.conn.commit()
            print(f"Database restored from {backup_path}")
        except sqlite3.Error as e:
            print(f"Error restoring database: {e}")
        finally:
            if self.conn:
                self.conn.close()
                
import tkinter as tk
import platform
import urllib.request
import zipfile
import os
import shutil


class UpdateNotification(tk.Toplevel):
    def __init__(self, new_version):
        super().__init__()
        self.title("Update Available")
        self.geometry("300x150")
        self.resizable(False, False)
        
        message = tk.Label(self,
                           text=f"A new version ({new_version}) is available. Do you want to download and install it?")
        message.pack(pady=20)
        
        # 创建两个按钮，一个用于下载更新，一个用于取消更新
        download_button = tk.Button(self, text="Download and Install", command=self.download_and_install_update)
        download_button.pack(side="left", padx=20)
        
        cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.pack(side="right", padx=20)
    
    def download_and_install_update(self):
        self.destroy()
        updater_module = AutoUpdater('1.0.0')
        updater_module.download_update()
        updater_module.install_update()


def get_latest_version():
    # 获取最新版本号
    # TODO: 实现从服务器获取最新版本号的功能
    # 示例返回一个假的版本号
    if platform.system() == 'Windows':
        return '2.0.0'
    elif platform.system() == 'Linux':
        return '1.5.0'
    else:
        return None


def get_download_url():
    # 获取更新包下载链接
    # TODO: 实现从服务器获取更新包下载链接的功能
    # 示例返回一个假的下载链接
    if platform.system() == 'Windows':
        return 'http://73wan.cn/paiwei/update_1.0.0.zip'
    elif platform.system() == 'Linux':
        return 'http://73wan.cn/paiwei/update_1.0.0.zip'
    else:
        return None


def main():
    # 创建 AutoUpdater 对象
    updater_module = AutoUpdater('1.0.0')
    # 检查更新
    if updater_module.check_for_update():
        # 下载并安装更新
        updater_module.download_update()
        updater_module.install_update()
    # 程序继续执行
    ...


import tkinter as tk
import platform
import urllib.request
import zipfile
import os
import shutil


def check_for_update():
    # 检查更新
    latest_version = get_latest_version()  # 获取最新版本号
    current_version = get_current_version()  # 获取当前版本号
    if latest_version > current_version:
        return True
    else:
        return False


def get_current_version():
    # 获取当前版本号
    # TODO: 实现获取当前版本号的功能
    # 示例返回一个假的版本号
    return '1.0.0'


def get_latest_version():
    # 获取最新版本号
    # TODO: 实现从服务器获取最新版本号的功能
    # 示例返回一个假的版本号
    if platform.system() == 'Windows':
        return '2.0.0'
    elif platform.system() == 'Linux':
        return '1.5.0'
    else:
        return None


class UpdateNotification(tk.Toplevel):
    def __init__(self, new_version):
        super().__init__()
        self.title("Update Available")
        self.geometry("300x150")
        self.resizable(False, False)
        
        self.should_update = False  # 初始化 should_update 属性为 False
        
        message = tk.Label(self,
                           text=f"A new version ({new_version}) is available. Do you want to download and install it?")
        message.pack(pady=20)
        
        # 创建两个按钮，一个用于下载更新，一个用于取消更新
        download_button = tk.Button(self, text="Download and Install", command=self.on_download_and_install)
        download_button.pack(side="left", padx=20)
        
        cancel_button = tk.Button(self, text="Cancel", command=self.on_cancel)
        cancel_button.pack(side="right", padx=20)
    
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


class AutoUpdater:
    def __init__(self, version):
        self.version = version
    
    def check_for_update(self):
        # 检查更新
        latest_version = get_latest_version()  # 获取最新版本号
        if latest_version > self.version:
            return True
        else:
            return False
    
    def download_update(self):
        # 下载更新包
        download_url = get_download_url()
        download_path = os.path.join(os.getcwd(), 'update.zip')
        urllib.request.urlretrieve(download_url, download_path, reporthook=self.show_progress)
    
    def install_update(self):
        # 安装更新
        update_url = get_download_url()
        update_path = os.path.join(os.getcwd(), 'update.zip')
        urllib.request.urlretrieve(update_url, update_path, reporthook=self.show_progress)  # 显示下载进度
        backup_path = os.path.join(os.getcwd(), 'backup')
        try:
            # 备份旧文件
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
            shutil.copytree(os.getcwd(), backup_path)
            # 解压缩新文件
            with open(update_path, 'rb') as f:
                with zipfile.ZipFile(f, 'r') as zip_ref:
                    zip_ref.extractall(os.getcwd())
            os.remove(update_path)
            # 重启程序
            self.restart_program()
        except Exception as e:
            # 出现错误，恢复旧文件
            if os.path.exists(backup_path):
                shutil.rmtree(os.getcwd())
                shutil.copytree(backup_path, os.getcwd())
                shutil.rmtree(backup_path)
            raise e
        
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)  # 删除已有的备份文件夹
        shutil.copytree(os.getcwd(), backup_path)  # 备份当前文件夹
        with zipfile.ZipFile(update_path, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())  # 解压更新包到当前文件夹
        shutil.rmtree(update_path)  # 删除更新包
        self.restart_program()
    
    def restart_program(self):
        # 重启程序
        print('Restarting program...')
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    
    def show_progress(self, count, block_size, total_size):
        # 显示下载进度
        percent = int(count * block_size * 100 / total_size)
        print(f"Download progress: {percent}%")


def main():
    updater_module = AutoUpdater('1.0.0')
    if updater_module.check_for_update():
        # 显示更新提示框，让用户选择是否更新
        notification = UpdateNotification(get_latest_version())
        notification.wait_window(notification)
        if notification.should_update:
            updater_module.download_update()
            updater_module.install_update()
    else:
        # 程序继续执行
        ...


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
