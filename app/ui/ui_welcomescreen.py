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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1074, 741)
        self.appContainer = QWidget(Dialog)
        self.appContainer.setObjectName(u"appContainer")
        self.appContainer.setGeometry(QRect(-10, 0, 1200, 800))
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
        self.ProtocolSelection = QGroupBox(self.appContainer)
        self.ProtocolSelection.setObjectName(u"ProtocolSelection")
        self.ProtocolSelection.setGeometry(QRect(20, 20, 471, 91))
        self.ProtocolSelection.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.ProtocolSelection)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 441, 41))
        self.ProtocolSelectionConctainer = QHBoxLayout(self.horizontalLayoutWidget)
        self.ProtocolSelectionConctainer.setSpacing(0)
        self.ProtocolSelectionConctainer.setObjectName(u"ProtocolSelectionConctainer")
        self.ProtocolSelectionConctainer.setSizeConstraint(QLayout.SetMaximumSize)
        self.ProtocolSelectionConctainer.setContentsMargins(0, 0, 0, 0)
        self.ProtocolSelectionLabel = QLabel(self.horizontalLayoutWidget)
        self.ProtocolSelectionLabel.setObjectName(u"ProtocolSelectionLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProtocolSelectionLabel.sizePolicy().hasHeightForWidth())
        self.ProtocolSelectionLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.ProtocolSelectionLabel.setFont(font)

        self.ProtocolSelectionConctainer.addWidget(self.ProtocolSelectionLabel)

        self.ProtocolSelectionInput = QComboBox(self.horizontalLayoutWidget)
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.addItem("")
        self.ProtocolSelectionInput.setObjectName(u"ProtocolSelectionInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ProtocolSelectionInput.sizePolicy().hasHeightForWidth())
        self.ProtocolSelectionInput.setSizePolicy(sizePolicy1)

        self.ProtocolSelectionConctainer.addWidget(self.ProtocolSelectionInput)

        self.ProtocolsContainer = QStackedWidget(self.appContainer)
        self.ProtocolsContainer.setObjectName(u"ProtocolsContainer")
        self.ProtocolsContainer.setGeometry(QRect(20, 110, 491, 511))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.IPProtocolDetails = QGroupBox(self.page_2)
        self.IPProtocolDetails.setObjectName(u"IPProtocolDetails")
        self.IPProtocolDetails.setEnabled(True)
        self.IPProtocolDetails.setGeometry(QRect(0, 0, 471, 511))
        self.IPProtocolDetails.setAcceptDrops(False)
        self.IPProtocolDetails.setStyleSheet(u"")
        self.horizontalLayoutWidget_23 = QWidget(self.IPProtocolDetails)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(10, 30, 441, 41))
        self.SourceMacAddressContainer_4 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.SourceMacAddressContainer_4.setSpacing(0)
        self.SourceMacAddressContainer_4.setObjectName(u"SourceMacAddressContainer_4")
        self.SourceMacAddressContainer_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_4.setContentsMargins(0, 0, 0, 0)
        self.SourceMacAddressLabel_4 = QLabel(self.horizontalLayoutWidget_23)
        self.SourceMacAddressLabel_4.setObjectName(u"SourceMacAddressLabel_4")
        sizePolicy.setHeightForWidth(self.SourceMacAddressLabel_4.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_4.setSizePolicy(sizePolicy)
        self.SourceMacAddressLabel_4.setFont(font)

        self.SourceMacAddressContainer_4.addWidget(self.SourceMacAddressLabel_4)

        self.SourceMacAddressInput_8 = QLineEdit(self.horizontalLayoutWidget_23)
        self.SourceMacAddressInput_8.setObjectName(u"SourceMacAddressInput_8")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_8.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_8.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_8.setProperty("MAC_ADDRESS", False)
        self.SourceMacAddressInput_8.setProperty("IP", True)

        self.SourceMacAddressContainer_4.addWidget(self.SourceMacAddressInput_8)

        self.horizontalLayoutWidget_24 = QWidget(self.IPProtocolDetails)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(10, 90, 441, 41))
        self.DestinationMacAddressContainer_4 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.DestinationMacAddressContainer_4.setSpacing(0)
        self.DestinationMacAddressContainer_4.setObjectName(u"DestinationMacAddressContainer_4")
        self.DestinationMacAddressContainer_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressContainer_4.setContentsMargins(0, 0, 0, 0)
        self.DestinationMacAddressLabel_4 = QLabel(self.horizontalLayoutWidget_24)
        self.DestinationMacAddressLabel_4.setObjectName(u"DestinationMacAddressLabel_4")
        sizePolicy.setHeightForWidth(self.DestinationMacAddressLabel_4.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_4.setSizePolicy(sizePolicy)
        self.DestinationMacAddressLabel_4.setFont(font)

        self.DestinationMacAddressContainer_4.addWidget(self.DestinationMacAddressLabel_4)

        self.SourceMacAddressInput_9 = QLineEdit(self.horizontalLayoutWidget_24)
        self.SourceMacAddressInput_9.setObjectName(u"SourceMacAddressInput_9")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_9.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_9.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_9.setProperty("MAC_ADDRESS", False)
        self.SourceMacAddressInput_9.setProperty("IP", True)

        self.DestinationMacAddressContainer_4.addWidget(self.SourceMacAddressInput_9)

        self.horizontalLayoutWidget_25 = QWidget(self.IPProtocolDetails)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(10, 150, 439, 39))
        self.PayloadContainer_5 = QHBoxLayout(self.horizontalLayoutWidget_25)
        self.PayloadContainer_5.setSpacing(0)
        self.PayloadContainer_5.setObjectName(u"PayloadContainer_5")
        self.PayloadContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.PayloadContainer_5.setContentsMargins(0, 0, 0, 0)
        self.PayloadLabel_5 = QLabel(self.horizontalLayoutWidget_25)
        self.PayloadLabel_5.setObjectName(u"PayloadLabel_5")
        sizePolicy1.setHeightForWidth(self.PayloadLabel_5.sizePolicy().hasHeightForWidth())
        self.PayloadLabel_5.setSizePolicy(sizePolicy1)
        self.PayloadLabel_5.setFont(font)

        self.PayloadContainer_5.addWidget(self.PayloadLabel_5)

        self.PayloadInput_5 = QLineEdit(self.horizontalLayoutWidget_25)
        self.PayloadInput_5.setObjectName(u"PayloadInput_5")
        sizePolicy1.setHeightForWidth(self.PayloadInput_5.sizePolicy().hasHeightForWidth())
        self.PayloadInput_5.setSizePolicy(sizePolicy1)

        self.PayloadContainer_5.addWidget(self.PayloadInput_5)

        self.ProtocolsContainer.addWidget(self.page_2)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.IPProtocolDetails_2 = QGroupBox(self.page_1)
        self.IPProtocolDetails_2.setObjectName(u"IPProtocolDetails_2")
        self.IPProtocolDetails_2.setEnabled(True)
        self.IPProtocolDetails_2.setGeometry(QRect(0, 0, 471, 511))
        self.IPProtocolDetails_2.setAcceptDrops(False)
        self.IPProtocolDetails_2.setStyleSheet(u"")
        self.horizontalLayoutWidget_26 = QWidget(self.IPProtocolDetails_2)
        self.horizontalLayoutWidget_26.setObjectName(u"horizontalLayoutWidget_26")
        self.horizontalLayoutWidget_26.setGeometry(QRect(10, 30, 441, 41))
        self.SourceMacAddressContainer_5 = QHBoxLayout(self.horizontalLayoutWidget_26)
        self.SourceMacAddressContainer_5.setSpacing(0)
        self.SourceMacAddressContainer_5.setObjectName(u"SourceMacAddressContainer_5")
        self.SourceMacAddressContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_5.setContentsMargins(0, 0, 0, 0)
        self.SourceMacAddressLabel_5 = QLabel(self.horizontalLayoutWidget_26)
        self.SourceMacAddressLabel_5.setObjectName(u"SourceMacAddressLabel_5")
        sizePolicy.setHeightForWidth(self.SourceMacAddressLabel_5.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_5.setSizePolicy(sizePolicy)
        self.SourceMacAddressLabel_5.setFont(font)

        self.SourceMacAddressContainer_5.addWidget(self.SourceMacAddressLabel_5)

        self.SourceMacAddressInput_10 = QLineEdit(self.horizontalLayoutWidget_26)
        self.SourceMacAddressInput_10.setObjectName(u"SourceMacAddressInput_10")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_10.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_10.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_10.setProperty("MAC_ADDRESS", True)

        self.SourceMacAddressContainer_5.addWidget(self.SourceMacAddressInput_10)

        self.horizontalLayoutWidget_27 = QWidget(self.IPProtocolDetails_2)
        self.horizontalLayoutWidget_27.setObjectName(u"horizontalLayoutWidget_27")
        self.horizontalLayoutWidget_27.setGeometry(QRect(10, 90, 441, 41))
        self.DestinationMacAddressContainer_5 = QHBoxLayout(self.horizontalLayoutWidget_27)
        self.DestinationMacAddressContainer_5.setSpacing(0)
        self.DestinationMacAddressContainer_5.setObjectName(u"DestinationMacAddressContainer_5")
        self.DestinationMacAddressContainer_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressContainer_5.setContentsMargins(0, 0, 0, 0)
        self.DestinationMacAddressLabel_5 = QLabel(self.horizontalLayoutWidget_27)
        self.DestinationMacAddressLabel_5.setObjectName(u"DestinationMacAddressLabel_5")
        sizePolicy.setHeightForWidth(self.DestinationMacAddressLabel_5.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_5.setSizePolicy(sizePolicy)
        self.DestinationMacAddressLabel_5.setFont(font)

        self.DestinationMacAddressContainer_5.addWidget(self.DestinationMacAddressLabel_5)

        self.SourceMacAddressInput_11 = QLineEdit(self.horizontalLayoutWidget_27)
        self.SourceMacAddressInput_11.setObjectName(u"SourceMacAddressInput_11")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_11.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_11.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_11.setProperty("MAC_ADDRESS", True)

        self.DestinationMacAddressContainer_5.addWidget(self.SourceMacAddressInput_11)

        self.ProtocolsContainer.addWidget(self.page_1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.ARPProtocolDetails = QGroupBox(self.page)
        self.ARPProtocolDetails.setObjectName(u"ARPProtocolDetails")
        self.ARPProtocolDetails.setEnabled(True)
        self.ARPProtocolDetails.setGeometry(QRect(0, 0, 471, 511))
        self.ARPProtocolDetails.setAcceptDrops(False)
        self.ARPProtocolDetails.setStyleSheet(u"")
        self.horizontalLayoutWidget_32 = QWidget(self.ARPProtocolDetails)
        self.horizontalLayoutWidget_32.setObjectName(u"horizontalLayoutWidget_32")
        self.horizontalLayoutWidget_32.setGeometry(QRect(10, 30, 441, 41))
        self.SourceMacAddressContainer_7 = QHBoxLayout(self.horizontalLayoutWidget_32)
        self.SourceMacAddressContainer_7.setSpacing(0)
        self.SourceMacAddressContainer_7.setObjectName(u"SourceMacAddressContainer_7")
        self.SourceMacAddressContainer_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.SourceMacAddressContainer_7.setContentsMargins(0, 0, 0, 0)
        self.SourceMacAddressLabel_7 = QLabel(self.horizontalLayoutWidget_32)
        self.SourceMacAddressLabel_7.setObjectName(u"SourceMacAddressLabel_7")
        sizePolicy.setHeightForWidth(self.SourceMacAddressLabel_7.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressLabel_7.setSizePolicy(sizePolicy)
        self.SourceMacAddressLabel_7.setFont(font)

        self.SourceMacAddressContainer_7.addWidget(self.SourceMacAddressLabel_7)

        self.SourceMacAddressInput_12 = QLineEdit(self.horizontalLayoutWidget_32)
        self.SourceMacAddressInput_12.setObjectName(u"SourceMacAddressInput_12")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_12.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_12.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_12.setProperty("MAC_ADDRESS", True)

        self.SourceMacAddressContainer_7.addWidget(self.SourceMacAddressInput_12)

        self.horizontalLayoutWidget_33 = QWidget(self.ARPProtocolDetails)
        self.horizontalLayoutWidget_33.setObjectName(u"horizontalLayoutWidget_33")
        self.horizontalLayoutWidget_33.setGeometry(QRect(10, 90, 441, 41))
        self.DestinationMacAddressContainer_7 = QHBoxLayout(self.horizontalLayoutWidget_33)
        self.DestinationMacAddressContainer_7.setSpacing(0)
        self.DestinationMacAddressContainer_7.setObjectName(u"DestinationMacAddressContainer_7")
        self.DestinationMacAddressContainer_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.DestinationMacAddressContainer_7.setContentsMargins(0, 0, 0, 0)
        self.DestinationMacAddressLabel_7 = QLabel(self.horizontalLayoutWidget_33)
        self.DestinationMacAddressLabel_7.setObjectName(u"DestinationMacAddressLabel_7")
        sizePolicy.setHeightForWidth(self.DestinationMacAddressLabel_7.sizePolicy().hasHeightForWidth())
        self.DestinationMacAddressLabel_7.setSizePolicy(sizePolicy)
        self.DestinationMacAddressLabel_7.setFont(font)

        self.DestinationMacAddressContainer_7.addWidget(self.DestinationMacAddressLabel_7)

        self.SourceMacAddressInput_13 = QLineEdit(self.horizontalLayoutWidget_33)
        self.SourceMacAddressInput_13.setObjectName(u"SourceMacAddressInput_13")
        sizePolicy1.setHeightForWidth(self.SourceMacAddressInput_13.sizePolicy().hasHeightForWidth())
        self.SourceMacAddressInput_13.setSizePolicy(sizePolicy1)
        self.SourceMacAddressInput_13.setProperty("MAC_ADDRESS", True)

        self.DestinationMacAddressContainer_7.addWidget(self.SourceMacAddressInput_13)

        self.ProtocolsContainer.addWidget(self.page)
        self.SendPacketButton = QPushButton(self.appContainer)
        self.SendPacketButton.setObjectName(u"SendPacketButton")
        self.SendPacketButton.setGeometry(QRect(20, 630, 491, 81))
        self.PacketResults = QStackedWidget(self.appContainer)
        self.PacketResults.setObjectName(u"PacketResults")
        self.PacketResults.setGeometry(QRect(570, 10, 491, 701))
        self.packet_results_page_1 = QWidget()
        self.packet_results_page_1.setObjectName(u"packet_results_page_1")
        self.packets_sent_container = QGroupBox(self.packet_results_page_1)
        self.packets_sent_container.setObjectName(u"packets_sent_container")
        self.packets_sent_container.setGeometry(QRect(0, 0, 491, 621))
        self.scrollArea = QScrollArea(self.packets_sent_container)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 30, 491, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 489, 589))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 491, 591))
        self.packets_list = QVBoxLayout(self.verticalLayoutWidget)
        self.packets_list.setObjectName(u"packets_list")
        self.packets_list.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.packets_list.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.PacketResults.addWidget(self.packet_results_page_1)

        self.retranslateUi(Dialog)

        self.ProtocolsContainer.setCurrentIndex(0)
        self.PacketResults.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ProtocolSelection.setTitle(QCoreApplication.translate("Dialog", u"Protocol Selection", None))
        self.ProtocolSelectionLabel.setText(QCoreApplication.translate("Dialog", u"Protocol Selection", None))
        self.ProtocolSelectionInput.setItemText(0, QCoreApplication.translate("Dialog", u"IP", None))
        self.ProtocolSelectionInput.setItemText(1, QCoreApplication.translate("Dialog", u"DNS", None))
        self.ProtocolSelectionInput.setItemText(2, QCoreApplication.translate("Dialog", u"ARP", None))

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
        self.SendPacketButton.setText(QCoreApplication.translate("Dialog", u"Send Packet", None))
        self.packets_sent_container.setTitle(QCoreApplication.translate("Dialog", u"Packets Sent and Received", None))
    # retranslateUi

