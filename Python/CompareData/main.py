import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui import Comparator


def exception_hook(exctype, value, traceback):
    QMessageBox.critical(None,
                         "Error",
                         f"Type: {exctype.__name__}"
                         f"\n\nInfo: \n{str(value)}",
                         QMessageBox.Ok)

    sys.__excepthook__(exctype, value, traceback)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    comparator = Comparator.Ui_MainWindow()
    comparator.setupUi(window)
    window.show()

    sys.excepthook = exception_hook
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
