# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : todo
# @Time  : 2021/10/26 18:55
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Stats:
    def __init__(self):
        qfile_stats = QFile("../designer/statis.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如： self.ui.button,self.ui.textEdit
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.button1.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()
        count = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            count += line + '\n'

        QMessageBox.about(self.ui, '统计结果', count)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
