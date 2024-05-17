from PyQt5.QtWidgets import *
from PyQt5 import uic

class MonInterface(QMainWindow):

    def __init__(self):
        super(MonInterface, self).__init__()
        uic.loadUi("des.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.connexion)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_2.clicked.connect(self.addition)
        self.pushButton_3.clicked.connect(self.soustraction)
    
    def connexion(self):
        if self.lineEdit.text() == "mouad" and self.lineEdit_2.text() == "kazangui":
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True) 
            self.pushButton_5.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("ID que vous avez saisie n'est pas associée à un compte.")
            message.exec_()
        
    def addition(self):
        message2 = QMessageBox()
        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        y = int(a) + int(b)
        message2.setText(str(y))
        message2.exec_()
            
    def soustraction(self):
        message2 = QMessageBox()
        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        y = int(a) - int(b)
        message2.setText(str(y))
        message2.exec_()
    
def main():
    mon_app = QApplication([])
    fenetre = MonInterface()  # Ajout d'un signe égal ici
    mon_app.exec_()
    
if __name__ == '__main__':        
    main()
