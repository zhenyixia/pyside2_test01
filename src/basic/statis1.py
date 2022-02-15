# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : todo
# @Time  : 22/02/16 6:34

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)
button = QPushButton('统计', window)
button.move(380, 80)
window.show()
app.exec_()
