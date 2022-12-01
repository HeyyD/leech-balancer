# Form implementation generated from reading ui file 'set_lapse_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetLapseDialog(object):
    def setupUi(self, SetLapseDialog):
        SetLapseDialog.setObjectName("SetLapseDialog")
        SetLapseDialog.resize(302, 122)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetLapseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SetLapseDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(SetLapseDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.updateLeechesCheckbox = QtWidgets.QCheckBox(SetLapseDialog)
        self.updateLeechesCheckbox.setObjectName("updateLeechesCheckbox")
        self.verticalLayout.addWidget(self.updateLeechesCheckbox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetLapseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SetLapseDialog)
        self.buttonBox.accepted.connect(SetLapseDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(SetLapseDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SetLapseDialog)

    def retranslateUi(self, SetLapseDialog):
        _translate = QtCore.QCoreApplication.translate
        SetLapseDialog.setWindowTitle(_translate("SetLapseDialog", "Set Card Lapse Count"))
        self.label.setText(_translate("SetLapseDialog", "Supports math with the symbols: + - * /\n"
"* 2 = multiply all lapses by 2, etc."))
        self.updateLeechesCheckbox.setToolTip(_translate("SetLapseDialog", "Tags/Un-tags leeches based on their individual lapse counts after being updated."))
        self.updateLeechesCheckbox.setText(_translate("SetLapseDialog", "Update leech status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetLapseDialog = QtWidgets.QDialog()
    ui = Ui_SetLapseDialog()
    ui.setupUi(SetLapseDialog)
    SetLapseDialog.show()
    sys.exit(app.exec())
