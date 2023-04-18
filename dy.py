import os
import sys

# 将标准输出流重定向到文件中
sys.stdout = open('output.log', 'w')

# 从这里开始，所有的 print() 函数输出都将写入到 output.log 文件中
print('This is a debug message')

# 其他代码
from flask import Flask
app = Flask(__name__)
app.config.from_object("config")

# 使用配置参数
if app.config["DEBUG"]:
    print("Debug mode is on.")

from app import app
from os.path import join, dirname

# 获取 config.py 文件所在目录的绝对路径
config_path = join(dirname(__file__), 'config.py')

# 导入 config 模块
app.config.from_pyfile(config_path)


import platform
from typing import Tuple

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "nan mo e mi tuo fo , jixiang!"

if __name__ == '__main__':
    # Run the app with Gunicorn
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)

# wsgi.py
from app import app

if __name__ == '__main__':
    app.run()

# 使用Gunicorn启动应用程序
wsgi:app

def print_excel_data():
    pass


def print_text():
    pass


def jsonify():
    pass


def PrintJob():
    pass


def PrintJob(job_id, printer_name):
    pass


class Printer:
    def __init__(self, font: str = "Arial", font_size: int = 12, line_spacing: int = 1, letter_spacing: int = 1, style: str = "left", paper_size: str = "A4", custom_paper_size: Tuple[int, int] = (794, 1123)):
        self.mimetype = None
        self.form = None
        self.files = None
        self.font = font
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.letter_spacing = letter_spacing
        self.style = style
        self.paper_size = paper_size
        self.custom_paper_size = custom_paper_size
        self.text = ""
        self.preview_mode = False
        self.log = []
        self.print_queue = []
        self.warning_level = 80
        self.print_settings = {
            "font": font,
            "font_size": font_size,
            "line_spacing": line_spacing,
            "letter_spacing": letter_spacing,
            "style": style,
            "paper_size": paper_size,
            "custom_paper_size": custom_paper_size
        }
        self.bluetooth_enabled = False
        self.bluetooth_address = None
        self.print_drivers = []

        # 根据操作系统自动加载打印驱动程序
        if platform.system() == "Windows":
            self.print_drivers.append("printer_windows.dll")
        elif platform.system() == "Darwin":
            self.print_drivers.append("printer_mac.so")
        else:
            self.print_drivers.append("printer_linux.so")

    def set_font(self, font: str) -> None:
        self.font = font
        self.print_settings["font"] = font

    def set_font_size(self, font_size: int) -> None:
        self.font_size = font_size
        self.print_settings["font_size"] = font_size

    def set_line_spacing(self, line_spacing: int) -> None:
        self.line_spacing = line_spacing
        self.print_settings["line_spacing"] = line_spacing

    def set_letter_spacing(self, letter_spacing: int) -> None:
        self.letter_spacing = letter_spacing
        self.print_settings["letter_spacing"] = letter_spacing

    def set_style(self, style: str) -> None:
        self.style = style
        self.print_settings["style"] = style

    def print_text(self, font_name, font_size, line_spacing, letter_spacing, layout_style, page_range, paper_size,
                   win32com=None):
        # Create print settings object
        ps = win32com.client.Dispatch("Excel.PrintSettings")

        # Set print settings
        ps.LeftMargin = 0
        ps.RightMargin = 0
        ps.TopMargin = 0
        ps.BottomMargin = 0
        ps.HeaderMargin = 0
        ps.FooterMargin = 0
        ps.Header = '&''Helvetica Neu''&12' + self[:20]
        ps.Footer = "&""Helvetica Neu""&12" + self[-20:]
        ps.FitToPagesWide = 1
        ps.FitToPagesTall = 1
        ps.Scale = False

        # Set font and paragraph settings
        fp = ps.FontProperties
        fp.Name = font_name
        fp.Size = font_size
        fp.LineSpacing = line_spacing
        fp.LetterSpacing = letter_spacing
        fp.LayoutMode = layout_style

        # Set paper size
        if paper_size == "A4":
            ps.PaperSize = win32com.client.constants.xlPaperA4
        elif paper_size == "Letter":
            ps.PaperSize = win32com.client.constants.xlPaperLetter

        # Set print range
        ps.PrintArea = page_range

        # Create Excel application object
        xl = win32com.client.Dispatch("Excel.Application")

        # Hide Excel application window
        xl.Visible = False

        # Create new workbook
        wb = xl.Workbooks.Add()

        # Copy text to new workbook
        ws = wb.ActiveSheet
        ws.PageSetup.Orientation = win32com.client.constants.xlPortrait
        ws.PageSetup.CenterHorizontally = True
        ws.PageSetup.CenterVertically = True
        ws.Range("A1").Value = self

        # Print preview
        wb.PrintOut(ps)

        # Close workbook and Excel application
        wb.Close(False)
        xl.Quit()

    def print_excel_folder(self):
        # Loop through all files in folder
        for filename in os.listdir(self):
            if filename.endswith(".xlsx"):
                # Print Excel file
                os.path.join(self, filename)
                print_excel_data()


    @staticmethod
    def print_text(font_name, font_size, line_spacing, letter_spacing, layout_style, page_range, paper_size,
                   logging=None, wb=None, xl=None):
        # Create logger
        logger = logging.getLogger("print_text")
        logger.setLevel(logging.DEBUG)

        # Create print job tuple
        print_job = (text, font_name, font_size, line_spacing, letter_spacing, layout_style, page_range, paper_size)

        # Add print job to self
        self.put(print_job)

    def print_text(text, font_size, line_spacing, letter_spacing, layout_style, win10toast=None):
        # Create toaster
        toaster = win10toast.ToastNotifier()

        # Print settings...
        ...

        # Show notification
        toaster.show_toast("Printing complete", "Your document has finished printing.", duration=10)

    def read_excel_file(file_path, openpyxl=None):
        # Open Excel file
        wb = openpyxl.load_workbook(file_path)

        # Get active worksheet
        ws = wb.active

        # Read text from worksheet
        text = ""
        for row in ws.rows:
            for cell in row:
                text += str(cell.value) + " "
            text += "\n"

        return text

    def print_tex(text, font_name, font_size, line_spacing, letter_spacing, layout_style, page_range, paper_size,
                  win32com=None):
        # Create Word application object
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # Create new document
        doc = word.Documents.Add()

        # Set page size
        if paper_size == "Custom":
            doc.PageSetup.PageWidth = 720  # 10 inches
            doc.PageSetup.PageHeight = 1080  # 15 inches
        else:
            paper_size_constant = getattr(win32com.client.constants, f"wdPaper{paper_size}")
            doc.PageSetup.PageWidth = paper_size_constant.Width
            doc.PageSetup.PageHeight = paper_size_constant.Height

        # Set margins
        doc.PageSetup.LeftMargin = 36  # 0.5 inches
        doc.PageSetup.RightMargin = 36  # 0.5 inches
        doc.PageSetup.TopMargin = 36  # 0.5 inches
        doc.PageSetup.BottomMargin = 36  # 0.5 inches

        # Set header and footer
        header = doc.Sections[0].Headers(win32com.client.constants.wdHeaderFooterPrimary)
        header.Range.Text = "Header"
        footer = doc.Sections[0].Footers(win32com.client.constants.wdHeaderFooterPrimary)
        footer.Range.Text = "Footer"

        # Create font object
        font = doc.Content.Font
        font.Name = font_name
        font.Size = font_size

        # Set line spacing and letter spacing
        para_format = doc.Content.Paragraphs.Format
        para_format.LineSpacing = line_spacing
        para_format.SpaceBefore = 0
        para_format.SpaceAfter = 0
        para_format.CharacterUnitFirstLineIndent = 0
        para_format.CharacterUnitLeftIndent = 0
        para_format.CharacterUnitRightIndent = 0
        para_format.CharacterUnitSpacing = letter_spacing

        # Set layout style
        if layout_style == "Portrait":
            doc.PageSetup.Orientation = win32com.client.constants.wdOrientPortrait
        elif layout_style == "Landscape":
            doc.PageSetup.Orientation = win32com.client.constants.wdOrientLandscape

        # Set page range
        if page_range == "All":
            doc.PrintOut()
        else:
            pages = page_range.split(",")
            for page in pages:
                page = page.strip()
                if "-" in page:
                    start, end = page.split("-")
                    start = int(start)
                    end = int(end)
                    for i in range(start, end + 1):
                        doc.PrintOut(pages=f"{i},{i}")
                else:
                    page = int(page)
                    doc.PrintOut(pages=f"{page},{page}")

        # Close document and Word application
        doc.Close()
        word.Quit()

    def read_word_file(file_path, docx=None):
        # Open Word file
        doc = docx.Document(file_path)

        # Read text from document
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    def print_queue(self, queue=None):
        # Process print jobs until self is empty
        while not queue.empty():
            # Get next print job from self
            print_job = queue.get()

            # Print job
            print_text()


    app = Flask(__name__)

    @app.route('/print', methods=['POST'])
    def print_file(request=None, subprocess=None):
        file = request.files['file']
        printer = request.form['printer']
        file.save('/tmp/' + file.filename)
        subprocess.call(['lp', '-d', printer, '/tmp/' + file.filename])
        return 'Print job submitted'

    if __name__ == '__main__':
        app.run()

    app: object = Flask(__name__)

    @app.route('/cloudprint', methods=['POST'])
    def cloud_print(request=None, requests=None):
        file = request.files['file']
        printer_id = request.form['printer_id']
        content_type = request.mimetype
        headers = {'Authorization': 'Bearer ' + request.form['access_token'],
                   'Content-Type': content_type}
        url = 'https://www.google.com/cloudprint/submit'
        files = {'file': ('file.pdf', file.read(), content_type)}
        params = dict(printerid=printer_id)
        response = requests.post(url, headers=headers, params=params, files=files)
        return response.text

    if __name__ == '__main__':
        app.run()

    app = Flask(__name__)

    @app.route('/google-auth', methods=['GET'])
    def google_auth(self):
        return '''
            <html>
            <head>
                <title>Google Cloud Print Authorization</title>
            </head>
            <body onload="onLoad()">
                <h1>Google Cloud Print Authorization</h1>
                <p>Close this window and return to the application.</p>
            </body>
            <script>
                function onLoad() {
                    var accessToken = window.location.hash.split('&')[0].split('=')[1];
                    window.opener.postMessage({'access_token': accessToken}, '*');
                    window.close();
                }
            </script>
            </html>
        '''

    @app.route('/cloudprint', methods=['POST'])
    def cloud_print(self, request=None, requests=None):
        file = request.files['file']
        printer_id = request.form['printer_id']
        content_type = request.mimetype
        access_token = request.form['access_token']
        headers = {'Authorization': 'Bearer ' + access_token,
                   'Content-Type': content_type}
        url = 'https://www.google.com/cloudprint/submit'
        files = {'file': ('file.pdf', file.read(), content_type)}
        params = {"printer": printer_id}
        response = requests.post(url, headers=headers, params=params, files=files)
        return response.text

    if __name__ == '__main__':
        app.run()

    class PrintStat(object):
        def __init__(self, host, port, user, password, database, pymysql=None):
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )

        def log_print(self, user_id, file_size, print_time):
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO print_logs (user_id, file_size, print_time) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, file_size, print_time))
            self.connection.commit()

        def get_print_stats(self, user_id=None):
            with self.connection.cursor() as cursor:
                if user_id:
                    sql = "SELECT COUNT(*) as count, SUM(file_size) as total_size, AVG(print_time) as avg_time FROM print_logs WHERE user_id=%s"
                    cursor.execute(sql, (user_id,))
                else:
                    sql = "SELECT COUNT(*) as count, SUM(file_size) as total_size, AVG(print_time) as avg_time FROM print_logs"
                    cursor.execute(sql)
                result = cursor.fetchone()
            return result

    def print_excel_folder(folder_path, sheet_name, start_row, start_col, rows_per_page, cols_per_page,
                           print_excel_data=None):
        # Loop through all files in folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".xlsx"):
                # Print Excel file
                file_path = os.path.join(folder_path, filename)
                print_excel_data(file_path, sheet_name, start_row, start_col, rows_per_page, cols_per_page)

    def print_excel_data(file_path, sheet_name, start_row, start_col, rows_per_page, cols_per_page, win32com=None):
        # Load Excel file
        xl = win32com.client.Dispatch("Excel.Application")
        wb = xl.Workbooks.Open(file_path)
        ws = wb.Sheets(sheet_name)

        # Get print area
        print_area = ws.Range(ws.Cells(start_row, start_col),
                              ws.Cells(start_row + rows_per_page - 1, start_col + cols_per_page - 1)).Address

        # Create print settings object
        ps = win32com.client.Dispatch("Excel.PrintSettings")

        # Set print settings
        ps.LeftMargin = 0
        ps.RightMargin = 0
        ps.TopMargin = 0
        ps.BottomMargin = 0
        ps.HeaderMargin = 0
        ps.FooterMargin = 0
        ps.Header = ""
        ps.Footer = ""
        ps.FitToPagesWide = 1
        ps.FitToPagesTall = 1
        ps.Scale = False

        # Set print range
        ps.PrintArea = print_area

        # Create new workbook
        wb2 = xl.Workbooks.Add()

        # Copy worksheet to new workbook
        ws2 = wb2.Worksheets.Add(After=None)
        ws2.Name = sheet_name
        for row in ws.Range(print_area).Rows:
            for cell in row.Cells:
                value = cell.Value
                ws2.Cells(cell.Row, cell.Column).Value = value

        # Print preview
        wb2.PrintOut(ps)

        # Close workbook and Excel application
        wb2.Close(False)
        wb.Close(False)
        xl.Quit()

    def set_paper_size(self, paper_size: str) -> None:
        self.paper_size = paper_size
        self.print_settings["paper_size"] = paper_size

    def set_custom_paper_size(self, width: int, height: int) -> None:
        self.custom_paper_size = (width, height)
        self.print_settings["custom_paper_size"] = (width, height)

    def set_text(self, text: str) -> None:
        self.text = text

    def set_warning_level(self, warning_level: int) -> None:
        self.warning_level = warning_level

    def print_pdf(file_path, printer_name=None, pdfkit=None):
        options = {
            'page-size': 'Letter',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm'
        }
        pdf_file = file_path + '.pdf'
        pdfkit.from_file(file_path, pdf_file, options=options)
        # 调用系统打印程序打印PDF文件
        os.system(f'lpr -P "{printer_name}" "{pdf_file}"')

    class PrintJobQueue:
        def __init__(self):
            self.jobs = {}
            self.next_job_id = 1

        def add_job(self, file_path, printer_name):
            job_id = self.next_job_id
            self.next_job_id += 1
            self.jobs[job_id] = {
                'file_path': file_path,
                'printer_name': printer_name,
                'status': 'queued'
            }
            return job_id

        def get_job_list(self):
            return self.jobs

        def cancel_job(self, job_id):
            if job_id in self.jobs:
                self.jobs[job_id]['status'] = 'canceled'
                return True
            else:
                return False

        def requeue_job(self, job_id):
            if job_id in self.jobs:
                self.jobs[job_id]['status'] = 'queued'
                return True
            else:
                return False

    print_job_queue = PrintJobQueue()

    def handle_print_job(self, request=None, print_job_queue=None):
        # 获取要打印的文件路径和打印机名称
        file_path = request.form['file_path']
        printer_name = request.form['printer_name']

        # 添加新的打印作业到队列中
        job_id = print_job_queue.add_job(file_path, printer_name)

        # 返回作业ID和成功消息
        response_data = {'job_id': job_id, 'message': 'Print job added to queue.'}
        return jsonify(), 200

    @app.route('/print-job-queue/<int:job_id>/cancel', methods=['POST'])
    def cancel_print_job(job_id, print_job_queue=None):
        success = print_job_queue.cancel_job(job_id)
        if success:
            return 'Print job canceled.', 200
        else:
            return 'Print job not found.', 404

    class PrintJob:
        def __init__(self, job_id, file_path, printer_name):
            self.job_id = job_id
            self.file_path = file_path
            self.printer_name = printer_name
            self.status = 'queued'

    class PrintJobQueue:
        def __init__(self):
            self.jobs = []
            self.current_job_id = 0

        def add_job(self, file_path, printer_name):
            job_id = self.current_job_id
            self.current_job_id += 1
            job = PrintJob()
            self.jobs.append(job)
            return job_id

        def cancel_job(self, job_id):
            for job in self.jobs:
                if job.job_id == job_id and job.status == 'queued':
                    job.status = 'canceled'
                    return True
            return False

        def requeue_job(self, job_id):
            for job in self.jobs:
                if job.job_id == job_id and job.status == 'canceled':
                    job.status = 'queued'
                    return True
            return False

    print_job_queue = PrintJobQueue()

    import cups

    conn = cups.Connection()

    # 获取可用打印机列表
    printer_list = conn.getPrinters()
    # 获取第一个打印机的名称
    printer_name = list(printer_list.keys())[0]

    # 设置纸张大小和打印质量
    options = {'media': paper_size, 'print-quality': print_quality}

    # 执行打印作业
    conn.printFile(printer_name, file_path, '', options=options)

    def preview(self, pages=None, bluetooth=None) -> None:
        self.preview_mode = True
        self.print()

        class PrintJob:
            def __init__(self, text, font="Arial", font_size=12, line_spacing=1, letter_spacing=1, style="left",
                         paper_size="A4", custom_paper_size=(794, 1123), orientation="portrait"):
                self.text = text
                self.font = font
                self.font_size = font_size
                self.line_spacing = line_spacing
                self.letter_spacing = letter_spacing
                self.style = style
                self.paper_size = paper_size
                self.custom_paper_size = custom_paper_size
                self.orientation = orientation
                self.print_drivers = ["win32print.py", "cups.py"]
                self.log = []

            def print(self):
                # 支持的纸张大小和对应的像素大小
                global indent
                paper_sizes = {
                    "A4": (794, 1123),
                    "A3": (1123, 1587),
                    "Letter": (792, 1224),
                    "Legal": (792, 1239)
                }

                # 支持的纸张方向
                orientations = {
                    "portrait": 0,
                    "landscape": 1
                }

        def print_text(text: str, font: str = "Arial", font_size: int = 12, line_spacing: int = 1,
                           letter_spacing: int = 1, style: str = "left", page_size: Tuple[int, int] = (80, 24),
                           paper_size: str = "custom", custom_paper_size: Tuple[int, int] = (794, 1123)) -> None:

            class PrintJob:
                def __init__(self, text, font="Arial", font_size=12, line_spacing=1, letter_spacing=1, style="left",
                             paper_size="A4", custom_paper_size=(794, 1123), orientation="portrait"):
                    self.text = text
                    self.font = font
                    self.font_size = font_size
                    self.line_spacing = line_spacing
                    self.letter_spacing = letter_spacing
                    self.style = style
                    self.paper_size = paper_size
                    self.custom_paper_size = custom_paper_size
                    self.orientation = orientation
                    self.print_drivers = ["win32print.py", "cups.py"]
                    self.log = []

            # 支持的纸张大小和对应的像素大小
            global indent
            paper_sizes = {
                "A4": (794, 1123),
                "A3": (1123, 1587),
                "Letter": (792, 1224),
                "Legal": (792, 1536)
            }
            # 支持的纸张方向
            orientations = {
                "portrait": 0,
                "landscape": 1
            }
            # 自定义纸张大小
            if paper_size == "custom":
                page_size = custom_paper_size
            elif paper_size not in paper_sizes:
                raise ValueError(
                        "Invalid paper size parameter. Valid values are 'A4', 'A3', 'Letter', 'Legal', and 'custom'.")
            else:
                page_size = paper_sizes[paper_size]
                # 字符串按行分割
                lines = text.split('\n')
                # 计算每行最大长度
                max_line_length = max([len(line) for line in lines])
                # 计算打印区域大小
                printable_area = (page_size[0] - 2, page_size[1] - 2)
                # 计算每个字符的大小
                char_size = (font_size, int(font_size * 0.6))
                # 计算每行最多容纳的字符数
                max_chars_per_line = printable_area[0] // char_size[1]
                # 计算每页最多容纳的行数
                max_lines_per_page = printable_area[1] // char_size[0]
                # 计算每页最多容纳的字符数
                max_chars_per_page = max_chars_per_line * max_lines_per_page
                # 将文本分割为多页
                pages = [lines[i:i + max_lines_per_page] for i in range(0, len(lines), max_lines_per_page)]
                # 遍历每页
                for page_num, page in enumerate(pages):
                    # 打印页码
                    print(f"Page {page_num + 1}/{len(pages)}")
                    # 遍历每行
                    for line in page:
                        # 计算行首空格数
                        if style == "left":
                            padding = 0
                        elif style == "center":
                            padding = (max_chars_per_line - len(line)) // 2
                        elif style == "right":
                            padding = max_chars_per_line - len(line)
                        else:
                            raise ValueError("Invalid style parameter. Valid values are 'left', 'center', and 'right'.")
                        # 打印每个字符
                        for char in line:
                            # 打印空格
                            for i in range(padding):
                                print(" " * char_size[1])
                            # 打印字符
                            print(char)
                            # 打印字距
                            print(" " * letter_spacing)
                            # 打印行距
                            print("\n" * line_spacing)

                        # 计算打印区域大小
            if self.paper_size == "Custom":
                width, height = self.custom_paper_size
            else:
                width, height = paper_sizes[self.paper_size]

            # 计算每行字数和每页行数
            char_width = self.font_size // 2
            line_width = (width // char_width) - self.letter_spacing
            lines_per_page = (height // self.font_size) - self.line_spacing

            # 根据样式计算缩进量
            if self.style == "left":
                indent = 0
            elif self.style == "center":
                indent = (line_width - len(self.text)) // 2
            elif self.style == "right":
                indent = line_width - len(self.text)

            # 拆分文本为多页
            pages = []
            while len(self.text) > 0:
                lines = self.text.split("\n")
                page = []
                line_count = 0
                for line in lines:
                    while len(line) > 0:
                        page.append(line[:line_width])
                        line = line[line_width:]
                        line_count += 1
                        if line_count >= lines_per_page:
                            break
                    if line_count >= lines_per_page:
                        break
                pages.append(page)
                self.text = "\n".join(lines[line_count:])

            # 打印每页
            for i, page in enumerate(pages):
                # 构造打印数据
                data = f"{self.font},{self.font_size},{self.line_spacing},{self.letter_spacing},{self.style},{width},{height}\n"
                for line in page:
                    data += " " * indent + line + "\n"
                data += "-" * line_width + "\n"
                if self.preview_mode:
                    print(data)
                else:
                    # 调用打印驱动程序
                    for driver in self.print_drivers:
                        try:
                            driver_module = __import__(driver[:-3])
                            driver_module.print_data(data)
                            break
                        except ImportError:
                            pass
                    else:
                        print(f"No print driver found for {platform.system()}.")

            # 打印日志
            self.log.append(f"Printed {len(pages)} pages.")
            if len(self.print_queue) > 0:
                self.print_queue.pop(0)
                self.log.append("Job completed and removed from self.")
            elif len(self.text) > 0:
                self.log.append("Text partially printed.")
            else:
                self.log.append("Print job completed.")

        # 连接蓝牙打印机并打印
        if self.bluetooth_enabled and self.bluetooth_address is not None:
            try:
                port = 1
                socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                socket.connect((self.bluetooth_address, port))
                socket.send(data.encode())
                socket.close()
            except bluetooth.BluetoothError as e:
                self.log.append(f"Bluetooth printing failed: {str(e)}")

        # 打印预警信息
        if len(self.text) > 0 and len(self.text) / len(pages[0]) > self.warning_level / 100:
            self.log.append(f"Warning: {self.warning_level}% of paper used.")

    def enable_bluetooth(self) -> None:
        self.bluetooth_enabled = True

    def disable_bluetooth(self) -> None:
        self.bluetooth_enabled = False

    def set_bluetooth_address(self, address: str) -> None:
        self.bluetooth_address = address

    def add_print_driver(self, driver: str) -> None:
        self.print_drivers.append(driver)

    def remove_print_driver(self, driver: str) -> None:
        self.print_drivers.remove(driver)

    def empty(self):
        pass

    def get(self):
        pass

    def put(self, print_job):
        pass

    def print_queue_summary(self):
        pass

    def print(self):
        pass

    def add_to_print_queue(self):
        pass


def print_text(font_name, font_size, line_spacing, letter_spacing, layout_style, page_range, paper_size,
               logging=None, wb=None, xl=None):

    # Create logger
    logger = logging.getLogger("print_text")
    logger.setLevel(logging.DEBUG)

    # Create file handler
    fh = logging.FileHandler("print_log.txt")
    fh.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(pastime)s - %(name)s - %(levelness)s - %(message)s')
    fh.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(fh)

    # Log print settings
    logger.info("Font name: %s", font_name)
    logger.info("Font size: %d", font_size)
    logger.info("Line spacing: %d", line_spacing)
    logger.info("Letter spacing: %d", letter_spacing)
    logger.info("Layout style: %s", layout_style)
    logger.info("Page range: %s", page_range)
    logger.info("Paper size: %s", paper_size)

    # Create print settings object


    # Log print success
    logger.info("Print successful")

    # Close workbook and Excel application
    wb.Close(False)
    xl.Quit()


# 示例用法
printer = Printer()
printer.set_text("Hello, world!")
printer.set_font_size(16)
printer.set_style("center")
printer.set_paper_size("Letter")
printer.preview()

printer.set_text("This is a long text that will be split into multiple pages. ")
printer.set_text("It will also exceed the warning level of 80%.")
printer.set_warning_level(80)
printer.add_to_print_queue()

printer.set_text("This is another print job.")
printer.set_font_size(12)
printer.add_to_print_queue()

print(printer.print_queue_summary())

printer.print()

printer.enable_bluetooth()
printer.set_bluetooth_address("00:11:22:33:44:55")
printer.print()

printer.add_print_driver("printer_custom.so")
# 增加适配打印机列表功能
class Printer:
    def __init__(self, font: str = "Arial", font_size: int = 12, line_spacing: int = 1, letter_spacing: int = 1, style: str = "left", paper_size: str = "A4", custom_paper_size: Tuple[int, int] = (794, 1123)):
        self.font = font
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.letter_spacing = letter_spacing
        self.style = style
        self.paper_size = paper_size
        self.custom_paper_size = custom_paper_size
        self.text = ""
        self.preview_mode = False
        self.log = []
        self.print_queue = []
        self.warning_level = 80
        self.print_settings = {
            "font": font,
            "font_size": font_size,
            "line_spacing": line_spacing,
            "letter_spacing": letter_spacing,
            "style": style,
            "paper_size": paper_size,
            "custom_paper_size": custom_paper_size
        }
        self.bluetooth_enabled = False
        self.bluetooth_address = None
        self.print_drivers = []
        import subprocess

        # 显示已安装的驱动程序列表
        def get_installed_drivers():
            drivers = []
            cmd = 'pnputil.exe -e'
            output = subprocess.run(cmd, shell=True, capture_output=True)
            if output.returncode == 0:
                for line in output.stdout.decode().split('\r\n'):
                    if 'Published name' in line:
                        drivers.append(line.split(':')[1].strip())
            return drivers

        # 安装驱动程序
        def install_driver(driver_path):
            cmd = f'psutil.exe -i -a "{driver_path}"'
            subprocess.run(cmd, shell=True)

        # 删除驱动程序
        def remove_driver(driver_name):
            cmd = f'pnputil.exe -d "{driver_name}"'
            subprocess.run(cmd, shell=True)

        # 更新驱动程序
        def update_driver(driver_path):
            driver_name = os.path.basename(driver_path)
            if driver_name in get_installed_drivers():
                remove_driver(driver_name)
            install_driver(driver_path)


        # 安装驱动程序
        def install_driver(driver_path):
            cmd = f'pnputil.exe -i -a "{driver_path}"'
            subprocess.run(cmd, shell=True)

        # 删除驱动程序
        def remove_driver(driver_name):
            cmd = f'pnputil.exe -d "{driver_name}"'
            subprocess.run(cmd, shell=True)
        # 根据操作系统自动加载打印驱动程序
        if platform.system() == "Windows":
            self.print_drivers.append("printer_windows.dll")
        elif platform.system() == "Darwin":
            self.print_drivers.append("printer_mac.so")
        else:
            self.print_drivers.append("printer_linux.so")

    def set_font(self, font: str) -> None:
        self.font = font
        self.print_settings["font"] = font

    def set_font_size(self, font_size: int) -> None:
        self.font_size = font_size
        self.print_settings["font_size"] = font_size

    def set_line_spacing(self, line_spacing: int) -> None:
        self.line_spacing = line_spacing
        self.print_settings["line_spacing"] = line_spacing

    def set_letter_spacing(self, letter_spacing: int) -> None:
        self.letter_spacing = letter_spacing
        self.print_settings["letter_spacing"] = letter_spacing

    def set_style(self, style: str) -> None:
        self.style = style
        self.print_settings["style"] = style

    def set_paper_size(self, paper_size: str) -> None:
        self.paper_size = paper_size
        self.print_settings["paper_size"] = paper_size

    def set_custom_paper_size(self, width: int, height: int) -> None:
        self.custom_paper_size = (width, height)
        self.print_settings["custom_paper_size"] = (width, height)

    def set_text(self, text: str) -> None:
        self.text = text

    def set_warning_level(self, warning_level: int) -> None:
        self.warning_level = warning_level

    def preview(self) -> None:
        self.preview_mode = True
        self.print()

    def add_to_print_queue(self) -> None:
        self.print_queue.append(self.print_settings)

    def print_queue_summary(self) -> str:
        summary = f"Number of jobs in print self: {len(self.print_queue)}\n"
        for i, job in enumerate(self.print_queue):
            summary += f"Job {i+1}:\n"
            for key, value in job.items():
                summary += f"    {key}: {value}\n"
        return summary

    def print(self) -> None:
        # 支持的纸张大小和对应的像素大小
        global data, indent


        # 适配打印机列表
        available_printers = []
        for driver in self.print_drivers:
            try:
                driver_module = __import__(driver[:-3])
                available_printers.extend(driver_module.get_available_printers())
            except ImportError:
                pass

        self.log.append(f"Available printers: {', '.join(available_printers)}")

    def enable_bluetooth(self) -> None:
        self.bluetooth_enabled = True

    def disable_bluetooth(self) -> None:
        self.bluetooth_enabled = False

    def set_bluetooth_address(self, address: str) -> None:
        self.bluetooth_address = address

    def add_print_driver(self, driver: str) -> None:
        self.print_drivers.append(driver)

    def remove_print_driver(self, driver: str) -> None:
        self.print_drivers.remove(driver)

