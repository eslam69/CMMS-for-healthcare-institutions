import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from DB_Management import DatabaseUtilities as DU
import hospital_gui

DB = DU()


class ApplicationWindow(hospital_gui.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(ApplicationWindow, self).setupUi(mainWindow)
        ''' Buttons
        self.AddDevice_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.SubmitAnswers_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.CreateForm_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.ManageTasks_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.Export_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.Print_button.clicked.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        '''
        ''' Tables
        self.Forms_table
        self.Department_table
        self.Devices_table
        self.ToDo_table
        '''
        ''' LineEdit
        self.Search_lineEdit
        '''
        ''' Actions (Ordered by the actual toolbar order)
        self.actionFollow_Up.triggered.connect()
        self.actionHome.triggered.connect()
        self.actionTo_Do.triggered.connect()
        self.actionDaily_Inspection.triggered.connect()
        self.actionInformation.triggered.connect()
        self.actionTools.triggered.connect()
        self.actionAdd_Device.triggered.connect()
        self.actionCreate_Form.triggered.connect()
        self.actionManage_Tasks.triggered.connect()
        self.actionCMMS.triggered.connect()
        '''
        ''' Combos
        self.DepartmentSelection_combo
        self.DepartmentSelection_combo_2
        self.Date_comboBox
        self.Inspection_comboBox
        '''
        self.question = [
            self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7,
            self.q8, self.q9, self.q10
        ]

        self.InitCheckBoxes()
        self.InitActions()
        self.UpdateDevCombo()
        self.UpdateTables()
        self.InitComboBoxes()

    def InitCheckBoxes(self):
        self.checks = [
            self.checkq1, self.checkq2, self.checkq3, self.checkq4,
            self.checkq5, self.checkq6, self.checkq7, self.checkq8,
            self.checkq9, self.checkq10
        ]

        self.CheckAll_checkBox.stateChanged.connect(self.CheckAll)

        for i in range(10):
            self.checks[i].stateChanged.connect(self.FormIsFilling)

    def InitActions(self):
        self.actionFollow_Up.triggered.connect(
            lambda: self.toolBox.setCurrentIndex(0))
        self.actionHome.triggered.connect(lambda: self.NavTo(0))
        self.actionTo_Do.triggered.connect(lambda: self.NavTo(1))
        self.actionDaily_Inspection.triggered.connect(lambda: self.NavTo(2))
        self.actionInformation.triggered.connect(
            lambda: self.toolBox.setCurrentIndex(1))
        self.actionTools.triggered.connect(
            lambda: self.toolBox.setCurrentIndex(2))

    def InitComboBoxes(self):
        ## gives an error when we choose all departmenst after changing the department from the combo
        ## because there is no department with id ==0
        self.DepartmentSelection_combo.currentIndexChanged.connect(
            lambda: self.UpdateTable(
                DB.SelectRows(
                    'device', 'depid = %s' % self.DepartmentSelection_combo.
                    currentIndex()), self.Devices_table))
        self.DepartmentSelection_combo_2.currentIndexChanged.connect(
            lambda: self.UpdateTable(
                DB.GetDF(self.DepartmentSelection_combo_2.currentIndex()), self
                .Forms_table))

        self.Inspection_comboBox.currentIndexChanged.connect(self.UpdateForm)

    def UpdateDevCombo(self):
        self.Inspection_comboBox.clear()

        dailyDevices_names = DB.RunCommand("SELECT DevName FROM device")
        dailyDevices_names = [str(device[0]) for device in dailyDevices_names]

        self.Inspection_comboBox.addItems(dailyDevices_names)

    def UpdateTables(self):
        self.UpdateTable(DB.GetRows('department'), self.Department_table)
        self.UpdateTable(DB.GetRows('device'), self.Devices_table)
        self.UpdateTable(DB.GetRows('form'), self.Forms_table)
        self.UpdateForm()

    def UpdateTable(self, rows, UItable):
        if str(type(rows)) != "<class 'NoneType'>" and len(rows[0]) > 0:
            UItable.setRowCount(len(rows))

            UItable.setColumnCount(len(rows[0]))

            for row_number, row_data in enumerate(rows):
                for column_number, column_data in enumerate(row_data):
                    self.InsertAtIndex(UItable, row_number, column_number,
                                       str(column_data))
        else:
            UItable.clearContents()

    def UpdateForm(self):
        family = DB.SelectRows(
            "device",
            "DevName='{}'".format(self.Inspection_comboBox.currentText()))
        if len(family) > 0:
            form = DB.SelectRows(
                "form",
                "formfamily='{}' AND formtype= 'daily inspection' ".format(
                    str(family[0][8])))
            if len(form) > 0:
                form = form[0][3].split("?")
                form = [str(question) + str('  ?') for question in form]
                EnableVar = len(form)
                for i, quest in enumerate(form):
                    if quest != "  ?":
                        self.question[i - 1].setText(quest)
                    else:
                        EnableVar -= 1
                self.clear_form(len(self.checks), 10 - EnableVar)
                self.enable_form(EnableVar)
            else:
                self.clear_form(10, 10)
                self.question[0].setText('No Form To Display For This Device')
        else:
            self.clear_form(10, 10)
            self.question[0].setText('No Form To Display For This Device')

    # def update_form2(self):
    #     self.clear_form(10, 10)
    #     family = DB.SelectRows(
    #         "device",
    #         "DevName='{}'".format(self.ppm_comboBox.currentText())) #####edit
    #     if len(family) > 0:
    #         form = DB.SelectRows(
    #             "form",
    #             "formfamily='{}' AND formtype= 'PPM' ".format(
    #                 str(family[0][8])))
    #         if len(form) > 0:
    #             form = form[0][3].split("?")
    #             form = [str(question) + str('  ?') for question in form]
    #             print(form)
    #             for i, quest in enumerate(form):
    #                 if quest != "  ?":
    #                     print(quest)
    #                     self.question2[i - 1].setText(quest) ######### edit
    #             self.clear_form(len(self.checks), 10 - len(form)) ############generalize these functions ---> enable_form(self,checklist, amount) , clear_Form(self, questionList,checklist,lenlist, amount)
    #             self.enable_form(len(form) - 1)
    #     else:
    #         print('Clearing All Form')
    #         self.clear_form(10, 10)


    def InsertAtIndex(self, table, y, x, Item):
        table.setItem(y, x, QTableWidgetItem(Item))

    def clear_form(self, lenlist, amount):
        for i in range(amount):
            self.question[lenlist - i - 1].clear()
            self.checks[lenlist - i - 1].hide()
            self.checks[lenlist - i - 1].setDisabled(True)

    def enable_form(self, amount):
        for i in range(amount):
            self.checks[i].setDisabled(False)
            self.checks[i].show()

    def NavTo(self, i):
        self.toolBox.setCurrentIndex(0)
        self.followUp_tabWidget.setCurrentIndex(i)

    def CheckAll(self):
        for i in range(10):
            if self.CheckAll_checkBox.isChecked():
                self.checks[i].setChecked(True)
                self.FormIsFilling()
            else:
                self.checks[i].setChecked(False)
                self.FormIsFilling()

    def FormIsFilling(self):
        self.CheckStates = [
            False, False, False, False, False, False, False, False, False,
            False, False
        ]
        self.CheckStates[10] = self.CheckAll_checkBox.isChecked()
        for i in range(10):
            self.CheckStates[i] = self.checks[i].isChecked()

        if any(self.CheckStates):
            self.Inspection_comboBox.setDisabled(True)
        else:
            self.Inspection_comboBox.setDisabled(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
