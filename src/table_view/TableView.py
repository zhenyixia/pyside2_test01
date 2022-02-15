# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : todo
# @Time  : 2021/10/25 6:18
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TableView(QMainWindow):
    def __init__(self, arg=None):
        super(TableView, self).__init__(arg)

        self.setWindowTitle("QTableView 表格视图控件演示")

        self.resize(500, 300)

        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])

        # 关联model
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 添加数据
        item00 = QStandardItem('1')
        item01 = QStandardItem('姓名0')
        item02 = QStandardItem('年龄0')

        item30 = QStandardItem('30')
        item31 = QStandardItem('姓名3')
        item32 = QStandardItem('年龄3')

        self.model.setItem(0, 0, item00)
        self.model.setItem(0, 1, item01)
        self.model.setItem(0, 2, item02)

        self.model.setItem(3, 0, item30)
        self.model.setItem(3, 1, item31)
        self.model.setItem(3, 2, item32)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        # 创建主框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        # 设置主框架居中
        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())
