import os,time,sys
from PyQt5 import QtCore,QtWidgets,QtGui
class test(QtWidgets.QWidget):
    def setUI(self):
        self.setGeometry(400,400,400,200)
        self.setWindowTitle("test")
        self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = test()
    ui.setUI()
    sys.exit(app.exec_())