# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 在指定文件，指定代码行，添加一些指定代码
# @Time  : 2021/10/23 8:57


def insert_codes(file_name):
    file = open(file_name, mode='a+', encoding='utf-8')
    codes = """

    import sys
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        widget = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(widget)
        widget.show()
        sys.exit(app.exec_())

    """
    file.writelines(codes)
    file.close()


if __name__ == '__main__':
    import sys

    file_name = sys.argv[0]

    insert_codes(file_name)
