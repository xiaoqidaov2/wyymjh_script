import sys
from PyQt5.QtWidgets import QApplication
from gui import Example

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
