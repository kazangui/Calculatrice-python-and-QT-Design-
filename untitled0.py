from PyQt5.QtWidgets import *
from PyQt5 import uic


class MonInterface (QMainWindow):
    
    def __init__(self):
        super(MonInterface,self).__init__()
        uic.loadUi("des.ui",self)
        self.show()
        
def main():
        mon_app=QApplication([])
        fenetre=MonInterface()
        mon_app.exec_()
        
if __name__=='__main__':
    main()

        
    
        
