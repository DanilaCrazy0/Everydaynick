# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_task_edit(object):
    def setupUi(self, Form_task_edit):
        Form_task_edit.setObjectName("Form_task_edit")
        Form_task_edit.resize(483, 248)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form_task_edit)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form_task_edit)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_task = QtWidgets.QLabel(self.groupBox)
        self.label_task.setObjectName("label_task")
        self.verticalLayout.addWidget(self.label_task)
        self.label_time = QtWidgets.QLabel(self.groupBox)
        self.label_time.setObjectName("label_time")
        self.verticalLayout.addWidget(self.label_time)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_task = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.verticalLayout_2.addWidget(self.lineEdit_task)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_2.addWidget(self.dateTimeEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form_task_edit)
        QtCore.QMetaObject.connectSlotsByName(Form_task_edit)

    def retranslateUi(self, Form_task_edit):
        _translate = QtCore.QCoreApplication.translate
        Form_task_edit.setWindowTitle(_translate("Form_task_edit", "Изменить задачу"))
        self.groupBox.setTitle(_translate("Form_task_edit", "GroupBox"))
        self.label_task.setText(_translate("Form_task_edit", "Описание задачи"))
        self.label_time.setText(_translate("Form_task_edit", "Время"))
        self.pushButton_cancel.setText(_translate("Form_task_edit", "Отмена"))
        self.pushButton_ok.setText(_translate("Form_task_edit", "Ок"))
