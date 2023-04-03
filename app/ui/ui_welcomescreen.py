# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomescreen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1074, 741)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.appContainer = QWidget(Dialog)
        self.appContainer.setObjectName(u"appContainer")
        self.appContainer.setMaximumSize(QSize(1200, 800))
        self.appContainer.setStyleSheet(u"QWidget#appContainer {\n"
"	background-color: rgb(239, 239, 239);\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
" 	border: none;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.gridLayout = QGridLayout(self.appContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.SendPacketButton = QPushButton(self.appContainer)
        self.SendPacketButton.setObjectName(u"SendPacketButton")

        self.gridLayout.addWidget(self.SendPacketButton, 2, 0, 1, 1)

        self.ProtocolSelection = QGroupBox(self.appContainer)
        self.ProtocolSelection.setObjectName(u"ProtocolSelection")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProtocolSelection.sizePolicy().hasHeightForWidth())
        self.ProtocolSelection.setSizePolicy(sizePolicy)
        self.ProtocolSelection.setMinimumSize(QSize(0, 100))
        self.ProtocolSelection.setMaximumSize(QSize(500, 100))
        self.ProtocolSelection.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.ProtocolSelection)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.ProtocolSelectionConctainer = QHBoxLayout()
        self.ProtocolSelectionConctainer.setSpacing(0)
        self.ProtocolSelectionConctainer.setObjectName(u"ProtocolSelectionConctainer")
        self.ProtocolSelectionConctainer.setSizeConstraint(QLayout.SetMinimumSize)
        self.ProtocolSelectionLabel = QLabel(self.ProtocolSelection)
        self.ProtocolSelectionLabel.setObjectName(u"ProtocolSelectionLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProtocolSelectionLabel.sizePolicy().hasHeightForWidth())
        self.ProtocolSelectionLabel.setSizePolicy(sizePolicy1)
        self.ProtocolSelectionLabel.setMinimumSize(QSize(0, 0))
        self.ProtocolSelectionLabel.setMaximumSize(QSize(500, 300))
        font = QFont()
        font.setPointSize(12)
        self.ProtocolSelectionLabel.setFont(font)

        self.ProtocolSelectionConctainer.addWidget(self.ProtocolSelectionLabel)

        self.ProtocolSelectionInput = QComboBox(self.ProtocolSelection)
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.setObjectName(u"ProtocolSelectionInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ProtocolSelectionInput.sizePolicy().hasHeightForWidth())
        self.ProtocolSelectionInput.setSizePolicy(sizePolicy2)
        self.ProtocolSelectionInput.setMinimumSize(QSize(0, 50))
        self.ProtocolSelectionInput.setMaximumSize(QSize(250, 50))

        self.ProtocolSelectionConctainer.addWidget(self.ProtocolSelectionInput)


        self.verticalLayout_4.addLayout(self.ProtocolSelectionConctainer)


        self.gridLayout.addWidget(self.ProtocolSelection, 0, 0, 1, 1)

        self.PacketResults = QStackedWidget(self.appContainer)
        self.PacketResults.setObjectName(u"PacketResults")
        self.packet_results_page_1 = QWidget()
        self.packet_results_page_1.setObjectName(u"packet_results_page_1")
        self.verticalLayout_2 = QVBoxLayout(self.packet_results_page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.packets_sent_container = QGroupBox(self.packet_results_page_1)
        self.packets_sent_container.setObjectName(u"packets_sent_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.packets_sent_container.sizePolicy().hasHeightForWidth())
        self.packets_sent_container.setSizePolicy(sizePolicy3)
        self.packets_sent_container.setMaximumSize(QSize(500, 600))
        self.verticalLayout_3 = QVBoxLayout(self.packets_sent_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.packets_sent_container)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(450, 550))
        self.scrollArea.setMaximumSize(QSize(500, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 548))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.packet_list = QVBoxLayout()
        self.packet_list.setObjectName(u"packet_list")

        self.verticalLayout_11.addLayout(self.packet_list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.packets_sent_container)

        self.PacketResults.addWidget(self.packet_results_page_1)

        self.gridLayout.addWidget(self.PacketResults, 0, 1, 2, 1)

        self.ProtocolsContainer = QStackedWidget(self.appContainer)
        self.ProtocolsContainer.setObjectName(u"ProtocolsContainer")
        sizePolicy3.setHeightForWidth(self.ProtocolsContainer.sizePolicy().hasHeightForWidth())
        self.ProtocolsContainer.setSizePolicy(sizePolicy3)
        self.ProtocolsContainer.setMinimumSize(QSize(500, 302))
        self.ProtocolsContainer.setMaximumSize(QSize(500, 500))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMaximumSize(QSize(500, 300))
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.IPProtocolDetails = QGroupBox(self.page_2)
        self.IPProtocolDetails.setObjectName(u"IPProtocolDetails")
        self.IPProtocolDetails.setEnabled(True)
        self.IPProtocolDetails.setMaximumSize(QSize(500, 500))
        self.IPProtocolDetails.setAcceptDrops(False)
        self.IPProtocolDetails.setStyleSheet(u"")
        self.IPProtocolDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_5 = QVBoxLayout(self.IPProtocolDetails)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.SourceMacAddressContainer_4 = QHBoxLayout()
        self.SourceMacAddressContainer_4.setSpacing(0)
        self.SourceMacAddressContainer_4.setObjectName(u"SourceMacAddressContainer_4")
        self.SourceMacAddressContainer_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_4.setContentsMargins(0, -1, -1, -1)
        self.SourceMacAddressLabel_4 = QLabel(self.IPProtocolDetails)
        self.SourceMacAddressLabel_4.setObjectName(u"SourceMacAddressLabel_4")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressLabel_4.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_4.setSizePolicy(sizePolicy3)
        self.SourceMacAddressLabel_4.setMinimumSize(QSize(0, 100))
        self.SourceMacAddressLabel_4.setMaximumSize(QSize(200, 150))
        self.SourceMacAddressLabel_4.setFont(font)

        self.SourceMacAddressContainer_4.addWidget(self.SourceMacAddressLabel_4)

        self.SourceMacAddressInput_8 = QLineEdit(self.IPProtocolDetails)
        self.SourceMacAddressInput_8.setObjectName(u"SourceMacAddressInput_8")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressInput_8.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_8.setSizePolicy(sizePolicy3)
        self.SourceMacAddressInput_8.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_8.setProperty("MAC_ADDRESS", False)
        self.SourceMacAddressInput_8.setProperty("IP", True)

        self.SourceMacAddressContainer_4.addWidget(self.SourceMacAddressInput_8)


        self.verticalLayout_5.addLayout(self.SourceMacAddressContainer_4)

        self.DestinationMacAddressContainer_4 = QHBoxLayout()
        self.DestinationMacAddressContainer_4.setSpacing(0)
        self.DestinationMacAddressContainer_4.setObjectName(u"DestinationMacAddressContainer_4")
        self.DestinationMacAddressContainer_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressLabel_4 = QLabel(self.IPProtocolDetails)
        self.DestinationMacAddressLabel_4.setObjectName(u"DestinationMacAddressLabel_4")
        sizePolicy3.setHeightForWidth(self.DestinationMacAddressLabel_4.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_4.setSizePolicy(sizePolicy3)
        self.DestinationMacAddressLabel_4.setMinimumSize(QSize(200, 0))
        self.DestinationMacAddressLabel_4.setMaximumSize(QSize(200, 50))
        self.DestinationMacAddressLabel_4.setFont(font)

        self.DestinationMacAddressContainer_4.addWidget(self.DestinationMacAddressLabel_4)

        self.SourceMacAddressInput_9 = QLineEdit(self.IPProtocolDetails)
        self.SourceMacAddressInput_9.setObjectName(u"SourceMacAddressInput_9")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressInput_9.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_9.setSizePolicy(sizePolicy3)
        self.SourceMacAddressInput_9.setMinimumSize(QSize(200, 50))
        self.SourceMacAddressInput_9.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.SourceMacAddressInput_9.setProperty("MAC_ADDRESS", False)
        self.SourceMacAddressInput_9.setProperty("IP", True)

        self.DestinationMacAddressContainer_4.addWidget(self.SourceMacAddressInput_9)


        self.verticalLayout_5.addLayout(self.DestinationMacAddressContainer_4)

        self.PayloadContainer_5 = QHBoxLayout()
        self.PayloadContainer_5.setSpacing(0)
        self.PayloadContainer_5.setObjectName(u"PayloadContainer_5")
        self.PayloadContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.PayloadLabel_5 = QLabel(self.IPProtocolDetails)
        self.PayloadLabel_5.setObjectName(u"PayloadLabel_5")
        sizePolicy3.setHeightForWidth(self.PayloadLabel_5.sizePolicy().hasHeightForWidth())
        self.PayloadLabel_5.setSizePolicy(sizePolicy3)
        self.PayloadLabel_5.setMinimumSize(QSize(200, 0))
        self.PayloadLabel_5.setMaximumSize(QSize(200, 50))
        self.PayloadLabel_5.setFont(font)

        self.PayloadContainer_5.addWidget(self.PayloadLabel_5)

        self.PayloadInput_5 = QLineEdit(self.IPProtocolDetails)
        self.PayloadInput_5.setObjectName(u"PayloadInput_5")
        sizePolicy3.setHeightForWidth(self.PayloadInput_5.sizePolicy().hasHeightForWidth())
        self.PayloadInput_5.setSizePolicy(sizePolicy3)
        self.PayloadInput_5.setMinimumSize(QSize(250, 50))
        self.PayloadInput_5.setMaximumSize(QSize(200, 50))

        self.PayloadContainer_5.addWidget(self.PayloadInput_5)


        self.verticalLayout_5.addLayout(self.PayloadContainer_5)


        self.verticalLayout_7.addWidget(self.IPProtocolDetails)

        self.ProtocolsContainer.addWidget(self.page_2)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy3.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy3)
        self.page_1.setMaximumSize(QSize(500, 300))
        self.verticalLayout_8 = QVBoxLayout(self.page_1)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.IPProtocolDetails_2 = QGroupBox(self.page_1)
        self.IPProtocolDetails_2.setObjectName(u"IPProtocolDetails_2")
        self.IPProtocolDetails_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.IPProtocolDetails_2.sizePolicy().hasHeightForWidth())
        self.IPProtocolDetails_2.setSizePolicy(sizePolicy3)
        self.IPProtocolDetails_2.setMinimumSize(QSize(0, 100))
        self.IPProtocolDetails_2.setMaximumSize(QSize(500, 500))
        self.IPProtocolDetails_2.setAcceptDrops(False)
        self.IPProtocolDetails_2.setStyleSheet(u"")
        self.IPProtocolDetails_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_6 = QVBoxLayout(self.IPProtocolDetails_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SourceMacAddressContainer_5 = QHBoxLayout()
        self.SourceMacAddressContainer_5.setSpacing(0)
        self.SourceMacAddressContainer_5.setObjectName(u"SourceMacAddressContainer_5")
        self.SourceMacAddressContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_5.setContentsMargins(0, -1, -1, 9)
        self.SourceMacAddressLabel_5 = QLabel(self.IPProtocolDetails_2)
        self.SourceMacAddressLabel_5.setObjectName(u"SourceMacAddressLabel_5")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressLabel_5.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_5.setSizePolicy(sizePolicy1)
        self.SourceMacAddressLabel_5.setMinimumSize(QSize(200, 50))
        self.SourceMacAddressLabel_5.setMaximumSize(QSize(200, 50))
        self.SourceMacAddressLabel_5.setFont(font)

        self.SourceMacAddressContainer_5.addWidget(self.SourceMacAddressLabel_5)

        self.SourceMacAddressInput_10 = QLineEdit(self.IPProtocolDetails_2)
        self.SourceMacAddressInput_10.setObjectName(u"SourceMacAddressInput_10")
        sizePolicy2.setHeightForWidth(self.SourceMacAddressInput_10.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_10.setSizePolicy(sizePolicy2)
        self.SourceMacAddressInput_10.setMinimumSize(QSize(250, 50))
        self.SourceMacAddressInput_10.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_10.setProperty("MAC_ADDRESS", True)

        self.SourceMacAddressContainer_5.addWidget(self.SourceMacAddressInput_10)


        self.verticalLayout_6.addLayout(self.SourceMacAddressContainer_5)

        self.DestinationMacAddressContainer_5 = QHBoxLayout()
        self.DestinationMacAddressContainer_5.setSpacing(0)
        self.DestinationMacAddressContainer_5.setObjectName(u"DestinationMacAddressContainer_5")
        self.DestinationMacAddressContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressLabel_5 = QLabel(self.IPProtocolDetails_2)
        self.DestinationMacAddressLabel_5.setObjectName(u"DestinationMacAddressLabel_5")
        sizePolicy1.setHeightForWidth(self.DestinationMacAddressLabel_5.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_5.setSizePolicy(sizePolicy1)
        self.DestinationMacAddressLabel_5.setMinimumSize(QSize(200, 50))
        self.DestinationMacAddressLabel_5.setMaximumSize(QSize(200, 50))
        self.DestinationMacAddressLabel_5.setFont(font)

        self.DestinationMacAddressContainer_5.addWidget(self.DestinationMacAddressLabel_5)

        self.SourceMacAddressInput_11 = QLineEdit(self.IPProtocolDetails_2)
        self.SourceMacAddressInput_11.setObjectName(u"SourceMacAddressInput_11")
        sizePolicy2.setHeightForWidth(self.SourceMacAddressInput_11.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_11.setSizePolicy(sizePolicy2)
        self.SourceMacAddressInput_11.setMinimumSize(QSize(200, 50))
        self.SourceMacAddressInput_11.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_11.setProperty("MAC_ADDRESS", True)

        self.DestinationMacAddressContainer_5.addWidget(self.SourceMacAddressInput_11)


        self.verticalLayout_6.addLayout(self.DestinationMacAddressContainer_5)


        self.verticalLayout_8.addWidget(self.IPProtocolDetails_2)

        self.ProtocolsContainer.addWidget(self.page_1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setMinimumSize(QSize(0, 100))
        self.page.setMaximumSize(QSize(500, 300))
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetNoConstraint)
        self.ARPProtocolDetails = QGroupBox(self.page)
        self.ARPProtocolDetails.setObjectName(u"ARPProtocolDetails")
        self.ARPProtocolDetails.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ARPProtocolDetails.sizePolicy().hasHeightForWidth())
        self.ARPProtocolDetails.setSizePolicy(sizePolicy)
        self.ARPProtocolDetails.setMinimumSize(QSize(0, 100))
        self.ARPProtocolDetails.setMaximumSize(QSize(500, 150))
        self.ARPProtocolDetails.setAcceptDrops(False)
        self.ARPProtocolDetails.setStyleSheet(u"")
        self.ARPProtocolDetails.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_9 = QVBoxLayout(self.ARPProtocolDetails)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.SourceMacAddressContainer_7 = QHBoxLayout()
        self.SourceMacAddressContainer_7.setSpacing(0)
        self.SourceMacAddressContainer_7.setObjectName(u"SourceMacAddressContainer_7")
        self.SourceMacAddressContainer_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_7.setContentsMargins(0, -1, -1, -1)
        self.SourceMacAddressLabel_7 = QLabel(self.ARPProtocolDetails)
        self.SourceMacAddressLabel_7.setObjectName(u"SourceMacAddressLabel_7")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressLabel_7.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_7.setSizePolicy(sizePolicy3)
        self.SourceMacAddressLabel_7.setMaximumSize(QSize(200, 50))
        self.SourceMacAddressLabel_7.setFont(font)

        self.SourceMacAddressContainer_7.addWidget(self.SourceMacAddressLabel_7)

        self.SourceMacAddressInput_12 = QLineEdit(self.ARPProtocolDetails)
        self.SourceMacAddressInput_12.setObjectName(u"SourceMacAddressInput_12")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressInput_12.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_12.setSizePolicy(sizePolicy3)
        self.SourceMacAddressInput_12.setMinimumSize(QSize(200, 50))
        self.SourceMacAddressInput_12.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_12.setProperty("MAC_ADDRESS", True)

        self.SourceMacAddressContainer_7.addWidget(self.SourceMacAddressInput_12)


        self.verticalLayout_9.addLayout(self.SourceMacAddressContainer_7)

        self.DestinationMacAddressContainer_7 = QHBoxLayout()
        self.DestinationMacAddressContainer_7.setSpacing(0)
        self.DestinationMacAddressContainer_7.setObjectName(u"DestinationMacAddressContainer_7")
        self.DestinationMacAddressContainer_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressLabel_7 = QLabel(self.ARPProtocolDetails)
        self.DestinationMacAddressLabel_7.setObjectName(u"DestinationMacAddressLabel_7")
        sizePolicy1.setHeightForWidth(self.DestinationMacAddressLabel_7.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_7.setSizePolicy(sizePolicy1)
        self.DestinationMacAddressLabel_7.setMaximumSize(QSize(200, 50))
        self.DestinationMacAddressLabel_7.setFont(font)

        self.DestinationMacAddressContainer_7.addWidget(self.DestinationMacAddressLabel_7)

        self.SourceMacAddressInput_13 = QLineEdit(self.ARPProtocolDetails)
        self.SourceMacAddressInput_13.setObjectName(u"SourceMacAddressInput_13")
        sizePolicy3.setHeightForWidth(self.SourceMacAddressInput_13.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_13.setSizePolicy(sizePolicy3)
        self.SourceMacAddressInput_13.setMinimumSize(QSize(200, 50))
        self.SourceMacAddressInput_13.setMaximumSize(QSize(250, 50))
        self.SourceMacAddressInput_13.setProperty("MAC_ADDRESS", True)

        self.DestinationMacAddressContainer_7.addWidget(self.SourceMacAddressInput_13)


        self.verticalLayout_9.addLayout(self.DestinationMacAddressContainer_7)


        self.verticalLayout_10.addWidget(self.ARPProtocolDetails)

        self.ProtocolsContainer.addWidget(self.page)

        self.gridLayout.addWidget(self.ProtocolsContainer, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.appContainer, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.PacketResults.setCurrentIndex(0)
        self.ProtocolsContainer.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SendPacketButton.setText(QCoreApplication.translate("Dialog", u"Send Packet", None))
        self.ProtocolSelection.setTitle(QCoreApplication.translate("Dialog", u"Protocol Selection", None))
        self.ProtocolSelectionLabel.setText(QCoreApplication.translate("Dialog", u"Protocol Selection", None))
        self.ProtocolSelectionInput.setItemText(0, QCoreApplication.translate("Dialog", u"IP", None))
        self.ProtocolSelectionInput.setItemText(1, QCoreApplication.translate("Dialog", u"DNS", None))
        self.ProtocolSelectionInput.setItemText(2, QCoreApplication.translate("Dialog", u"ARP", None))

        self.packets_sent_container.setTitle(QCoreApplication.translate("Dialog", u"Packets Sent and Received", None))
        self.IPProtocolDetails.setTitle(QCoreApplication.translate("Dialog", u"IP Protocol Details", None))
        self.SourceMacAddressLabel_4.setText(QCoreApplication.translate("Dialog", u"Source IP Address", None))
        self.SourceMacAddressInput_8.setText("")
        self.SourceMacAddressInput_8.setPlaceholderText(QCoreApplication.translate("Dialog", u"00:11:22:33:44:55", None))
        self.DestinationMacAddressLabel_4.setText(QCoreApplication.translate("Dialog", u"Destination IP Address", None))
        self.SourceMacAddressInput_9.setText("")
        self.SourceMacAddressInput_9.setPlaceholderText("")
        self.PayloadLabel_5.setText(QCoreApplication.translate("Dialog", u"Payload", None))
        self.PayloadInput_5.setText("")
        self.PayloadInput_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"Payload", None))
        self.IPProtocolDetails_2.setTitle(QCoreApplication.translate("Dialog", u"DNS Protocol Details", None))
        self.SourceMacAddressLabel_5.setText(QCoreApplication.translate("Dialog", u"Source MAC Address", None))
        self.SourceMacAddressInput_10.setText("")
        self.SourceMacAddressInput_10.setPlaceholderText(QCoreApplication.translate("Dialog", u"00:11:22:33:44:55", None))
        self.DestinationMacAddressLabel_5.setText(QCoreApplication.translate("Dialog", u"Destination MAC Address", None))
        self.SourceMacAddressInput_11.setText("")
        self.SourceMacAddressInput_11.setPlaceholderText(QCoreApplication.translate("Dialog", u"00:11:22:33:44:55", None))
        self.ARPProtocolDetails.setTitle(QCoreApplication.translate("Dialog", u"ARP Protocol Details", None))
        self.SourceMacAddressLabel_7.setText(QCoreApplication.translate("Dialog", u"Source MAC Address", None))
        self.SourceMacAddressInput_12.setText("")
        self.SourceMacAddressInput_12.setPlaceholderText(QCoreApplication.translate("Dialog", u"00:11:22:33:44:55", None))
        self.DestinationMacAddressLabel_7.setText(QCoreApplication.translate("Dialog", u"Destination MAC Address", None))
        self.SourceMacAddressInput_13.setText("")
        self.SourceMacAddressInput_13.setPlaceholderText(QCoreApplication.translate("Dialog", u"00:11:22:33:44:55", None))
    # retranslateUi

