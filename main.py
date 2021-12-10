import sys
import pickle
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from list_zadach import Ui_MainWindow
from task_create import Ui_Form_task_create
from task_edit import Ui_Form_task_edit


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            with open('data.txt', 'rb') as f:
                self.data = pickle.load(f)
        except EOFError:
                self.data = []
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.pushButton_create.clicked.connect(self.click_create)
        self.pushButton_delete.clicked.connect(self.click_delete)
        self.pushButton_edit.clicked.connect(self.click_edit)


    def calendar_clicked(self, date):
        self.date = date.toPyDate()
        date_list_task = list(map(lambda x: f'{x[0]}: {x[1]}', filter(lambda t: t[0] == self.date, self.data)))
        print(date_list_task)
        self.listWidget.clear()
        self.listWidget.addItems(date_list_task)
        self.dateEdit.setDate(self.date)

    def click_create(self):
        self.wnd_create = CreateTaskWindow(self.data, self.date)
        self.wnd_create.show()

    def click_delete(self):
        elem = self.listWidget.currentItem().text()[12:]
        self.data.remove((self.date, elem))
        row = self.listWidget.row(self.listWidget.currentItem())
        self.listWidget.takeItem(row)
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)

    def click_edit(self):
        if self.listWidget.currentItem():
            self.wnd_edit = EditTaskWindow(self.data, self.date,
                                       self.listWidget.currentItem())
            self.wnd_edit.show()


class CreateTaskWindow(QWidget, Ui_Form_task_create):
    def __init__(self, list_tasks, date):
        super().__init__()
        self.setupUi(self)
        self.pushButton_create.clicked.connect(self.ok)
        self.data = list_tasks
        self.date = date
        self.dateTimeEdit.setDate(self.date)
        self.pushButton_cancel.clicked.connect(lambda: self.hide())

    def ok(self):
        description = self.lineEdit_task.text()
        datetime = self.dateTimeEdit.date().toPyDate()
        self.data.append((datetime, description))
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)
        self.hide()


class EditTaskWindow(QWidget, Ui_Form_task_edit):
    def __init__(self, list_tasks, date, elem):
        super().__init__()
        self.setupUi(self)
        self.data = list_tasks
        self.date = date
        self.elem = elem
        self.dateTimeEdit.setDate(self.date)
        self.pushButton_cancel.clicked.connect(lambda: self.hide())
        self.pushButton_ok.clicked.connect(self.click_ok)

    def click_ok(self):
        text = self.lineEdit_task.text()
        print(self.data)
        a = self.data.index((self.date, self.elem.text()[12:]))
        self.data[a] = list(self.data[a])
        self.data[a][1] = text
        self.data[a] = tuple(self.data[a])
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)
        self.hide()


def except_hook(clc, exception, traceback):
    sys.__excepthook__(clc, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())

