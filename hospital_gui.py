# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CMMS.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 784)
        MainWindow.setMinimumSize(QtCore.QSize(850, 784))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(
            self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 794, 586))
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.followUp_tabWidget = QtWidgets.QTabWidget(
            self.page)
        self.followUp_tabWidget.setIconSize(
            QtCore.QSize(100, 50))
        self.followUp_tabWidget.setDocumentMode(True)
        self.followUp_tabWidget.setMovable(True)
        self.followUp_tabWidget.setTabBarAutoHide(False)
        self.followUp_tabWidget.setObjectName(
            "followUp_tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(
            self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_29 = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.DashTasksCount_label = QtWidgets.QLabel(
            self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DashTasksCount_label.sizePolicy(
            ).hasHeightForWidth())
        self.DashTasksCount_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashTasksCount_label.setFont(font)
        self.DashTasksCount_label.setObjectName(
            "DashTasksCount_label")
        self.gridLayout_10.addWidget(self.splitter_2, 1, 1,
                                     1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.groupBox_3)
        self.verticalLayout_3.setObjectName(
            "verticalLayout_3")
        self.Search_lineEdit = QtWidgets.QLineEdit(
            self.groupBox_3)
        self.Search_lineEdit.setObjectName("Search_lineEdit")
        self.verticalLayout_3.addWidget(self.Search_lineEdit)
        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0,
                                     1, 5)
        self.splitter_5 = QtWidgets.QSplitter(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_35 = QtWidgets.QLabel(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.DashDepatmentsCount_label = QtWidgets.QLabel(
            self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DashDepatmentsCount_label.sizePolicy(
            ).hasHeightForWidth())
        self.DashDepatmentsCount_label.setSizePolicy(
            sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashDepatmentsCount_label.setFont(font)
        self.DashDepatmentsCount_label.setObjectName(
            "DashDepatmentsCount_label")
        self.gridLayout_10.addWidget(self.splitter_5, 1, 3,
                                     1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_31 = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.DashDevicesCount_label = QtWidgets.QLabel(
            self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DashDevicesCount_label.sizePolicy(
            ).hasHeightForWidth())
        self.DashDevicesCount_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashDevicesCount_label.setFont(font)
        self.DashDevicesCount_label.setObjectName(
            "DashDevicesCount_label")
        self.gridLayout_10.addWidget(self.splitter_3, 1, 2,
                                     1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_33 = QtWidgets.QLabel(self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.DashFormsCount_label = QtWidgets.QLabel(
            self.splitter_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DashFormsCount_label.sizePolicy(
            ).hasHeightForWidth())
        self.DashFormsCount_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashFormsCount_label.setFont(font)
        self.DashFormsCount_label.setObjectName(
            "DashFormsCount_label")
        self.gridLayout_10.addWidget(self.splitter_4, 1, 4,
                                     1, 1)
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_25 = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.DashToDoCount_label = QtWidgets.QLabel(
            self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DashToDoCount_label.sizePolicy(
            ).hasHeightForWidth())
        self.DashToDoCount_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashToDoCount_label.setFont(font)
        self.DashToDoCount_label.setObjectName(
            "DashToDoCount_label")
        self.gridLayout_10.addWidget(self.splitter, 1, 0, 1,
                                     1)
        self.Dash_Inspection_Button = QtWidgets.QPushButton(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Dash_Inspection_Button.sizePolicy(
            ).hasHeightForWidth())
        self.Dash_Inspection_Button.setSizePolicy(sizePolicy)
        self.Dash_Inspection_Button.setMinimumSize(
            QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dash_Inspection_Button.setFont(font)
        self.Dash_Inspection_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("Resources/images/paste.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Dash_Inspection_Button.setIcon(icon)
        self.Dash_Inspection_Button.setIconSize(
            QtCore.QSize(50, 100))
        self.Dash_Inspection_Button.setFlat(True)
        self.Dash_Inspection_Button.setObjectName(
            "Dash_Inspection_Button")
        self.gridLayout_10.addWidget(
            self.Dash_Inspection_Button, 2, 4, 1, 1)
        self.Dash_Dept_Button = QtWidgets.QPushButton(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Dash_Dept_Button.sizePolicy(
            ).hasHeightForWidth())
        self.Dash_Dept_Button.setSizePolicy(sizePolicy)
        self.Dash_Dept_Button.setMinimumSize(
            QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dash_Dept_Button.setFont(font)
        self.Dash_Dept_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dash_Dept_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "Resources/images/black-placeholder-variant.png"
            ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Dash_Dept_Button.setIcon(icon1)
        self.Dash_Dept_Button.setIconSize(
            QtCore.QSize(50, 100))
        self.Dash_Dept_Button.setFlat(True)
        self.Dash_Dept_Button.setObjectName(
            "Dash_Dept_Button")
        self.gridLayout_10.addWidget(self.Dash_Dept_Button,
                                     2, 3, 1, 1)
        self.Dash_Devices_Button = QtWidgets.QPushButton(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Dash_Devices_Button.sizePolicy(
            ).hasHeightForWidth())
        self.Dash_Devices_Button.setSizePolicy(sizePolicy)
        self.Dash_Devices_Button.setMinimumSize(
            QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dash_Devices_Button.setFont(font)
        self.Dash_Devices_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dash_Devices_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(
                "Resources/images/monitor-tool-symbol.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Dash_Devices_Button.setIcon(icon2)
        self.Dash_Devices_Button.setIconSize(
            QtCore.QSize(50, 100))
        self.Dash_Devices_Button.setFlat(True)
        self.Dash_Devices_Button.setObjectName(
            "Dash_Devices_Button")
        self.gridLayout_10.addWidget(
            self.Dash_Devices_Button, 2, 2, 1, 1)
        self.Dash_Forms_Button = QtWidgets.QPushButton(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Dash_Forms_Button.sizePolicy(
            ).hasHeightForWidth())
        self.Dash_Forms_Button.setSizePolicy(sizePolicy)
        self.Dash_Forms_Button.setMinimumSize(
            QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dash_Forms_Button.setFont(font)
        self.Dash_Forms_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dash_Forms_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("Resources/images/check.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Dash_Forms_Button.setIcon(icon3)
        self.Dash_Forms_Button.setIconSize(
            QtCore.QSize(50, 100))
        self.Dash_Forms_Button.setFlat(True)
        self.Dash_Forms_Button.setObjectName(
            "Dash_Forms_Button")
        self.gridLayout_10.addWidget(self.Dash_Forms_Button,
                                     2, 1, 1, 1)
        self.Dash_ToDo_Button = QtWidgets.QPushButton(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Dash_ToDo_Button.sizePolicy(
            ).hasHeightForWidth())
        self.Dash_ToDo_Button.setSizePolicy(sizePolicy)
        self.Dash_ToDo_Button.setMinimumSize(
            QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dash_ToDo_Button.setFont(font)
        self.Dash_ToDo_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("Resources/images/list.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Dash_ToDo_Button.setIcon(icon4)
        self.Dash_ToDo_Button.setIconSize(
            QtCore.QSize(50, 100))
        self.Dash_ToDo_Button.setFlat(True)
        self.Dash_ToDo_Button.setObjectName(
            "Dash_ToDo_Button")
        self.gridLayout_10.addWidget(self.Dash_ToDo_Button,
                                     2, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.calendarWidget = QtWidgets.QCalendarWidget(
            self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.calendarWidget.sizePolicy(
            ).hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(
            QtCore.QSize(750, 300))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_8.addWidget(self.calendarWidget, 0,
                                    0, 1, 1,
                                    QtCore.Qt.AlignHCenter)
        self.gridLayout_10.addLayout(self.gridLayout_8, 3, 0,
                                     1, 5)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("Resources/images/home.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.followUp_tabWidget.addTab(self.tab_2, icon5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ToDo_table = QtWidgets.QTableWidget(self.tab)
        self.ToDo_table.setAlternatingRowColors(True)
        self.ToDo_table.setGridStyle(QtCore.Qt.SolidLine)
        self.ToDo_table.setCornerButtonEnabled(False)
        self.ToDo_table.setRowCount(10)
        self.ToDo_table.setObjectName("ToDo_table")
        self.ToDo_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ToDo_table.setItem(2, 3, item)
        self.ToDo_table.horizontalHeader(
        ).setStretchLastSection(True)
        self.ToDo_table.verticalHeader().setVisible(False)
        self.ToDo_table.verticalHeader(
        ).setSortIndicatorShown(True)
        self.ToDo_table.verticalHeader(
        ).setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.ToDo_table, 1, 0, 1,
                                    1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(
            self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Export_button = QtWidgets.QPushButton(
            self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Export_button.sizePolicy(
            ).hasHeightForWidth())
        self.Export_button.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("Resources/images/export.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export_button.setIcon(icon6)
        self.Export_button.setObjectName("Export_button")
        self.gridLayout_5.addWidget(self.Export_button, 0, 1,
                                    1, 1)
        self.Date_comboBox = QtWidgets.QComboBox(
            self.groupBox)
        self.Date_comboBox.setObjectName("Date_comboBox")
        self.Date_comboBox.addItem("")
        self.Date_comboBox.addItem("")
        self.Date_comboBox.addItem("")
        self.gridLayout_5.addWidget(self.Date_comboBox, 0, 0,
                                    1, 1)
        self.Print_button = QtWidgets.QPushButton(
            self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Print_button.sizePolicy().hasHeightForWidth(
            ))
        self.Print_button.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(
                "Resources/images/document-rounded-square-interface-symbol-with-text-lines.png"
            ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Print_button.setIcon(icon7)
        self.Print_button.setObjectName("Print_button")
        self.gridLayout_5.addWidget(self.Print_button, 0, 2,
                                    1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1,
                                    1)
        self.followUp_tabWidget.addTab(self.tab, icon4, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.tab_8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(
            self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dateEdit_inspection = QtWidgets.QDateEdit(
            self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit_inspection.sizePolicy(
            ).hasHeightForWidth())
        self.dateEdit_inspection.setSizePolicy(sizePolicy)
        self.dateEdit_inspection.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2020, 5, 20),
                             QtCore.QTime(0, 0, 0)))
        self.dateEdit_inspection.setMinimumDate(
            QtCore.QDate(2015, 9, 14))
        self.dateEdit_inspection.setCalendarPopup(True)
        self.dateEdit_inspection.setObjectName(
            "dateEdit_inspection")
        self.gridLayout_6.addWidget(self.dateEdit_inspection,
                                    0, 1, 1, 1)
        self.CheckAll_checkBox = QtWidgets.QCheckBox(
            self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CheckAll_checkBox.sizePolicy(
            ).hasHeightForWidth())
        self.CheckAll_checkBox.setSizePolicy(sizePolicy)
        self.CheckAll_checkBox.setObjectName(
            "CheckAll_checkBox")
        self.gridLayout_6.addWidget(self.CheckAll_checkBox,
                                    0, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(
            "horizontalLayout_7")
        self.Inspection_comboBox = QtWidgets.QComboBox(
            self.groupBox_2)
        self.Inspection_comboBox.setObjectName(
            "Inspection_comboBox")
        self.Inspection_comboBox.addItem("")
        self.Inspection_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(
            self.Inspection_comboBox)
        self.Inspection_comboBox_Dep_comboBox = QtWidgets.QComboBox(
            self.groupBox_2)
        self.Inspection_comboBox_Dep_comboBox.setObjectName(
            "Inspection_comboBox_Dep_comboBox")
        self.horizontalLayout_7.addWidget(
            self.Inspection_comboBox_Dep_comboBox)
        self.gridLayout_6.addLayout(self.horizontalLayout_7,
                                    0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.line_10 = QtWidgets.QFrame(self.tab_8)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout.addWidget(self.line_10)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.q8 = QtWidgets.QLabel(self.tab_8)
        self.q8.setObjectName("q8")
        self.gridLayout_7.addWidget(self.q8, 14, 0, 1, 1)
        self.q10 = QtWidgets.QLabel(self.tab_8)
        self.q10.setObjectName("q10")
        self.gridLayout_7.addWidget(self.q10, 18, 0, 1, 1)
        self.q5 = QtWidgets.QLabel(self.tab_8)
        self.q5.setObjectName("q5")
        self.gridLayout_7.addWidget(self.q5, 8, 0, 1, 1)
        self.checkq7 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq7.sizePolicy().hasHeightForWidth())
        self.checkq7.setSizePolicy(sizePolicy)
        self.checkq7.setObjectName("checkq7")
        self.gridLayout_7.addWidget(self.checkq7, 12, 2, 1,
                                    1)
        self.checkq10 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq10.sizePolicy().hasHeightForWidth())
        self.checkq10.setSizePolicy(sizePolicy)
        self.checkq10.setObjectName("checkq10")
        self.gridLayout_7.addWidget(self.checkq10, 18, 2, 1,
                                    1)
        self.q7 = QtWidgets.QLabel(self.tab_8)
        self.q7.setObjectName("q7")
        self.gridLayout_7.addWidget(self.q7, 12, 0, 1, 1)
        self.checkq2 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq2.sizePolicy().hasHeightForWidth())
        self.checkq2.setSizePolicy(sizePolicy)
        self.checkq2.setObjectName("checkq2")
        self.gridLayout_7.addWidget(self.checkq2, 2, 2, 1, 1)
        self.q1 = QtWidgets.QLabel(self.tab_8)
        self.q1.setObjectName("q1")
        self.gridLayout_7.addWidget(self.q1, 0, 0, 1, 1)
        self.q2 = QtWidgets.QLabel(self.tab_8)
        self.q2.setObjectName("q2")
        self.gridLayout_7.addWidget(self.q2, 2, 0, 1, 1)
        self.checkq9 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq9.sizePolicy().hasHeightForWidth())
        self.checkq9.setSizePolicy(sizePolicy)
        self.checkq9.setObjectName("checkq9")
        self.gridLayout_7.addWidget(self.checkq9, 16, 2, 1,
                                    1)
        self.checkq8 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq8.sizePolicy().hasHeightForWidth())
        self.checkq8.setSizePolicy(sizePolicy)
        self.checkq8.setObjectName("checkq8")
        self.gridLayout_7.addWidget(self.checkq8, 14, 2, 1,
                                    1)
        self.line_9 = QtWidgets.QFrame(self.tab_8)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_7.addWidget(self.line_9, 17, 0, 1, 1)
        self.checkq1 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq1.sizePolicy().hasHeightForWidth())
        self.checkq1.setSizePolicy(sizePolicy)
        self.checkq1.setObjectName("checkq1")
        self.gridLayout_7.addWidget(self.checkq1, 0, 2, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.tab_8)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_7.addWidget(self.line_8, 15, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 3, 0, 1, 1)
        self.q3 = QtWidgets.QLabel(self.tab_8)
        self.q3.setObjectName("q3")
        self.gridLayout_7.addWidget(self.q3, 4, 0, 1, 1)
        self.q6 = QtWidgets.QLabel(self.tab_8)
        self.q6.setObjectName("q6")
        self.gridLayout_7.addWidget(self.q6, 10, 0, 1, 1)
        self.checkq3 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq3.sizePolicy().hasHeightForWidth())
        self.checkq3.setSizePolicy(sizePolicy)
        self.checkq3.setObjectName("checkq3")
        self.gridLayout_7.addWidget(self.checkq3, 4, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab_8)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_7.addWidget(self.line_3, 5, 0, 1, 1)
        self.SubmitInspectionAnswers_button = QtWidgets.QPushButton(
            self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SubmitInspectionAnswers_button.sizePolicy(
            ).hasHeightForWidth())
        self.SubmitInspectionAnswers_button.setSizePolicy(
            sizePolicy)
        self.SubmitInspectionAnswers_button.setObjectName(
            "SubmitInspectionAnswers_button")
        self.gridLayout_7.addWidget(
            self.SubmitInspectionAnswers_button, 19, 2, 1, 1)
        self.line_1 = QtWidgets.QFrame(self.tab_8)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.gridLayout_7.addWidget(self.line_1, 1, 0, 1, 1)
        self.checkq4 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq4.sizePolicy().hasHeightForWidth())
        self.checkq4.setSizePolicy(sizePolicy)
        self.checkq4.setObjectName("checkq4")
        self.gridLayout_7.addWidget(self.checkq4, 6, 2, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.tab_8)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_7.addWidget(self.line_7, 13, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_8)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_7.addWidget(self.line_4, 7, 0, 1, 1)
        self.q9 = QtWidgets.QLabel(self.tab_8)
        self.q9.setObjectName("q9")
        self.gridLayout_7.addWidget(self.q9, 16, 0, 1, 1)
        self.q4 = QtWidgets.QLabel(self.tab_8)
        self.q4.setObjectName("q4")
        self.gridLayout_7.addWidget(self.q4, 6, 0, 1, 1)
        self.checkq5 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq5.sizePolicy().hasHeightForWidth())
        self.checkq5.setSizePolicy(sizePolicy)
        self.checkq5.setObjectName("checkq5")
        self.gridLayout_7.addWidget(self.checkq5, 8, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab_8)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_7.addWidget(self.line_6, 11, 0, 1, 1)
        self.checkq6 = QtWidgets.QCheckBox(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq6.sizePolicy().hasHeightForWidth())
        self.checkq6.setSizePolicy(sizePolicy)
        self.checkq6.setObjectName("checkq6")
        self.gridLayout_7.addWidget(self.checkq6, 10, 2, 1,
                                    1)
        self.line_5 = QtWidgets.QFrame(self.tab_8)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_7.addWidget(self.line_5, 9, 0, 1, 1)
        self.deleteInspection_button = QtWidgets.QPushButton(
            self.tab_8)
        self.deleteInspection_button.setObjectName(
            "deleteInspection_button")
        self.gridLayout_7.addWidget(
            self.deleteInspection_button, 20, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(
            "horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.insp_notes = QtWidgets.QTextEdit(self.tab_8)
        self.insp_notes.setObjectName("insp_notes")
        self.horizontalLayout.addWidget(self.insp_notes)
        self.gridLayout_7.addLayout(self.horizontalLayout,
                                    19, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.line_11 = QtWidgets.QFrame(self.tab_8)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.followUp_tabWidget.addTab(self.tab_8, icon3, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.tab_3)
        self.verticalLayout_5.setObjectName(
            "verticalLayout_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(
            self.groupBox_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.dateEdit_ppm = QtWidgets.QDateEdit(
            self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit_ppm.sizePolicy().hasHeightForWidth(
            ))
        self.dateEdit_ppm.setSizePolicy(sizePolicy)
        self.dateEdit_ppm.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2020, 5, 20),
                             QtCore.QTime(0, 0, 0)))
        self.dateEdit_ppm.setMinimumDate(
            QtCore.QDate(2015, 9, 14))
        self.dateEdit_ppm.setCalendarPopup(True)
        self.dateEdit_ppm.setObjectName("dateEdit_ppm")
        self.gridLayout_14.addWidget(self.dateEdit_ppm, 1, 2,
                                     1, 1)
        self.MarkAsDone_checkBox_3 = QtWidgets.QCheckBox(
            self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MarkAsDone_checkBox_3.sizePolicy(
            ).hasHeightForWidth())
        self.MarkAsDone_checkBox_3.setSizePolicy(sizePolicy)
        self.MarkAsDone_checkBox_3.setObjectName(
            "MarkAsDone_checkBox_3")
        self.gridLayout_14.addWidget(
            self.MarkAsDone_checkBox_3, 1, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(
            "horizontalLayout_8")
        self.ppm_comboBox = QtWidgets.QComboBox(
            self.groupBox_6)
        self.ppm_comboBox.setObjectName("ppm_comboBox")
        self.ppm_comboBox.addItem("")
        self.ppm_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.ppm_comboBox)
        self.ppm_Dep_comboBox = QtWidgets.QComboBox(
            self.groupBox_6)
        self.ppm_Dep_comboBox.setObjectName(
            "ppm_Dep_comboBox")
        self.horizontalLayout_8.addWidget(
            self.ppm_Dep_comboBox)
        self.gridLayout_14.addLayout(self.horizontalLayout_8,
                                     1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        self.gridLayout_71 = QtWidgets.QGridLayout()
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.checkq20 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq20.sizePolicy().hasHeightForWidth())
        self.checkq20.setSizePolicy(sizePolicy)
        self.checkq20.setObjectName("checkq20")
        self.gridLayout_71.addWidget(self.checkq20, 19, 2, 1,
                                     1)
        self.q12 = QtWidgets.QLabel(self.tab_3)
        self.q12.setObjectName("q12")
        self.gridLayout_71.addWidget(self.q12, 3, 0, 1, 1)
        self.q20 = QtWidgets.QLabel(self.tab_3)
        self.q20.setObjectName("q20")
        self.gridLayout_71.addWidget(self.q20, 19, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.tab_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_71.addWidget(self.line_11, 2, 0, 1,
                                     1)
        self.q16 = QtWidgets.QLabel(self.tab_3)
        self.q16.setObjectName("q16")
        self.gridLayout_71.addWidget(self.q16, 11, 0, 1, 1)
        self.q11 = QtWidgets.QLabel(self.tab_3)
        self.q11.setObjectName("q11")
        self.gridLayout_71.addWidget(self.q11, 1, 0, 1, 1)
        self.checkq18 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq18.sizePolicy().hasHeightForWidth())
        self.checkq18.setSizePolicy(sizePolicy)
        self.checkq18.setObjectName("checkq18")
        self.gridLayout_71.addWidget(self.checkq18, 15, 2, 1,
                                     1)
        self.q18 = QtWidgets.QLabel(self.tab_3)
        self.q18.setObjectName("q18")
        self.gridLayout_71.addWidget(self.q18, 15, 0, 1, 1)
        self.checkq17 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq17.sizePolicy().hasHeightForWidth())
        self.checkq17.setSizePolicy(sizePolicy)
        self.checkq17.setObjectName("checkq17")
        self.gridLayout_71.addWidget(self.checkq17, 13, 2, 1,
                                     1)
        self.checkq12 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq12.sizePolicy().hasHeightForWidth())
        self.checkq12.setSizePolicy(sizePolicy)
        self.checkq12.setObjectName("checkq12")
        self.gridLayout_71.addWidget(self.checkq12, 3, 2, 1,
                                     1)
        self.line_21 = QtWidgets.QFrame(self.tab_3)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_71.addWidget(self.line_21, 4, 0, 1,
                                     1)
        self.checkq13 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq13.sizePolicy().hasHeightForWidth())
        self.checkq13.setSizePolicy(sizePolicy)
        self.checkq13.setObjectName("checkq13")
        self.gridLayout_71.addWidget(self.checkq13, 5, 2, 1,
                                     1)
        self.q13 = QtWidgets.QLabel(self.tab_3)
        self.q13.setObjectName("q13")
        self.gridLayout_71.addWidget(self.q13, 5, 0, 1, 1)
        self.checkq19 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq19.sizePolicy().hasHeightForWidth())
        self.checkq19.setSizePolicy(sizePolicy)
        self.checkq19.setObjectName("checkq19")
        self.gridLayout_71.addWidget(self.checkq19, 17, 2, 1,
                                     1)
        self.line_91 = QtWidgets.QFrame(self.tab_3)
        self.line_91.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_91.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_91.setObjectName("line_91")
        self.gridLayout_71.addWidget(self.line_91, 18, 0, 1,
                                     1)
        self.line_31 = QtWidgets.QFrame(self.tab_3)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.gridLayout_71.addWidget(self.line_31, 6, 0, 1,
                                     1)
        self.q19 = QtWidgets.QLabel(self.tab_3)
        self.q19.setObjectName("q19")
        self.gridLayout_71.addWidget(self.q19, 17, 0, 1, 1)
        self.checkq16 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq16.sizePolicy().hasHeightForWidth())
        self.checkq16.setSizePolicy(sizePolicy)
        self.checkq16.setObjectName("checkq16")
        self.gridLayout_71.addWidget(self.checkq16, 11, 2, 1,
                                     1)
        self.q15 = QtWidgets.QLabel(self.tab_3)
        self.q15.setObjectName("q15")
        self.gridLayout_71.addWidget(self.q15, 9, 0, 1, 1)
        self.line_51 = QtWidgets.QFrame(self.tab_3)
        self.line_51.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_51.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_51.setObjectName("line_51")
        self.gridLayout_71.addWidget(self.line_51, 10, 0, 1,
                                     1)
        self.q17 = QtWidgets.QLabel(self.tab_3)
        self.q17.setObjectName("q17")
        self.gridLayout_71.addWidget(self.q17, 13, 0, 1, 1)
        self.checkq14 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq14.sizePolicy().hasHeightForWidth())
        self.checkq14.setSizePolicy(sizePolicy)
        self.checkq14.setObjectName("checkq14")
        self.gridLayout_71.addWidget(self.checkq14, 7, 2, 1,
                                     1)
        self.checkq11 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq11.sizePolicy().hasHeightForWidth())
        self.checkq11.setSizePolicy(sizePolicy)
        self.checkq11.setObjectName("checkq11")
        self.gridLayout_71.addWidget(self.checkq11, 1, 2, 1,
                                     1)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName(
            "horizontalLayout1")
        self.notes2Label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.notes2Label.setFont(font)
        self.notes2Label.setObjectName("notes2Label")
        self.horizontalLayout1.addWidget(self.notes2Label)
        self.ppmNotes_text = QtWidgets.QTextEdit(self.tab_3)
        self.ppmNotes_text.setMaximumSize(
            QtCore.QSize(701, 201))
        self.ppmNotes_text.setObjectName("ppmNotes_text")
        self.horizontalLayout1.addWidget(self.ppmNotes_text)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout1.addWidget(self.label_5)
        self.ppmCost_text = QtWidgets.QTextEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ppmCost_text.sizePolicy().hasHeightForWidth(
            ))
        self.ppmCost_text.setSizePolicy(sizePolicy)
        self.ppmCost_text.setMaximumSize(
            QtCore.QSize(151, 51))
        self.ppmCost_text.setObjectName("ppmCost_text")
        self.horizontalLayout1.addWidget(
            self.ppmCost_text, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem)
        self.gridLayout_71.addLayout(self.horizontalLayout1,
                                     20, 0, 1, 1)
        self.SubmitPPMAnswers_button = QtWidgets.QPushButton(
            self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SubmitPPMAnswers_button.sizePolicy(
            ).hasHeightForWidth())
        self.SubmitPPMAnswers_button.setSizePolicy(
            sizePolicy)
        self.SubmitPPMAnswers_button.setObjectName(
            "SubmitPPMAnswers_button")
        self.gridLayout_71.addWidget(
            self.SubmitPPMAnswers_button, 20, 2, 1, 1)
        self.q14 = QtWidgets.QLabel(self.tab_3)
        self.q14.setObjectName("q14")
        self.gridLayout_71.addWidget(self.q14, 7, 0, 1, 1)
        self.line_71 = QtWidgets.QFrame(self.tab_3)
        self.line_71.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_71.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_71.setObjectName("line_71")
        self.gridLayout_71.addWidget(self.line_71, 14, 0, 1,
                                     1)
        self.line_81 = QtWidgets.QFrame(self.tab_3)
        self.line_81.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_81.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_81.setObjectName("line_81")
        self.gridLayout_71.addWidget(self.line_81, 16, 0, 1,
                                     1)
        self.line_61 = QtWidgets.QFrame(self.tab_3)
        self.line_61.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_61.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_61.setObjectName("line_61")
        self.gridLayout_71.addWidget(self.line_61, 12, 0, 1,
                                     1)
        self.line_41 = QtWidgets.QFrame(self.tab_3)
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.gridLayout_71.addWidget(self.line_41, 8, 0, 1,
                                     1)
        self.checkq15 = QtWidgets.QCheckBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkq15.sizePolicy().hasHeightForWidth())
        self.checkq15.setSizePolicy(sizePolicy)
        self.checkq15.setObjectName("checkq15")
        self.gridLayout_71.addWidget(self.checkq15, 9, 2, 1,
                                     1)
        self.line_12 = QtWidgets.QFrame(self.tab_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_71.addWidget(self.line_12, 0, 0, 1,
                                     3)
        self.verticalLayout_5.addLayout(self.gridLayout_71)
        self.line_111 = QtWidgets.QFrame(self.tab_3)
        self.line_111.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_111.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_111.setObjectName("line_111")
        self.verticalLayout_5.addWidget(self.line_111)
        self.line_42 = QtWidgets.QFrame(self.tab_3)
        self.line_42.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.verticalLayout_5.addWidget(self.line_42)
        self.followUp_tabWidget.addTab(self.tab_3, icon7, "")
        self.gridLayout_2.addWidget(self.followUp_tabWidget,
                                    0, 0, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("Resources/images/follow-up.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon8, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 328, 300))
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(
            self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.information_tabWidget = QtWidgets.QTabWidget(
            self.page_2)
        self.information_tabWidget.setIconSize(
            QtCore.QSize(100, 50))
        self.information_tabWidget.setObjectName(
            "information_tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.tab_6)
        self.verticalLayout_6.setObjectName(
            "verticalLayout_6")
        self.DepartmentSelection_combo = QtWidgets.QComboBox(
            self.tab_6)
        self.DepartmentSelection_combo.setObjectName(
            "DepartmentSelection_combo")
        self.DepartmentSelection_combo.addItem("")
        self.DepartmentSelection_combo.addItem("")
        self.DepartmentSelection_combo.addItem("")
        self.DepartmentSelection_combo.addItem("")
        self.verticalLayout_6.addWidget(
            self.DepartmentSelection_combo)
        self.Devices_table = QtWidgets.QTableWidget(
            self.tab_6)
        self.Devices_table.setAlternatingRowColors(True)
        self.Devices_table.setRowCount(10)
        self.Devices_table.setObjectName("Devices_table")
        self.Devices_table.setColumnCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Devices_table.setItem(0, 12, item)
        self.Devices_table.verticalHeader(
        ).setSortIndicatorShown(True)
        self.verticalLayout_6.addWidget(self.Devices_table)
        self.information_tabWidget.addTab(self.tab_6, icon2,
                                          "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.tab_4)
        self.verticalLayout_2.setObjectName(
            "verticalLayout_2")
        self.Department_table = QtWidgets.QTableWidget(
            self.tab_4)
        self.Department_table.setAlternatingRowColors(False)
        self.Department_table.setRowCount(3)
        self.Department_table.setObjectName(
            "Department_table")
        self.Department_table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setHorizontalHeaderItem(
            0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setHorizontalHeaderItem(
            1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setHorizontalHeaderItem(
            2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Department_table.setItem(2, 2, item)
        self.Department_table.horizontalHeader(
        ).setStretchLastSection(True)
        self.verticalLayout_2.addWidget(
            self.Department_table)
        self.information_tabWidget.addTab(self.tab_4, icon1,
                                          "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.tab_7)
        self.verticalLayout_4.setObjectName(
            "verticalLayout_4")
        self.DepartmentSelection_combo_2 = QtWidgets.QComboBox(
            self.tab_7)
        self.DepartmentSelection_combo_2.setObjectName(
            "DepartmentSelection_combo_2")
        self.DepartmentSelection_combo_2.addItem("")
        self.DepartmentSelection_combo_2.addItem("")
        self.DepartmentSelection_combo_2.addItem("")
        self.DepartmentSelection_combo_2.addItem("")
        self.verticalLayout_4.addWidget(
            self.DepartmentSelection_combo_2)
        self.Forms_table = QtWidgets.QTableWidget(self.tab_7)
        self.Forms_table.setAutoFillBackground(False)
        self.Forms_table.setAlternatingRowColors(True)
        self.Forms_table.setRowCount(10)
        self.Forms_table.setObjectName("Forms_table")
        self.Forms_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Forms_table.setItem(0, 3, item)
        self.Forms_table.horizontalHeader(
        ).setStretchLastSection(True)
        self.Forms_table.verticalHeader(
        ).setSortIndicatorShown(True)
        self.verticalLayout_4.addWidget(self.Forms_table)
        self.information_tabWidget.addTab(self.tab_7, icon3,
                                          "")
        self.gridLayout_3.addWidget(
            self.information_tabWidget, 0, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("Resources/images/request.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon9, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 840, 301))
        self.page_3.setObjectName("page_3")
        self.gridLayout_18 = QtWidgets.QGridLayout(
            self.page_3)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.groupBox_5)
        self.horizontalLayout_3.setObjectName(
            "horizontalLayout_3")
        self.CreateForm_button = QtWidgets.QPushButton(
            self.groupBox_5)
        self.CreateForm_button.setMinimumSize(
            QtCore.QSize(250, 250))
        self.CreateForm_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateForm_button.setMouseTracking(True)
        self.CreateForm_button.setIcon(icon3)
        self.CreateForm_button.setIconSize(
            QtCore.QSize(150, 150))
        self.CreateForm_button.setFlat(True)
        self.CreateForm_button.setObjectName(
            "CreateForm_button")
        self.horizontalLayout_3.addWidget(
            self.CreateForm_button)
        self.gridLayout_18.addWidget(self.groupBox_5, 0, 1,
                                     1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.groupBox_4)
        self.horizontalLayout_2.setObjectName(
            "horizontalLayout_2")
        self.AddDevice_button = QtWidgets.QPushButton(
            self.groupBox_4)
        self.AddDevice_button.setMinimumSize(
            QtCore.QSize(250, 250))
        self.AddDevice_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddDevice_button.setMouseTracking(True)
        self.AddDevice_button.setIcon(icon2)
        self.AddDevice_button.setIconSize(
            QtCore.QSize(150, 150))
        self.AddDevice_button.setFlat(True)
        self.AddDevice_button.setObjectName(
            "AddDevice_button")
        self.horizontalLayout_2.addWidget(
            self.AddDevice_button)
        self.gridLayout_18.addWidget(self.groupBox_4, 0, 0,
                                     1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.groupBox_11)
        self.horizontalLayout_4.setObjectName(
            "horizontalLayout_4")
        self.ManageTasks_button = QtWidgets.QPushButton(
            self.groupBox_11)
        self.ManageTasks_button.setMinimumSize(
            QtCore.QSize(250, 250))
        self.ManageTasks_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ManageTasks_button.setMouseTracking(True)
        self.ManageTasks_button.setIcon(icon4)
        self.ManageTasks_button.setIconSize(
            QtCore.QSize(150, 150))
        self.ManageTasks_button.setFlat(True)
        self.ManageTasks_button.setObjectName(
            "ManageTasks_button")
        self.horizontalLayout_4.addWidget(
            self.ManageTasks_button)
        self.gridLayout_18.addWidget(self.groupBox_11, 0, 2,
                                     1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap("Resources/images/settings.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon10, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea,
                              self.toolBar)
        self.dockWidget_AboutWindow = QtWidgets.QDockWidget(
            MainWindow)
        self.dockWidget_AboutWindow.setMinimumSize(
            QtCore.QSize(500, 400))
        self.dockWidget_AboutWindow.setMaximumSize(
            QtCore.QSize(500, 400))
        self.dockWidget_AboutWindow.setFloating(True)
        self.dockWidget_AboutWindow.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable)
        self.dockWidget_AboutWindow.setAllowedAreas(
            QtCore.Qt.NoDockWidgetArea)
        self.dockWidget_AboutWindow.setObjectName(
            "dockWidget_AboutWindow")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName(
            "dockWidgetContents")
        self.gridLayout_15 = QtWidgets.QGridLayout(
            self.dockWidgetContents)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_10 = QtWidgets.QLabel(
            self.dockWidgetContents)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter
                                   | QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.gridLayout_15.addWidget(self.label_10, 4, 0, 1,
                                     2)
        self.buttonBox = QtWidgets.QDialogButtonBox(
            self.dockWidgetContents)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_15.addWidget(self.buttonBox, 6, 0, 1,
                                     2)
        self.label_6 = QtWidgets.QLabel(
            self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 100))
        self.label_6.setMaximumSize(QtCore.QSize(100, 100))
        self.label_6.setPixmap(
            QtGui.QPixmap("Resources/images/app.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading
                                  | QtCore.Qt.AlignLeft
                                  | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1,
                                     1)
        self.label_8 = QtWidgets.QLabel(
            self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom
                                  | QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_15.addWidget(self.label_8, 3, 0, 1,
                                     2)
        self.label_7 = QtWidgets.QLabel(
            self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading
                                  | QtCore.Qt.AlignLeft
                                  | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_15.addWidget(self.label_7, 0, 1, 1,
                                     1)
        self.label_9 = QtWidgets.QLabel(
            self.dockWidgetContents)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_15.addWidget(self.label_9, 5, 0, 1,
                                     2)
        self.dockWidget_AboutWindow.setWidget(
            self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2),
                                 self.dockWidget_AboutWindow)
        self.dockWidget_AddDeviceWindow = QtWidgets.QDockWidget(
            MainWindow)
        self.dockWidget_AddDeviceWindow.setMinimumSize(
            QtCore.QSize(500, 300))
        self.dockWidget_AddDeviceWindow.setMaximumSize(
            QtCore.QSize(524287, 300))
        self.dockWidget_AddDeviceWindow.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable)
        self.dockWidget_AddDeviceWindow.setAllowedAreas(
            QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget_AddDeviceWindow.setObjectName(
            "dockWidget_AddDeviceWindow")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName(
            "dockWidgetContents_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(
            self.dockWidgetContents_2)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.scrollArea = QtWidgets.QScrollArea(
            self.dockWidgetContents_2)
        self.scrollArea.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 478, 324))
        self.scrollAreaWidgetContents.setObjectName(
            "scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(
            self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole,
            self.label_11)
        self.lineEdit = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit)
        self.label_12 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole,
            self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_2)
        self.label_13 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole,
            self.label_13)
        self.lineEdit_3 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_3)
        self.label_14 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole,
            self.label_14)
        self.lineEdit_4 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_4)
        self.label_15 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole,
            self.label_15)
        self.lineEdit_5 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_5)
        self.label_16 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole,
            self.label_16)
        self.lineEdit_6 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_6)
        self.label_17 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole,
            self.label_17)
        self.label_18 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole,
            self.label_18)
        self.lineEdit_8 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_8)
        self.label_19 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole,
            self.label_19)
        self.lineEdit_9 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_9)
        self.label_20 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole,
            self.label_20)
        self.lineEdit_10 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_10)
        self.label_21 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole,
            self.label_21)
        self.lineEdit_11 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.FieldRole,
            self.lineEdit_12)
        self.label_23 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.LabelRole,
            self.label_23)
        self.installation_dateEdit = QtWidgets.QDateEdit(
            self.scrollAreaWidgetContents)
        self.installation_dateEdit.setWrapping(False)
        self.installation_dateEdit.setAlignment(
            QtCore.Qt.AlignCenter)
        self.installation_dateEdit.setProperty(
            "showGroupSeparator", False)
        self.installation_dateEdit.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2020, 5, 1),
                             QtCore.QTime(0, 0, 0)))
        self.installation_dateEdit.setCalendarPopup(True)
        self.installation_dateEdit.setObjectName(
            "installation_dateEdit")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole,
            self.installation_dateEdit)
        self.scrollArea.setWidget(
            self.scrollAreaWidgetContents)
        self.gridLayout_16.addWidget(self.scrollArea, 0, 0,
                                     1, 2)
        self.pushButton_CancelAddDeviceWindow = QtWidgets.QPushButton(
            self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_CancelAddDeviceWindow.sizePolicy(
            ).hasHeightForWidth())
        self.pushButton_CancelAddDeviceWindow.setSizePolicy(
            sizePolicy)
        self.pushButton_CancelAddDeviceWindow.setObjectName(
            "pushButton_CancelAddDeviceWindow")
        self.gridLayout_16.addWidget(
            self.pushButton_CancelAddDeviceWindow, 1, 0, 1,
            1)
        self.pushButton_AddDeviceWindow = QtWidgets.QPushButton(
            self.dockWidgetContents_2)
        self.pushButton_AddDeviceWindow.setObjectName(
            "pushButton_AddDeviceWindow")
        self.gridLayout_16.addWidget(
            self.pushButton_AddDeviceWindow, 1, 1, 1, 1)
        self.dockWidget_AddDeviceWindow.setWidget(
            self.dockWidgetContents_2)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(8),
            self.dockWidget_AddDeviceWindow)
        self.dockWidget_CreateFormWindow = QtWidgets.QDockWidget(
            MainWindow)
        self.dockWidget_CreateFormWindow.setFloating(False)
        self.dockWidget_CreateFormWindow.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable)
        self.dockWidget_CreateFormWindow.setAllowedAreas(
            QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget_CreateFormWindow.setObjectName(
            "dockWidget_CreateFormWindow")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName(
            "dockWidgetContents_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(
            self.dockWidgetContents_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.pushButton_CreateFormWindow = QtWidgets.QPushButton(
            self.dockWidgetContents_3)
        self.pushButton_CreateFormWindow.setObjectName(
            "pushButton_CreateFormWindow")
        self.gridLayout_17.addWidget(
            self.pushButton_CreateFormWindow, 1, 1, 1, 1)
        self.pushButton_CancelCreateFormWindow = QtWidgets.QPushButton(
            self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_CancelCreateFormWindow.
            sizePolicy().hasHeightForWidth())
        self.pushButton_CancelCreateFormWindow.setSizePolicy(
            sizePolicy)
        self.pushButton_CancelCreateFormWindow.setObjectName(
            "pushButton_CancelCreateFormWindow")
        self.gridLayout_17.addWidget(
            self.pushButton_CancelCreateFormWindow, 1, 0, 1,
            1)
        self.scrollArea_2 = QtWidgets.QScrollArea(
            self.dockWidgetContents_3)
        self.scrollArea_2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 315, 229))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.formLayout_2 = QtWidgets.QFormLayout(
            self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_24 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole,
            self.label_24)
        self.createForm_ans1 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_2)
        self.createForm_ans1.setObjectName("createForm_ans1")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole,
            self.createForm_ans1)
        self.label_27 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole,
            self.label_27)
        self.createForm_ans2 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_2)
        self.createForm_ans2.setObjectName("createForm_ans2")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole,
            self.createForm_ans2)
        self.label_37 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName("label_37")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole,
            self.label_37)
        self.createForm_ans3 = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_2)
        self.createForm_ans3.setObjectName("createForm_ans3")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole,
            self.createForm_ans3)
        self.label_41 = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName("label_41")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole,
            self.label_41)
        self.createForm_ans4 = QtWidgets.QTextEdit(
            self.scrollAreaWidgetContents_2)
        self.createForm_ans4.setObjectName("createForm_ans4")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole,
            self.createForm_ans4)
        self.scrollArea_2.setWidget(
            self.scrollAreaWidgetContents_2)
        self.gridLayout_17.addWidget(self.scrollArea_2, 0, 0,
                                     1, 2)
        self.dockWidget_CreateFormWindow.setWidget(
            self.dockWidgetContents_3)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(8),
            self.dockWidget_CreateFormWindow)
        self.actionCMMS = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap("Resources/images/app.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCMMS.setIcon(icon11)
        self.actionCMMS.setObjectName("actionCMMS")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap("Resources/images/open.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon12)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRequests = QtWidgets.QAction(MainWindow)
        self.actionRequests.setIcon(icon9)
        self.actionRequests.setObjectName("actionRequests")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(
                "Resources/images/cross-gross-symbol.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon13)
        self.actionExit.setObjectName("actionExit")
        self.actionTo_Do = QtWidgets.QAction(MainWindow)
        self.actionTo_Do.setIcon(icon4)
        self.actionTo_Do.setObjectName("actionTo_Do")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setIcon(icon5)
        self.actionHome.setObjectName("actionHome")
        self.actionDaily_Inspection = QtWidgets.QAction(
            MainWindow)
        self.actionDaily_Inspection.setIcon(icon3)
        self.actionDaily_Inspection.setObjectName(
            "actionDaily_Inspection")
        self.actionFollow_Up = QtWidgets.QAction(MainWindow)
        self.actionFollow_Up.setIcon(icon8)
        self.actionFollow_Up.setObjectName("actionFollow_Up")
        self.actionInformation = QtWidgets.QAction(
            MainWindow)
        self.actionInformation.setCheckable(False)
        self.actionInformation.setIcon(icon9)
        self.actionInformation.setObjectName(
            "actionInformation")
        self.actionAdd_Device = QtWidgets.QAction(MainWindow)
        self.actionAdd_Device.setIcon(icon2)
        self.actionAdd_Device.setObjectName(
            "actionAdd_Device")
        self.actionTools = QtWidgets.QAction(MainWindow)
        self.actionTools.setIcon(icon10)
        self.actionTools.setObjectName("actionTools")
        self.actionCreate_Form = QtWidgets.QAction(
            MainWindow)
        self.actionCreate_Form.setIcon(icon3)
        self.actionCreate_Form.setObjectName(
            "actionCreate_Form")
        self.actionManage_Tasks = QtWidgets.QAction(
            MainWindow)
        self.actionManage_Tasks.setIcon(icon4)
        self.actionManage_Tasks.setObjectName(
            "actionManage_Tasks")
        self.actionPPM = QtWidgets.QAction(MainWindow)
        self.actionPPM.setIcon(icon7)
        self.actionPPM.setObjectName("actionPPM")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionCMMS)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(
            self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionFollow_Up)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionTo_Do)
        self.toolBar.addAction(self.actionDaily_Inspection)
        self.toolBar.addAction(self.actionPPM)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInformation)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTools)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Device)
        self.toolBar.addAction(self.actionCreate_Form)
        self.toolBar.addAction(self.actionManage_Tasks)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCMMS)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.label_11.setBuddy(self.lineEdit)
        self.label_12.setBuddy(self.lineEdit)
        self.label_13.setBuddy(self.lineEdit)
        self.label_14.setBuddy(self.lineEdit)
        self.label_15.setBuddy(self.lineEdit)
        self.label_16.setBuddy(self.lineEdit)
        self.label_17.setBuddy(self.lineEdit)
        self.label_18.setBuddy(self.lineEdit)
        self.label_19.setBuddy(self.lineEdit)
        self.label_20.setBuddy(self.lineEdit)
        self.label_21.setBuddy(self.lineEdit)
        self.label_23.setBuddy(self.lineEdit)
        self.label_24.setBuddy(self.lineEdit)
        self.label_27.setBuddy(self.lineEdit)
        self.label_37.setBuddy(self.lineEdit)
        self.label_41.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.followUp_tabWidget.setCurrentIndex(3)
        self.Date_comboBox.setCurrentIndex(2)
        self.Inspection_comboBox.setCurrentIndex(0)
        self.ppm_comboBox.setCurrentIndex(0)
        self.information_tabWidget.setCurrentIndex(0)
        self.buttonBox.clicked['QAbstractButton*'].connect(
            self.dockWidget_AboutWindow.close)
        self.pushButton_CancelAddDeviceWindow.clicked.connect(
            self.dockWidget_AddDeviceWindow.close)
        self.pushButton_CancelCreateFormWindow.clicked.connect(
            self.dockWidget_CreateFormWindow.close)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq11.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq12.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq13.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq14.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq15.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq16.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq17.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq18.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq19.setChecked)
        self.MarkAsDone_checkBox_3.toggled['bool'].connect(
            self.checkq20.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "CMMS"))
        self.label_29.setText(
            _translate("MainWindow", "Tasks:"))
        self.DashTasksCount_label.setText(
            _translate("MainWindow", "2"))
        self.groupBox_3.setTitle(
            _translate("MainWindow", "Search"))
        self.Search_lineEdit.setPlaceholderText(
            _translate(
                "MainWindow",
                "Search for To Do, Tasks, Devices,..etc"))
        self.label_35.setText(
            _translate("MainWindow", "Departments:"))
        self.DashDepatmentsCount_label.setText(
            _translate("MainWindow", "3"))
        self.label_31.setText(
            _translate("MainWindow", "Devices:"))
        self.DashDevicesCount_label.setText(
            _translate("MainWindow", "31"))
        self.label_33.setText(
            _translate("MainWindow", "Forms:"))
        self.DashFormsCount_label.setText(
            _translate("MainWindow", "0"))
        self.label_25.setText(
            _translate("MainWindow", "To Do:"))
        self.DashToDoCount_label.setText(
            _translate("MainWindow", "38"))
        self.followUp_tabWidget.setTabText(
            self.followUp_tabWidget.indexOf(self.tab_2),
            _translate("MainWindow", "Dashboard"))
        self.ToDo_table.setSortingEnabled(True)
        item = self.ToDo_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Task"))
        item = self.ToDo_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.ToDo_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.ToDo_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Comment"))
        __sortingEnabled = self.ToDo_table.isSortingEnabled()
        self.ToDo_table.setSortingEnabled(False)
        item = self.ToDo_table.item(0, 0)
        item.setText(_translate("MainWindow", "Task X"))
        item = self.ToDo_table.item(0, 1)
        item.setText(_translate("MainWindow", "13/5/2020"))
        item = self.ToDo_table.item(0, 2)
        item.setText(_translate("MainWindow", "In-Progress"))
        item = self.ToDo_table.item(0, 3)
        item.setText(
            _translate(
                "MainWindow",
                "This is test item for evaluation purpose only!"
            ))
        item = self.ToDo_table.item(1, 0)
        item.setText(_translate("MainWindow", "Task Y"))
        item = self.ToDo_table.item(1, 1)
        item.setText(_translate("MainWindow", "13/5/2020"))
        item = self.ToDo_table.item(1, 2)
        item.setText(_translate("MainWindow", "Done"))
        item = self.ToDo_table.item(1, 3)
        item.setText(
            _translate(
                "MainWindow",
                "This is test item for evaluation purpose only!"
            ))
        item = self.ToDo_table.item(2, 0)
        item.setText(_translate("MainWindow", "Review"))
        item = self.ToDo_table.item(2, 1)
        item.setText(_translate("MainWindow", "13/5/2020"))
        item = self.ToDo_table.item(2, 2)
        item.setText(_translate("MainWindow", "On-Hold"))
        item = self.ToDo_table.item(2, 3)
        item.setText(
            _translate(
                "MainWindow",
                "This is test item for evaluation purpose only!"
            ))
        self.ToDo_table.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(
            _translate("MainWindow", "View:"))
        self.Export_button.setText(
            _translate("MainWindow", "Export..."))
        self.Date_comboBox.setItemText(
            0, _translate("MainWindow", "7 Days"))
        self.Date_comboBox.setItemText(
            1, _translate("MainWindow", "3 Days"))
        self.Date_comboBox.setItemText(
            2, _translate("MainWindow", "Today"))
        self.Print_button.setText(
            _translate("MainWindow", "Print..."))
        self.followUp_tabWidget.setTabText(
            self.followUp_tabWidget.indexOf(self.tab),
            _translate("MainWindow", "To Do"))
        self.groupBox_2.setTitle(
            _translate("MainWindow", "Task:"))
        self.CheckAll_checkBox.setText(
            _translate("MainWindow", "Check all"))
        self.Inspection_comboBox.setItemText(
            0, _translate("MainWindow", "Task X"))
        self.Inspection_comboBox.setItemText(
            1, _translate("MainWindow", "Task Y"))
        self.q8.setText(_translate("MainWindow", "HHHH"))
        self.q10.setText(_translate("MainWindow", "HhHh"))
        self.q5.setText(
            _translate("MainWindow", "Clean Windows"))
        self.checkq7.setText(_translate("MainWindow",
                                        "Done"))
        self.checkq10.setText(
            _translate("MainWindow", "Done"))
        self.q7.setText(_translate("MainWindow", "qestion "))
        self.checkq2.setText(_translate("MainWindow",
                                        "Done"))
        self.q1.setText(
            _translate("MainWindow", "Fix Lights"))
        self.q2.setText(_translate("MainWindow", "Fix Beds"))
        self.checkq9.setText(_translate("MainWindow",
                                        "Done"))
        self.checkq8.setText(_translate("MainWindow",
                                        "Done"))
        self.checkq1.setText(_translate("MainWindow",
                                        "Done"))
        self.q3.setText(_translate("MainWindow", "Fix MRI"))
        self.q6.setText(
            _translate("MainWindow", "Install Word 2007"))
        self.checkq3.setText(_translate("MainWindow",
                                        "Done"))
        self.SubmitInspectionAnswers_button.setText(
            _translate("MainWindow", "Submit"))
        self.checkq4.setText(_translate("MainWindow",
                                        "Done"))
        self.q9.setText(_translate("MainWindow", "hhhh"))
        self.q4.setText(_translate("MainWindow",
                                   "Fix X-Ray"))
        self.checkq5.setText(_translate("MainWindow",
                                        "Done"))
        self.checkq6.setText(_translate("MainWindow",
                                        "Done"))
        self.deleteInspection_button.setText(
            _translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "Notes"))
        self.insp_notes.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.85455pt;\"><br /></p></body></html>"
            ))
        self.followUp_tabWidget.setTabText(
            self.followUp_tabWidget.indexOf(self.tab_8),
            _translate("MainWindow", "Inspection"))
        self.groupBox_6.setTitle(
            _translate("MainWindow", "Task:"))
        self.MarkAsDone_checkBox_3.setText(
            _translate("MainWindow", "Check all"))
        self.ppm_comboBox.setItemText(
            0, _translate("MainWindow", "Task X"))
        self.ppm_comboBox.setItemText(
            1, _translate("MainWindow", "Task Y"))
        self.checkq20.setText(
            _translate("MainWindow", "Done"))
        self.q12.setText(_translate("MainWindow",
                                    "Fix Beds"))
        self.q20.setText(_translate("MainWindow", "HhHh"))
        self.q16.setText(
            _translate("MainWindow", "Install Word 2007"))
        self.q11.setText(
            _translate("MainWindow", "Fix Lights"))
        self.checkq18.setText(
            _translate("MainWindow", "Done"))
        self.q18.setText(_translate("MainWindow", "HHHH"))
        self.checkq17.setText(
            _translate("MainWindow", "Done"))
        self.checkq12.setText(
            _translate("MainWindow", "Done"))
        self.checkq13.setText(
            _translate("MainWindow", "Done"))
        self.q13.setText(_translate("MainWindow", "Fix MRI"))
        self.checkq19.setText(
            _translate("MainWindow", "Done"))
        self.q19.setText(_translate("MainWindow", "hhhh"))
        self.checkq16.setText(
            _translate("MainWindow", "Done"))
        self.q15.setText(
            _translate("MainWindow", "Clean Windows"))
        self.q17.setText(_translate("MainWindow",
                                    "Question"))
        self.checkq14.setText(
            _translate("MainWindow", "Done"))
        self.checkq11.setText(
            _translate("MainWindow", "Done"))
        self.notes2Label.setText(
            _translate("MainWindow", "Notes:"))
        self.ppmNotes_text.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.85455pt;\"><br /></p></body></html>"
            ))
        self.label_5.setText(
            _translate("MainWindow", "Cost:"))
        self.ppmCost_text.setHtml(
            _translate(
                "MainWindow",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.85455pt;\"><br /></p></body></html>"
            ))
        self.SubmitPPMAnswers_button.setText(
            _translate("MainWindow", "Submit"))
        self.q14.setText(
            _translate("MainWindow", "Fix X-Ray"))
        self.checkq15.setText(
            _translate("MainWindow", "Done"))
        self.followUp_tabWidget.setTabText(
            self.followUp_tabWidget.indexOf(self.tab_3),
            _translate("MainWindow", "PPM"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page),
            _translate("MainWindow", "Follow-Up"))
        self.DepartmentSelection_combo.setItemText(
            0, _translate("MainWindow", "All Departments"))
        self.DepartmentSelection_combo.setItemText(
            1, _translate("MainWindow", "Operating Room"))
        self.DepartmentSelection_combo.setItemText(
            2, _translate("MainWindow", "ICU"))
        self.DepartmentSelection_combo.setItemText(
            3, _translate("MainWindow", "Radiology"))
        self.Devices_table.setSortingEnabled(True)
        item = self.Devices_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Devices_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Device"))
        item = self.Devices_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.Devices_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Model"))
        item = self.Devices_table.horizontalHeaderItem(4)
        item.setText(
            _translate("MainWindow", "Serial Number"))
        item = self.Devices_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow",
                                "Manufacturer"))
        item = self.Devices_table.horizontalHeaderItem(6)
        item.setText(
            _translate("MainWindow", "Installation Date"))
        item = self.Devices_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "PPM Period"))
        item = self.Devices_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Family"))
        item = self.Devices_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.Devices_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Warranty"))
        item = self.Devices_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "PPM ID"))
        item = self.Devices_table.horizontalHeaderItem(12)
        item.setText(
            _translate("MainWindow", "Department ID"))
        __sortingEnabled = self.Devices_table.isSortingEnabled(
        )
        self.Devices_table.setSortingEnabled(False)
        item = self.Devices_table.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.Devices_table.item(0, 1)
        item.setText(_translate("MainWindow", "MRI"))
        item = self.Devices_table.item(0, 2)
        item.setText(_translate("MainWindow", "TEST"))
        item = self.Devices_table.item(0, 3)
        item.setText(_translate("MainWindow", "TEST"))
        item = self.Devices_table.item(0, 4)
        item.setText(_translate("MainWindow", "32RGS432FSA"))
        item = self.Devices_table.item(0, 5)
        item.setText(_translate("MainWindow", "TEST"))
        item = self.Devices_table.item(0, 6)
        item.setText(_translate("MainWindow", "13/5/2020"))
        item = self.Devices_table.item(0, 7)
        item.setText(_translate("MainWindow", "001"))
        item = self.Devices_table.item(0, 8)
        item.setText(_translate("MainWindow", "TEST"))
        item = self.Devices_table.item(0, 9)
        item.setText(_translate("MainWindow", "TEST"))
        item = self.Devices_table.item(0, 10)
        item.setText(_translate("MainWindow", "1 Year"))
        item = self.Devices_table.item(0, 12)
        item.setText(_translate("MainWindow", "002"))
        self.Devices_table.setSortingEnabled(
            __sortingEnabled)
        self.information_tabWidget.setTabText(
            self.information_tabWidget.indexOf(self.tab_6),
            _translate("MainWindow", "Devices"))
        item = self.Department_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Department_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Department"))
        item = self.Department_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location"))
        __sortingEnabled = self.Department_table.isSortingEnabled(
        )
        self.Department_table.setSortingEnabled(False)
        item = self.Department_table.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.Department_table.item(0, 1)
        item.setText(
            _translate("MainWindow", "Operating Room"))
        item = self.Department_table.item(0, 2)
        item.setText(_translate("MainWindow", "Basement"))
        item = self.Department_table.item(1, 0)
        item.setText(_translate("MainWindow", "002"))
        item = self.Department_table.item(1, 1)
        item.setText(_translate("MainWindow", "Radiology"))
        item = self.Department_table.item(1, 2)
        item.setText(_translate("MainWindow", "Basement"))
        item = self.Department_table.item(2, 0)
        item.setText(_translate("MainWindow", "003"))
        item = self.Department_table.item(2, 1)
        item.setText(
            _translate("MainWindow",
                       "Intensive Care Unit (ICU)"))
        item = self.Department_table.item(2, 2)
        item.setText(_translate("MainWindow", "Basement"))
        self.Department_table.setSortingEnabled(
            __sortingEnabled)
        self.information_tabWidget.setTabText(
            self.information_tabWidget.indexOf(self.tab_4),
            _translate("MainWindow", "Departments"))
        self.DepartmentSelection_combo_2.setItemText(
            0, _translate("MainWindow", "All Departments"))
        self.DepartmentSelection_combo_2.setItemText(
            1, _translate("MainWindow", "Operating Room"))
        self.DepartmentSelection_combo_2.setItemText(
            2, _translate("MainWindow", "ICU"))
        self.DepartmentSelection_combo_2.setItemText(
            3, _translate("MainWindow", "Radiology"))
        item = self.Forms_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Forms_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.Forms_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Family"))
        item = self.Forms_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Text"))
        __sortingEnabled = self.Forms_table.isSortingEnabled(
        )
        self.Forms_table.setSortingEnabled(False)
        item = self.Forms_table.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.Forms_table.item(0, 1)
        item.setText(_translate("MainWindow", "Question"))
        item = self.Forms_table.item(0, 2)
        item.setText(_translate("MainWindow", "MRI"))
        item = self.Forms_table.item(0, 3)
        item.setText(
            _translate(
                "MainWindow",
                "Q1$Q2$Q3$$FDFASFAASFASFAFASFAGF$$DAFAFFAFASGASGSAGA"
            ))
        self.Forms_table.setSortingEnabled(__sortingEnabled)
        self.information_tabWidget.setTabText(
            self.information_tabWidget.indexOf(self.tab_7),
            _translate("MainWindow", "Forms"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page_2),
            _translate("MainWindow", "Information"))
        self.groupBox_5.setTitle(
            _translate("MainWindow", "Create Form"))
        self.groupBox_4.setTitle(
            _translate("MainWindow", "Add Device"))
        self.groupBox_11.setTitle(
            _translate("MainWindow", "Manage Tasks"))
        self.toolBox.setItemText(
            self.toolBox.indexOf(self.page_3),
            _translate("MainWindow", "Tools"))
        self.menuFile.setTitle(
            _translate("MainWindow", "File"))
        self.menuEdit.setTitle(
            _translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(
            _translate("MainWindow", "Settings"))
        self.menuWindow.setTitle(
            _translate("MainWindow", "Window"))
        self.menuHelp.setTitle(
            _translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(
            _translate("MainWindow", "toolBar"))
        self.dockWidget_AboutWindow.setWindowTitle(
            _translate("MainWindow", "About CMMS"))
        self.label_10.setText(
            _translate(
                "MainWindow", "Abdulla A. Zahran\n"
                "Ahmad A. Muhammad\n"
                "Eslam Khaled (Es Kh)\n"
                "Reham Abd El-fattah\n"
                "Renad Taher"))
        self.label_8.setText(
            _translate("MainWindow",
                       "Developed By: A.A.E.R.R. Team"))
        self.label_7.setText(_translate("MainWindow",
                                        "CMMS"))
        self.label_9.setText(
            _translate(
                "MainWindow", "Version: 1.0.0\n"
                "© 2020 - Systems & Biomedical Engineering - Cairo University\n"
                "Clinical Engineering Course by: PROF. BASSEL TAWFIK\n"
                "All Rights Reserved"))
        self.dockWidget_AddDeviceWindow.setWindowTitle(
            _translate("MainWindow", "Add New Device"))
        self.label_11.setText(_translate("MainWindow", "ID"))
        self.label_12.setText(
            _translate("MainWindow", "Device"))
        self.label_13.setText(
            _translate("MainWindow", "Type"))
        self.label_14.setText(
            _translate("MainWindow", "Model"))
        self.label_15.setText(
            _translate("MainWindow", "Serial No."))
        self.label_16.setText(
            _translate("MainWindow", "Manufacturer"))
        self.label_17.setText(
            _translate("MainWindow", "Installation Date"))
        self.label_18.setText(
            _translate("MainWindow", "PPM Period"))
        self.label_19.setText(
            _translate("MainWindow", "Family"))
        self.label_20.setText(
            _translate("MainWindow", "Vendor"))
        self.label_21.setText(
            _translate("MainWindow", "Warranty"))
        self.label_23.setText(
            _translate("MainWindow", "Department ID"))
        self.pushButton_CancelAddDeviceWindow.setText(
            _translate("MainWindow", "Cancel"))
        self.pushButton_AddDeviceWindow.setText(
            _translate("MainWindow", "Add"))
        self.dockWidget_CreateFormWindow.setWindowTitle(
            _translate("MainWindow", "Create Form"))
        self.pushButton_CreateFormWindow.setText(
            _translate("MainWindow", "Add"))
        self.pushButton_CancelCreateFormWindow.setText(
            _translate("MainWindow", "Cancel"))
        self.label_24.setText(_translate("MainWindow", "ID"))
        self.label_27.setText(
            _translate("MainWindow", "Type"))
        self.label_37.setText(
            _translate("MainWindow", "Family"))
        self.label_41.setText(
            _translate(
                "MainWindow", "Text\n"
                " \'Separte questions with ?\'"))
        self.actionCMMS.setText(
            _translate("MainWindow", "About CMMS"))
        self.actionCMMS.setShortcut(
            _translate("MainWindow", "?"))
        self.actionOpen.setText(
            _translate("MainWindow", "Exit"))
        self.actionOpen.setShortcut(
            _translate("MainWindow", "Ctrl+O"))
        self.actionRequests.setText(
            _translate("MainWindow", "Requests"))
        self.actionExit.setText(
            _translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(
            _translate("MainWindow", "Ctrl+W"))
        self.actionTo_Do.setText(
            _translate("MainWindow", "To Do"))
        self.actionHome.setText(
            _translate("MainWindow", "Home"))
        self.actionDaily_Inspection.setText(
            _translate("MainWindow", "Inspection"))
        self.actionFollow_Up.setText(
            _translate("MainWindow", "Follow-Up"))
        self.actionInformation.setText(
            _translate("MainWindow", "Information"))
        self.actionAdd_Device.setText(
            _translate("MainWindow", "Add Device"))
        self.actionTools.setText(
            _translate("MainWindow", "Tools"))
        self.actionCreate_Form.setText(
            _translate("MainWindow", "Create Form"))
        self.actionManage_Tasks.setText(
            _translate("MainWindow", "Manage Tasks"))
        self.actionPPM.setText(
            _translate("MainWindow", "PPM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
