# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deck_options_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeckOptionsPlaceholder(object):
    def setupUi(self, DeckOptionsPlaceholder):
        DeckOptionsPlaceholder.setObjectName("DeckOptionsPlaceholder")
        DeckOptionsPlaceholder.resize(318, 241)
        self.verticalLayout = QtWidgets.QVBoxLayout(DeckOptionsPlaceholder)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DeckOptionsPlaceholder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 318, 76))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setContentsMargins(6, 6, 6, 6)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")
        self.reverseWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reverseWidget.sizePolicy().hasHeightForWidth())
        self.reverseWidget.setSizePolicy(sizePolicy)
        self.reverseWidget.setMinimumSize(QtCore.QSize(32, 64))
        self.reverseWidget.setObjectName("reverseWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.reverseWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollAreaLayout.addWidget(self.reverseWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(DeckOptionsPlaceholder)
        QtCore.QMetaObject.connectSlotsByName(DeckOptionsPlaceholder)

    def retranslateUi(self, DeckOptionsPlaceholder):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeckOptionsPlaceholder = QtWidgets.QWidget()
    ui = Ui_DeckOptionsPlaceholder()
    ui.setupUi(DeckOptionsPlaceholder)
    DeckOptionsPlaceholder.show()
    sys.exit(app.exec_())
