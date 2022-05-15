###                                                                             Main Script

##                                                                  This is where the whole QR Code Generator is run

# IMPORTS
import QR_Logic, QR_UI, platform, helper_funcs, os
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys

    if platform.system() == "Windows":

        # Path to Youtube Icon
        QR_ICON = os.path.join("pics", "qr-code.png")

        # Execute program only if OS is Windows
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QR_Logic.QRMainWindow()

        # Set the window icon
        MainWindow.setWindowIcon(QtGui.QIcon(QR_ICON))

        # Set Window icon in PyQt5
        ui = QR_UI.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    else:
        helper_funcs.show_error("OS Error", "The Youtube Video Downloader only works for Windows")