from View.FrmLogin import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = FrmLogin()
    widget.show()
    sys.exit(app.exec())