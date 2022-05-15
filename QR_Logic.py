##                                                                                    Logic Script of the QR Code Generator

##                                                                  Python Script in charge of making the QR Code Generator work properly

import helper_funcs
import os
from PyQt5 import QtGui, QtWidgets


class QRMainWindow(QtWidgets.QMainWindow):
    """PyQt5 Main Window for the QR Code Generator"""

    def __init__(self):
        """Initialize this PyQt5 QR Code Main Window."""

        # Run the constructor method of the parent
        super(QRMainWindow, self).__init__()

        # The Generate QR Code itself
        self.__qr_code = None

        # The path where the user wants to download the QR Code
        self.__save_location = ""

    def generateQR(self, given_widget):
        """Produces the QR Code."""

        # Get the information to convert to QR code
        infoToQR: object = given_widget.toPlainText().strip()

        # Raise a GUI error message if the user wrote nothing in the QR Code Text box
        if len(infoToQR) == 0:
            helper_funcs.show_error("QR Code Generation Error", "No Information was given to generate a QR Code.")

        # Otherwise, generate the QR code
        else:

            # Generate a file dialog to ask the user where to save the QR Code
            dialog = QtWidgets.QFileDialog(self)
            dialog.setWindowTitle('Open Select QR Code Folder')
            dialog.setDirectory(os.getcwd())
            dialog.setFileMode(dialog.Directory)

            # If the user chose a valid folder, save the QR code with his/her consent
            if dialog.exec_() == QtWidgets.QFileDialog.Accepted:

                # Get the saving location
                self.__save_location = dialog.selectedFiles()[0]

                # Confirm if the user wants to save the QR code
                will_save = helper_funcs.yes_or_no("Save QR Code", "Do you want to download your QR code?")

                if will_save:
                    # Generate and save the QR code
                    self.__qr_code = helper_funcs.getQR(infoToQR)

                    # Save the QR code exactly where the user wants
                    self.__qr_code.save(os.path.join(self.__save_location, "QR_Code.png"), "PNG")

                    # Close the QR code once it is downloaded
                    self.__qr_code.close()

                    # Tell the user the file was saved successfully
                    helper_funcs.show_info("QR Code Success",
                                           "Your QR code was successfully generated and saved in your system.")

                    # Then, clear the information in the QR Code Text Box
                    given_widget.clear()
