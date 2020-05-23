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

        self.question =[self.q1 ,self.q2,self.q3,self.q4,self.q5,self.q6,self.q7,self.q8,self.q9,self.q10 ] 
        self.checks = [self.checkq1, self.checkq2, self.checkq3, self.checkq4 , self.checkq5, self.checkq6 , self.checkq7, self.checkq8, self.checkq9, self.checkq10]
        self.UpdateTables()
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
        self.actionFollow_Up.triggere seld.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionHome.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionTo_Do.triggered.connect(lambda:f.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionDaily_Inspection.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionInformation.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionTools.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionAdd_Device.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionCreate_Form.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionManage_Tasks.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        self.actionCMMS.triggered.connect(lambda: self.InsertAtIndex(self.Devices_table, 1, 0, 'Test'))
        '''
        ''' Combos
        self.DepartmentSelection_combo
        self.DepartmentSelection_combo_2
        self.DepartmentSelection_combo_3
        self.Date_comboBox
        self.Inspection_comboBox
        '''

        self.Inspection_comboBox.clear()


        ## gives an error when we choose all departmenst after changing the department from the combo
        ## because there is no department with id ==0
        self.DepartmentSelection_combo.currentIndexChanged.connect(
            lambda: self.UpdateTable(
                DB.SelectRows(
                    'device', 'depid = %s' % self.DepartmentSelection_combo.
                    currentIndex()), self.Devices_table)) 
        self.DepartmentSelection_combo_3.currentIndexChanged.connect(
            lambda: self.UpdateTable(
                DB.GetDF(self.DepartmentSelection_combo_3.currentIndex()), self.Forms_table))
        dailyDevices_names = DB.RunCommand("SELECT DevName FROM device")
        dailyDevices_names = [str(device[0])  for device in dailyDevices_names ]
        self.Inspection_comboBox.addItems(dailyDevices_names)

        family = DB.SelectRows("device","DevName='{}'".format(self.Inspection_comboBox.currentText()) )[0][8]
        # print(family)
        form = DB.SelectRows("form","formfamily='{}' AND formtype= 'daily inspection' ".format(str(family)) )
        form = form[0][3].split("?")[1:]
        form = [str(question)+str('  ?')  for question in form ]
        for i ,quest in enumerate(form):
            self.question[i].setText(quest)
        self.Inspection_comboBox.currentIndexChanged.connect(self.update_form)


        
    def UpdateTables(self):
        self.UpdateTable(DB.GetRows('department'), self.Department_table)
        self.UpdateTable(DB.GetRows('device'), self.Devices_table)
        self.UpdateTable(DB.GetRows('form'), self.Forms_table)
        self.update_form()

        
        
    def UpdateTable(self, rows, UItable):
        if str(type(rows)) != "<class 'NoneType'>" and len(rows[0])>0 :
            UItable.setRowCount(len(rows))
           
            UItable.setColumnCount(len(rows[0]))

            for row_number, row_data in enumerate(rows):
                for column_number, column_data in enumerate(row_data):
                    self.InsertAtIndex(UItable, row_number, column_number,
                                       str(column_data))
        else:
            UItable.clearContents()
    def update_form(self):
        family = DB.SelectRows("device","DevName='{}'".format(self.Inspection_comboBox.currentText()) )
        if len(family)>0 :
            form = DB.SelectRows("form","formfamily='{}' AND formtype= 'daily inspection' ".format(str(family[0][8])) )
            if len(form)>0:
                form = form[0][3].split("?")
                form = [str(question)+str('  ?')  for question in form ]
                for i ,quest in enumerate(form):
                    if quest !="  ?" :
                        self.question[i].setText(quest)
                self.clear_form(10-len(form))
        else :
            self.clear_form(10)

    def clear_form(self,amount) :
        for i in range(amount) :
            self.question[len(self.question)-i-1].clear()
            self.checks[len(self.checks)-i-1].hide()

    # def enable_form(self):
    #     for i in range(10) :
    #         self.question[i].setDisabled(False)


    def InsertAtIndex(self, table, y, x, Item):
        table.setItem(y, x, QTableWidgetItem(Item))


    

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
