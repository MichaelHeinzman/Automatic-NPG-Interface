# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

from ip_4_address_input import IPAddressInput
from ip_packet_configuration import IPConfigurationWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 900)
        MainWindow.setStyleSheet(u"QMainWindow, QWidget#centralwidget, QStackedWidget{\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(54,60,75);\n"
"}\n"
"\n"
"#ip_page, #arp_page, #dns_page {\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"	background-color: rgb(82, 88, 104);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_side = QVBoxLayout()
        self.left_side.setObjectName(u"left_side")
        self.left_side.setContentsMargins(-1, -1, -1, 0)
        self.protocol_selection_container = QVBoxLayout()
        self.protocol_selection_container.setObjectName(u"protocol_selection_container")
        self.protocol_selection_title = QLabel(self.centralwidget)
        self.protocol_selection_title.setObjectName(u"protocol_selection_title")
        font = QFont()
        font.setPointSize(24)
        self.protocol_selection_title.setFont(font)

        self.protocol_selection_container.addWidget(self.protocol_selection_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.protocol_label = QLabel(self.centralwidget)
        self.protocol_label.setObjectName(u"protocol_label")

        self.horizontalLayout.addWidget(self.protocol_label)

        self.protocol_input = QComboBox(self.centralwidget)
        self.protocol_input.addItem("")
        self.protocol_input.addItem("")
        self.protocol_input.addItem("")
        self.protocol_input.setObjectName(u"protocol_input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.protocol_input.sizePolicy().hasHeightForWidth())
        self.protocol_input.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.protocol_input)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.protocol_selection_container.addLayout(self.horizontalLayout)

        self.protocol_selection_container.setStretch(0, 1)
        self.protocol_selection_container.setStretch(1, 1)

        self.left_side.addLayout(self.protocol_selection_container)

        self.first_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_side.addItem(self.first_spacer)

        self.protocol_details_container = QVBoxLayout()
        self.protocol_details_container.setObjectName(u"protocol_details_container")
        self.protocol_details_container.setContentsMargins(-1, -1, -1, 0)
        self.protocol_types_configuration_pages = QStackedWidget(self.centralwidget)
        self.protocol_types_configuration_pages.setObjectName(u"protocol_types_configuration_pages")
        self.ip_page = IPConfigurationWidget()
        self.ip_page.setObjectName(u"ip_page")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(20)
        self.ip_page.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.ip_page)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.protocol_selection_title_3 = QLabel(self.ip_page)
        self.protocol_selection_title_3.setObjectName(u"protocol_selection_title_3")
        sizePolicy.setHeightForWidth(self.protocol_selection_title_3.sizePolicy().hasHeightForWidth())
        self.protocol_selection_title_3.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        self.protocol_selection_title_3.setFont(font2)

        self.verticalLayout.addWidget(self.protocol_selection_title_3)

        self.source_ip_address_layout = QHBoxLayout()
        self.source_ip_address_layout.setObjectName(u"source_ip_address_layout")
        self.source_ip_address_label = QLabel(self.ip_page)
        self.source_ip_address_label.setObjectName(u"source_ip_address_label")
        font3 = QFont()
        font3.setPointSize(14)
        self.source_ip_address_label.setFont(font3)

        self.source_ip_address_layout.addWidget(self.source_ip_address_label)

        self.source_ip_address_input = IPAddressInput(self.ip_page)
        self.source_ip_address_input.setObjectName(u"source_ip_address_input")
        sizePolicy.setHeightForWidth(self.source_ip_address_input.sizePolicy().hasHeightForWidth())
        self.source_ip_address_input.setSizePolicy(sizePolicy)

        self.source_ip_address_layout.addWidget(self.source_ip_address_input)


        self.verticalLayout.addLayout(self.source_ip_address_layout)

        self.ip_payload_layout = QHBoxLayout()
        self.ip_payload_layout.setObjectName(u"ip_payload_layout")
        self.ip_payload_label = QLabel(self.ip_page)
        self.ip_payload_label.setObjectName(u"ip_payload_label")
        self.ip_payload_label.setFont(font3)

        self.ip_payload_layout.addWidget(self.ip_payload_label)

        self.ip_payload_input = QLineEdit(self.ip_page)
        self.ip_payload_input.setObjectName(u"ip_payload_input")
        sizePolicy.setHeightForWidth(self.ip_payload_input.sizePolicy().hasHeightForWidth())
        self.ip_payload_input.setSizePolicy(sizePolicy)

        self.ip_payload_layout.addWidget(self.ip_payload_input)


        self.verticalLayout.addLayout(self.ip_payload_layout)

        self.destination_ip_address_layout = QHBoxLayout()
        self.destination_ip_address_layout.setObjectName(u"destination_ip_address_layout")
        self.destination_ip_address_label = QLabel(self.ip_page)
        self.destination_ip_address_label.setObjectName(u"destination_ip_address_label")
        self.destination_ip_address_label.setFont(font3)

        self.destination_ip_address_layout.addWidget(self.destination_ip_address_label)

        self.destination_ip_address_input = IPAddressInput(self.ip_page)
        self.destination_ip_address_input.setObjectName(u"destination_ip_address_input")
        sizePolicy.setHeightForWidth(self.destination_ip_address_input.sizePolicy().hasHeightForWidth())
        self.destination_ip_address_input.setSizePolicy(sizePolicy)

        self.destination_ip_address_layout.addWidget(self.destination_ip_address_input)


        self.verticalLayout.addLayout(self.destination_ip_address_layout)

        self.number_of_ip_packets_layout = QHBoxLayout()
        self.number_of_ip_packets_layout.setObjectName(u"number_of_ip_packets_layout")
        self.number_of_ip_packets_label = QLabel(self.ip_page)
        self.number_of_ip_packets_label.setObjectName(u"number_of_ip_packets_label")
        self.number_of_ip_packets_label.setFont(font3)

        self.number_of_ip_packets_layout.addWidget(self.number_of_ip_packets_label)

        self.number_of_ip_packets = QLineEdit(self.ip_page)
        self.number_of_ip_packets.setObjectName(u"number_of_ip_packets")
        sizePolicy.setHeightForWidth(self.number_of_ip_packets.sizePolicy().hasHeightForWidth())
        self.number_of_ip_packets.setSizePolicy(sizePolicy)

        self.number_of_ip_packets_layout.addWidget(self.number_of_ip_packets)


        self.verticalLayout.addLayout(self.number_of_ip_packets_layout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.protocol_types_configuration_pages.addWidget(self.ip_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.protocol_types_configuration_pages.addWidget(self.page_2)

        self.protocol_details_container.addWidget(self.protocol_types_configuration_pages)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.protocol_details_container.addItem(self.verticalSpacer)


        self.left_side.addLayout(self.protocol_details_container)

        self.left_side.setStretch(0, 1)
        self.left_side.setStretch(2, 5)

        self.horizontalLayout_2.addLayout(self.left_side)

        self.right_side = QVBoxLayout()
        self.right_side.setSpacing(0)
        self.right_side.setObjectName(u"right_side")
        self.packets_to_send_title = QLabel(self.centralwidget)
        self.packets_to_send_title.setObjectName(u"packets_to_send_title")
        self.packets_to_send_title.setFont(font)

        self.right_side.addWidget(self.packets_to_send_title)

        self.packets_to_send_scroll_container = QScrollArea(self.centralwidget)
        self.packets_to_send_scroll_container.setObjectName(u"packets_to_send_scroll_container")
        sizePolicy.setHeightForWidth(self.packets_to_send_scroll_container.sizePolicy().hasHeightForWidth())
        self.packets_to_send_scroll_container.setSizePolicy(sizePolicy)
        self.packets_to_send_scroll_container.setMinimumSize(QSize(0, 0))
        self.packets_to_send_scroll_container.setMaximumSize(QSize(16777215, 16777215))
        self.packets_to_send_scroll_container.setWidgetResizable(True)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, 0, 475, 584))
        self.verticalLayout_11 = QVBoxLayout(self.scroll_area_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.to_send_packets_list = QVBoxLayout()
        self.to_send_packets_list.setSpacing(10)
        self.to_send_packets_list.setObjectName(u"to_send_packets_list")
        self.to_send_packets_list.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_11.addLayout(self.to_send_packets_list)

        self.packets_to_send_scroll_container.setWidget(self.scroll_area_contents)

        self.right_side.addWidget(self.packets_to_send_scroll_container)

        self.right_side.setStretch(0, 1)
        self.right_side.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.right_side)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_packet_button = QPushButton(self.centralwidget)
        self.add_packet_button.setObjectName(u"add_packet_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_packet_button.sizePolicy().hasHeightForWidth())
        self.add_packet_button.setSizePolicy(sizePolicy1)
        self.add_packet_button.setMaximumSize(QSize(16777215, 100))
        self.add_packet_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.add_packet_button)

        self.send_packets_button = QPushButton(self.centralwidget)
        self.send_packets_button.setObjectName(u"send_packets_button")
        sizePolicy1.setHeightForWidth(self.send_packets_button.sizePolicy().hasHeightForWidth())
        self.send_packets_button.setSizePolicy(sizePolicy1)
        self.send_packets_button.setMaximumSize(QSize(16777215, 100))
        self.send_packets_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.send_packets_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 31))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"	background-color: rgb(100, 100, 100);\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.menuPacket_Generation = QMenu(self.menubar)
        self.menuPacket_Generation.setObjectName(u"menuPacket_Generation")
        self.menuPacket_Generation.setStyleSheet(u"")
        self.menuSend_Summary = QMenu(self.menubar)
        self.menuSend_Summary.setObjectName(u"menuSend_Summary")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuPacket_Generation.menuAction())
        self.menubar.addAction(self.menuSend_Summary.menuAction())

        self.retranslateUi(MainWindow)

        self.protocol_types_configuration_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.protocol_selection_title.setText(QCoreApplication.translate("MainWindow", u"Protocol Selection", None))
        self.protocol_label.setText(QCoreApplication.translate("MainWindow", u"Protocol Type", None))
        self.protocol_input.setItemText(0, QCoreApplication.translate("MainWindow", u"IP", None))
        self.protocol_input.setItemText(1, QCoreApplication.translate("MainWindow", u"ARP", None))
        self.protocol_input.setItemText(2, QCoreApplication.translate("MainWindow", u"DNS", None))

        self.protocol_selection_title_3.setText(QCoreApplication.translate("MainWindow", u"IP Packet Configuration", None))
        self.source_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Source IP Address", None))
        self.ip_payload_label.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.destination_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Destination IP Address", None))
        self.number_of_ip_packets_label.setText(QCoreApplication.translate("MainWindow", u"How many of this packet?", None))
        self.packets_to_send_title.setText(QCoreApplication.translate("MainWindow", u"Packets To Send", None))
        self.add_packet_button.setText(QCoreApplication.translate("MainWindow", u"Add Packets", None))
        self.send_packets_button.setText(QCoreApplication.translate("MainWindow", u"Send packets", None))
        self.menuPacket_Generation.setTitle(QCoreApplication.translate("MainWindow", u"Packet Generation", None))
        self.menuSend_Summary.setTitle(QCoreApplication.translate("MainWindow", u"Send Summary", None))
    # retranslateUi

