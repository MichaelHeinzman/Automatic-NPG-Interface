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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

from widgets.ip_4_address_input import IPAddressInput
from widgets.ip_packet_configuration import IPConfigurationWidget
from widgets.number_line_edit import NumberLineEdit
from widgets.protocol_selection import ProtocolSelection

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
"#ip_page, #arp_page, #dns_page {\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(54,60,75);\n"
"}\n"
"\n"
"\n"
"#scrollAreaWidgetContents {\n"
"	background-color: rgb(82, 88, 104);\n"
"}\n"
"\n"
"QLineEdit {\n"
"            position: absolute;\n"
"            padding: 10px;\n"
"            font-family: 'Inter';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 16px;\n"
"            line-height: 19px;\n"
"            text-align: center;\n"
"            color: #363C4B;\n"
"            background-color: rgba(217, 217, 217, 1);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

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

        self.protocol_input = ProtocolSelection(self.centralwidget)
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
        self.verticalLayout.setSpacing(0)
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

        self.scrollArea_3 = QScrollArea(self.ip_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(82, 88, 104, 1)\n"
"}\n"
"\n"
" QWidget #scrollAreaWidgetContents_6\n"
"{\n"
"	background-color: rgba(82, 88, 104, 1)\n"
"}\n"
"\n"
"QHBoxLayout {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 410, 580))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.source_ip_address_layout = QHBoxLayout()
        self.source_ip_address_layout.setObjectName(u"source_ip_address_layout")
        self.source_ip_address_label = QLabel(self.scrollAreaWidgetContents_6)
        self.source_ip_address_label.setObjectName(u"source_ip_address_label")
        self.source_ip_address_label.setMinimumSize(QSize(200, 50))
        self.source_ip_address_label.setMaximumSize(QSize(200, 50))
        font3 = QFont()
        font3.setPointSize(14)
        self.source_ip_address_label.setFont(font3)
        self.source_ip_address_label.setWordWrap(True)

        self.source_ip_address_layout.addWidget(self.source_ip_address_label)

        self.source_ip_address_input = IPAddressInput(self.scrollAreaWidgetContents_6)
        self.source_ip_address_input.setObjectName(u"source_ip_address_input")
        sizePolicy.setHeightForWidth(self.source_ip_address_input.sizePolicy().hasHeightForWidth())
        self.source_ip_address_input.setSizePolicy(sizePolicy)
        self.source_ip_address_input.setMinimumSize(QSize(0, 50))
        self.source_ip_address_input.setMaximumSize(QSize(250, 16777215))
        self.source_ip_address_input.setStyleSheet(u"")

        self.source_ip_address_layout.addWidget(self.source_ip_address_input)


        self.verticalLayout_9.addLayout(self.source_ip_address_layout)

        self.destination_ip_address_layout = QHBoxLayout()
        self.destination_ip_address_layout.setObjectName(u"destination_ip_address_layout")
        self.destination_ip_address_label = QLabel(self.scrollAreaWidgetContents_6)
        self.destination_ip_address_label.setObjectName(u"destination_ip_address_label")
        self.destination_ip_address_label.setMinimumSize(QSize(200, 50))
        self.destination_ip_address_label.setMaximumSize(QSize(200, 50))
        self.destination_ip_address_label.setFont(font3)
        self.destination_ip_address_label.setWordWrap(True)

        self.destination_ip_address_layout.addWidget(self.destination_ip_address_label)

        self.destination_ip_address_input = IPAddressInput(self.scrollAreaWidgetContents_6)
        self.destination_ip_address_input.setObjectName(u"destination_ip_address_input")
        sizePolicy.setHeightForWidth(self.destination_ip_address_input.sizePolicy().hasHeightForWidth())
        self.destination_ip_address_input.setSizePolicy(sizePolicy)
        self.destination_ip_address_input.setMinimumSize(QSize(0, 50))
        self.destination_ip_address_input.setMaximumSize(QSize(250, 16777215))
        self.destination_ip_address_input.setStyleSheet(u"")

        self.destination_ip_address_layout.addWidget(self.destination_ip_address_input)


        self.verticalLayout_9.addLayout(self.destination_ip_address_layout)

        self.time_to_live_ip_layout = QHBoxLayout()
        self.time_to_live_ip_layout.setObjectName(u"time_to_live_ip_layout")
        self.time_to_live_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.time_to_live_ip_label.setObjectName(u"time_to_live_ip_label")
        self.time_to_live_ip_label.setMinimumSize(QSize(200, 50))
        self.time_to_live_ip_label.setMaximumSize(QSize(200, 50))
        self.time_to_live_ip_label.setFont(font3)
        self.time_to_live_ip_label.setWordWrap(True)

        self.time_to_live_ip_layout.addWidget(self.time_to_live_ip_label)

        self.time_to_live_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.time_to_live_ip_input.setObjectName(u"time_to_live_ip_input")
        sizePolicy.setHeightForWidth(self.time_to_live_ip_input.sizePolicy().hasHeightForWidth())
        self.time_to_live_ip_input.setSizePolicy(sizePolicy)
        self.time_to_live_ip_input.setMinimumSize(QSize(0, 50))
        self.time_to_live_ip_input.setMaximumSize(QSize(250, 16777215))
        self.time_to_live_ip_input.setStyleSheet(u"")

        self.time_to_live_ip_layout.addWidget(self.time_to_live_ip_input)


        self.verticalLayout_9.addLayout(self.time_to_live_ip_layout)

        self.protocol_ip_layout = QHBoxLayout()
        self.protocol_ip_layout.setObjectName(u"protocol_ip_layout")
        self.protocol_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.protocol_ip_label.setObjectName(u"protocol_ip_label")
        self.protocol_ip_label.setMinimumSize(QSize(200, 50))
        self.protocol_ip_label.setMaximumSize(QSize(200, 50))
        self.protocol_ip_label.setFont(font3)
        self.protocol_ip_label.setWordWrap(True)

        self.protocol_ip_layout.addWidget(self.protocol_ip_label)

        self.protocol_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.protocol_ip_input.setObjectName(u"protocol_ip_input")
        sizePolicy.setHeightForWidth(self.protocol_ip_input.sizePolicy().hasHeightForWidth())
        self.protocol_ip_input.setSizePolicy(sizePolicy)
        self.protocol_ip_input.setMinimumSize(QSize(0, 50))
        self.protocol_ip_input.setMaximumSize(QSize(250, 16777215))
        self.protocol_ip_input.setStyleSheet(u"")

        self.protocol_ip_layout.addWidget(self.protocol_ip_input)


        self.verticalLayout_9.addLayout(self.protocol_ip_layout)

        self.flags_ip_layout = QHBoxLayout()
        self.flags_ip_layout.setObjectName(u"flags_ip_layout")
        self.flags_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.flags_ip_label.setObjectName(u"flags_ip_label")
        self.flags_ip_label.setMinimumSize(QSize(200, 50))
        self.flags_ip_label.setMaximumSize(QSize(200, 50))
        self.flags_ip_label.setFont(font3)
        self.flags_ip_label.setWordWrap(True)

        self.flags_ip_layout.addWidget(self.flags_ip_label)

        self.flags_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.flags_ip_input.setObjectName(u"flags_ip_input")
        sizePolicy.setHeightForWidth(self.flags_ip_input.sizePolicy().hasHeightForWidth())
        self.flags_ip_input.setSizePolicy(sizePolicy)
        self.flags_ip_input.setMinimumSize(QSize(0, 50))
        self.flags_ip_input.setMaximumSize(QSize(250, 16777215))
        self.flags_ip_input.setStyleSheet(u"")

        self.flags_ip_layout.addWidget(self.flags_ip_input)


        self.verticalLayout_9.addLayout(self.flags_ip_layout)

        self.fragmentation_offset_ip_layout = QHBoxLayout()
        self.fragmentation_offset_ip_layout.setObjectName(u"fragmentation_offset_ip_layout")
        self.fragmentation_offset_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.fragmentation_offset_ip_label.setObjectName(u"fragmentation_offset_ip_label")
        self.fragmentation_offset_ip_label.setMinimumSize(QSize(200, 50))
        self.fragmentation_offset_ip_label.setMaximumSize(QSize(200, 50))
        self.fragmentation_offset_ip_label.setFont(font3)
        self.fragmentation_offset_ip_label.setWordWrap(True)

        self.fragmentation_offset_ip_layout.addWidget(self.fragmentation_offset_ip_label)

        self.fragmentation_offset_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.fragmentation_offset_ip_input.setObjectName(u"fragmentation_offset_ip_input")
        sizePolicy.setHeightForWidth(self.fragmentation_offset_ip_input.sizePolicy().hasHeightForWidth())
        self.fragmentation_offset_ip_input.setSizePolicy(sizePolicy)
        self.fragmentation_offset_ip_input.setMinimumSize(QSize(0, 50))
        self.fragmentation_offset_ip_input.setMaximumSize(QSize(250, 16777215))
        self.fragmentation_offset_ip_input.setStyleSheet(u"")

        self.fragmentation_offset_ip_layout.addWidget(self.fragmentation_offset_ip_input)


        self.verticalLayout_9.addLayout(self.fragmentation_offset_ip_layout)

        self.identification_ip_layout = QHBoxLayout()
        self.identification_ip_layout.setObjectName(u"identification_ip_layout")
        self.identification_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.identification_ip_label.setObjectName(u"identification_ip_label")
        self.identification_ip_label.setMinimumSize(QSize(200, 50))
        self.identification_ip_label.setMaximumSize(QSize(200, 50))
        self.identification_ip_label.setFont(font3)
        self.identification_ip_label.setWordWrap(True)

        self.identification_ip_layout.addWidget(self.identification_ip_label)

        self.identification_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.identification_ip_input.setObjectName(u"identification_ip_input")
        sizePolicy.setHeightForWidth(self.identification_ip_input.sizePolicy().hasHeightForWidth())
        self.identification_ip_input.setSizePolicy(sizePolicy)
        self.identification_ip_input.setMinimumSize(QSize(0, 50))
        self.identification_ip_input.setMaximumSize(QSize(250, 16777215))
        self.identification_ip_input.setStyleSheet(u"")

        self.identification_ip_layout.addWidget(self.identification_ip_input)


        self.verticalLayout_9.addLayout(self.identification_ip_layout)

        self.ip_payload_layout = QHBoxLayout()
        self.ip_payload_layout.setObjectName(u"ip_payload_layout")
        self.ip_payload_label = QLabel(self.scrollAreaWidgetContents_6)
        self.ip_payload_label.setObjectName(u"ip_payload_label")
        self.ip_payload_label.setMinimumSize(QSize(200, 50))
        self.ip_payload_label.setMaximumSize(QSize(200, 50))
        self.ip_payload_label.setFont(font3)
        self.ip_payload_label.setWordWrap(True)

        self.ip_payload_layout.addWidget(self.ip_payload_label)

        self.ip_payload_input = QLineEdit(self.scrollAreaWidgetContents_6)
        self.ip_payload_input.setObjectName(u"ip_payload_input")
        sizePolicy.setHeightForWidth(self.ip_payload_input.sizePolicy().hasHeightForWidth())
        self.ip_payload_input.setSizePolicy(sizePolicy)
        self.ip_payload_input.setMinimumSize(QSize(0, 50))
        self.ip_payload_input.setMaximumSize(QSize(250, 16777215))
        self.ip_payload_input.setStyleSheet(u"")

        self.ip_payload_layout.addWidget(self.ip_payload_input)


        self.verticalLayout_9.addLayout(self.ip_payload_layout)

        self.number_ip_layout = QHBoxLayout()
        self.number_ip_layout.setObjectName(u"number_ip_layout")
        self.number_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.number_ip_label.setObjectName(u"number_ip_label")
        self.number_ip_label.setMinimumSize(QSize(200, 50))
        self.number_ip_label.setMaximumSize(QSize(200, 50))
        self.number_ip_label.setFont(font3)
        self.number_ip_label.setWordWrap(True)

        self.number_ip_layout.addWidget(self.number_ip_label)

        self.number_ip_input = NumberLineEdit(self.scrollAreaWidgetContents_6)
        self.number_ip_input.setObjectName(u"number_ip_input")
        sizePolicy.setHeightForWidth(self.number_ip_input.sizePolicy().hasHeightForWidth())
        self.number_ip_input.setSizePolicy(sizePolicy)
        self.number_ip_input.setMinimumSize(QSize(0, 50))
        self.number_ip_input.setMaximumSize(QSize(250, 16777215))
        self.number_ip_input.setStyleSheet(u"")

        self.number_ip_layout.addWidget(self.number_ip_input)


        self.verticalLayout_9.addLayout(self.number_ip_layout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout.addWidget(self.scrollArea_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.protocol_types_configuration_pages.addWidget(self.ip_page)
        self.arp_page = QWidget()
        self.arp_page.setObjectName(u"arp_page")
        self.verticalLayout_3 = QVBoxLayout(self.arp_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.source_mac_address_arp_10 = QLabel(self.arp_page)
        self.source_mac_address_arp_10.setObjectName(u"source_mac_address_arp_10")
        self.source_mac_address_arp_10.setFont(font3)

        self.verticalLayout_3.addWidget(self.source_mac_address_arp_10)

        self.source_mac_address_arp_layout_10 = QHBoxLayout()
        self.source_mac_address_arp_layout_10.setObjectName(u"source_mac_address_arp_layout_10")
        self.scrollArea = QScrollArea(self.arp_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"\n"
"QScrollArea {\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
" QWidget #scrollAreaWidgetContents_4{\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
"QHBoxLayout {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 408, 522))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.source_mac_address_arp_layout_8 = QHBoxLayout()
        self.source_mac_address_arp_layout_8.setObjectName(u"source_mac_address_arp_layout_8")
        self.source_mac_address_arp_8 = QLabel(self.scrollAreaWidgetContents_4)
        self.source_mac_address_arp_8.setObjectName(u"source_mac_address_arp_8")
        self.source_mac_address_arp_8.setMinimumSize(QSize(200, 50))
        self.source_mac_address_arp_8.setMaximumSize(QSize(50, 16777215))
        self.source_mac_address_arp_8.setFont(font3)
        self.source_mac_address_arp_8.setWordWrap(True)

        self.source_mac_address_arp_layout_8.addWidget(self.source_mac_address_arp_8)

        self.source_mac_address_arp_input_8 = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.source_mac_address_arp_input_8.setObjectName(u"source_mac_address_arp_input_8")
        sizePolicy.setHeightForWidth(self.source_mac_address_arp_input_8.sizePolicy().hasHeightForWidth())
        self.source_mac_address_arp_input_8.setSizePolicy(sizePolicy)
        self.source_mac_address_arp_input_8.setMinimumSize(QSize(0, 50))
        self.source_mac_address_arp_input_8.setMaximumSize(QSize(250, 16777215))

        self.source_mac_address_arp_layout_8.addWidget(self.source_mac_address_arp_input_8)


        self.verticalLayout_6.addLayout(self.source_mac_address_arp_layout_8)

        self.hardware_address_type_arp_layout = QHBoxLayout()
        self.hardware_address_type_arp_layout.setObjectName(u"hardware_address_type_arp_layout")
        self.hardware_address_type_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.hardware_address_type_arp_label.setObjectName(u"hardware_address_type_arp_label")
        self.hardware_address_type_arp_label.setMinimumSize(QSize(200, 50))
        self.hardware_address_type_arp_label.setMaximumSize(QSize(50, 16777215))
        self.hardware_address_type_arp_label.setFont(font3)
        self.hardware_address_type_arp_label.setWordWrap(True)

        self.hardware_address_type_arp_layout.addWidget(self.hardware_address_type_arp_label)

        self.hardware_address_type_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.hardware_address_type_arp_input.setObjectName(u"hardware_address_type_arp_input")
        sizePolicy.setHeightForWidth(self.hardware_address_type_arp_input.sizePolicy().hasHeightForWidth())
        self.hardware_address_type_arp_input.setSizePolicy(sizePolicy)
        self.hardware_address_type_arp_input.setMinimumSize(QSize(0, 50))
        self.hardware_address_type_arp_input.setMaximumSize(QSize(250, 50))

        self.hardware_address_type_arp_layout.addWidget(self.hardware_address_type_arp_input)


        self.verticalLayout_6.addLayout(self.hardware_address_type_arp_layout)

        self.hardware_address_length_arp_layout = QHBoxLayout()
        self.hardware_address_length_arp_layout.setObjectName(u"hardware_address_length_arp_layout")
        self.hardware_address_length_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.hardware_address_length_arp_label.setObjectName(u"hardware_address_length_arp_label")
        self.hardware_address_length_arp_label.setMinimumSize(QSize(200, 50))
        self.hardware_address_length_arp_label.setMaximumSize(QSize(50, 16777215))
        self.hardware_address_length_arp_label.setFont(font3)
        self.hardware_address_length_arp_label.setWordWrap(True)

        self.hardware_address_length_arp_layout.addWidget(self.hardware_address_length_arp_label)

        self.hardware_address_length_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.hardware_address_length_arp_input.setObjectName(u"hardware_address_length_arp_input")
        sizePolicy.setHeightForWidth(self.hardware_address_length_arp_input.sizePolicy().hasHeightForWidth())
        self.hardware_address_length_arp_input.setSizePolicy(sizePolicy)
        self.hardware_address_length_arp_input.setMinimumSize(QSize(0, 50))
        self.hardware_address_length_arp_input.setMaximumSize(QSize(250, 50))

        self.hardware_address_length_arp_layout.addWidget(self.hardware_address_length_arp_input)


        self.verticalLayout_6.addLayout(self.hardware_address_length_arp_layout)

        self.protocol_address_type_arp_layout = QHBoxLayout()
        self.protocol_address_type_arp_layout.setObjectName(u"protocol_address_type_arp_layout")
        self.protocol_address_type_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.protocol_address_type_arp_label.setObjectName(u"protocol_address_type_arp_label")
        self.protocol_address_type_arp_label.setMinimumSize(QSize(200, 50))
        self.protocol_address_type_arp_label.setMaximumSize(QSize(50, 16777215))
        self.protocol_address_type_arp_label.setFont(font3)
        self.protocol_address_type_arp_label.setWordWrap(True)

        self.protocol_address_type_arp_layout.addWidget(self.protocol_address_type_arp_label)

        self.protocol_address_type_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.protocol_address_type_arp_input.setObjectName(u"protocol_address_type_arp_input")
        sizePolicy.setHeightForWidth(self.protocol_address_type_arp_input.sizePolicy().hasHeightForWidth())
        self.protocol_address_type_arp_input.setSizePolicy(sizePolicy)
        self.protocol_address_type_arp_input.setMinimumSize(QSize(0, 50))
        self.protocol_address_type_arp_input.setMaximumSize(QSize(250, 50))

        self.protocol_address_type_arp_layout.addWidget(self.protocol_address_type_arp_input)


        self.verticalLayout_6.addLayout(self.protocol_address_type_arp_layout)

        self.protocol_address_length_arp_layout = QHBoxLayout()
        self.protocol_address_length_arp_layout.setObjectName(u"protocol_address_length_arp_layout")
        self.protocol_address_length_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.protocol_address_length_arp_label.setObjectName(u"protocol_address_length_arp_label")
        self.protocol_address_length_arp_label.setMinimumSize(QSize(200, 50))
        self.protocol_address_length_arp_label.setMaximumSize(QSize(50, 16777215))
        self.protocol_address_length_arp_label.setFont(font3)
        self.protocol_address_length_arp_label.setWordWrap(True)

        self.protocol_address_length_arp_layout.addWidget(self.protocol_address_length_arp_label)

        self.protocol_address_length_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.protocol_address_length_arp_input.setObjectName(u"protocol_address_length_arp_input")
        sizePolicy.setHeightForWidth(self.protocol_address_length_arp_input.sizePolicy().hasHeightForWidth())
        self.protocol_address_length_arp_input.setSizePolicy(sizePolicy)
        self.protocol_address_length_arp_input.setMinimumSize(QSize(0, 50))
        self.protocol_address_length_arp_input.setMaximumSize(QSize(250, 50))

        self.protocol_address_length_arp_layout.addWidget(self.protocol_address_length_arp_input)


        self.verticalLayout_6.addLayout(self.protocol_address_length_arp_layout)

        self.destination_mac_address_arp_layout = QHBoxLayout()
        self.destination_mac_address_arp_layout.setObjectName(u"destination_mac_address_arp_layout")
        self.destination_mac_address_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.destination_mac_address_arp_label.setObjectName(u"destination_mac_address_arp_label")
        self.destination_mac_address_arp_label.setMinimumSize(QSize(200, 50))
        self.destination_mac_address_arp_label.setMaximumSize(QSize(50, 16777215))
        self.destination_mac_address_arp_label.setFont(font3)
        self.destination_mac_address_arp_label.setWordWrap(True)

        self.destination_mac_address_arp_layout.addWidget(self.destination_mac_address_arp_label)

        self.destination_mac_address_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.destination_mac_address_arp_input.setObjectName(u"destination_mac_address_arp_input")
        sizePolicy.setHeightForWidth(self.destination_mac_address_arp_input.sizePolicy().hasHeightForWidth())
        self.destination_mac_address_arp_input.setSizePolicy(sizePolicy)
        self.destination_mac_address_arp_input.setMinimumSize(QSize(0, 50))
        self.destination_mac_address_arp_input.setMaximumSize(QSize(250, 50))

        self.destination_mac_address_arp_layout.addWidget(self.destination_mac_address_arp_input)


        self.verticalLayout_6.addLayout(self.destination_mac_address_arp_layout)

        self.operation_code_arp_layout = QHBoxLayout()
        self.operation_code_arp_layout.setObjectName(u"operation_code_arp_layout")
        self.operation_code_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.operation_code_arp_label.setObjectName(u"operation_code_arp_label")
        self.operation_code_arp_label.setMinimumSize(QSize(200, 50))
        self.operation_code_arp_label.setMaximumSize(QSize(50, 16777215))
        self.operation_code_arp_label.setFont(font3)
        self.operation_code_arp_label.setWordWrap(True)

        self.operation_code_arp_layout.addWidget(self.operation_code_arp_label)

        self.operation_code_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.operation_code_arp_input.setObjectName(u"operation_code_arp_input")
        sizePolicy.setHeightForWidth(self.operation_code_arp_input.sizePolicy().hasHeightForWidth())
        self.operation_code_arp_input.setSizePolicy(sizePolicy)
        self.operation_code_arp_input.setMinimumSize(QSize(0, 50))
        self.operation_code_arp_input.setMaximumSize(QSize(250, 50))

        self.operation_code_arp_layout.addWidget(self.operation_code_arp_input)


        self.verticalLayout_6.addLayout(self.operation_code_arp_layout)

        self.number_arp_layout = QHBoxLayout()
        self.number_arp_layout.setObjectName(u"number_arp_layout")
        self.number_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.number_arp_label.setObjectName(u"number_arp_label")
        self.number_arp_label.setMinimumSize(QSize(200, 50))
        self.number_arp_label.setMaximumSize(QSize(50, 16777215))
        self.number_arp_label.setFont(font3)
        self.number_arp_label.setWordWrap(True)

        self.number_arp_layout.addWidget(self.number_arp_label)

        self.number_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.number_arp_input.setObjectName(u"number_arp_input")
        sizePolicy.setHeightForWidth(self.number_arp_input.sizePolicy().hasHeightForWidth())
        self.number_arp_input.setSizePolicy(sizePolicy)
        self.number_arp_input.setMinimumSize(QSize(0, 50))
        self.number_arp_input.setMaximumSize(QSize(250, 50))

        self.number_arp_layout.addWidget(self.number_arp_input)


        self.verticalLayout_6.addLayout(self.number_arp_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.source_mac_address_arp_layout_10.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.source_mac_address_arp_layout_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 12)
        self.protocol_types_configuration_pages.addWidget(self.arp_page)
        self.dns_page = QWidget()
        self.dns_page.setObjectName(u"dns_page")
        self.dns_page.setToolTipDuration(12)
        self.dns_page.setAutoFillBackground(False)
        self.dns_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.dns_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.source_mac_address_arp_13 = QLabel(self.dns_page)
        self.source_mac_address_arp_13.setObjectName(u"source_mac_address_arp_13")
        self.source_mac_address_arp_13.setFont(font3)

        self.verticalLayout_8.addWidget(self.source_mac_address_arp_13)

        self.scrollArea_2 = QScrollArea(self.dns_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setAutoFillBackground(True)
        self.scrollArea_2.setStyleSheet(u"\n"
"\n"
"QScrollArea {\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
" QWidget #scrollAreaWidgetContents_5{\n"
"	background-color: rgb(54, 60, 75);\n"
"}\n"
"\n"
"QHBoxLayout {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 427, 518))
        self.scrollAreaWidgetContents_5.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_5.setStyleSheet(u"QHBoxLayout {\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.source_mac_address_arp_layout_13 = QHBoxLayout()
        self.source_mac_address_arp_layout_13.setObjectName(u"source_mac_address_arp_layout_13")
        self.source_mac_address_arp_14 = QLabel(self.scrollAreaWidgetContents_5)
        self.source_mac_address_arp_14.setObjectName(u"source_mac_address_arp_14")
        self.source_mac_address_arp_14.setMaximumSize(QSize(200, 16777215))
        self.source_mac_address_arp_14.setFont(font3)
        self.source_mac_address_arp_14.setWordWrap(True)

        self.source_mac_address_arp_layout_13.addWidget(self.source_mac_address_arp_14)

        self.source_mac_address_arp_input_10 = IPAddressInput(self.scrollAreaWidgetContents_5)
        self.source_mac_address_arp_input_10.setObjectName(u"source_mac_address_arp_input_10")
        sizePolicy.setHeightForWidth(self.source_mac_address_arp_input_10.sizePolicy().hasHeightForWidth())
        self.source_mac_address_arp_input_10.setSizePolicy(sizePolicy)
        self.source_mac_address_arp_input_10.setMinimumSize(QSize(0, 50))
        self.source_mac_address_arp_input_10.setMaximumSize(QSize(250, 16777215))

        self.source_mac_address_arp_layout_13.addWidget(self.source_mac_address_arp_input_10)


        self.verticalLayout_7.addLayout(self.source_mac_address_arp_layout_13)

        self.source_mac_address_arp_layout_6 = QHBoxLayout()
        self.source_mac_address_arp_layout_6.setObjectName(u"source_mac_address_arp_layout_6")
        self.source_mac_address_arp_6 = QLabel(self.scrollAreaWidgetContents_5)
        self.source_mac_address_arp_6.setObjectName(u"source_mac_address_arp_6")
        self.source_mac_address_arp_6.setMaximumSize(QSize(200, 16777215))
        self.source_mac_address_arp_6.setFont(font3)
        self.source_mac_address_arp_6.setWordWrap(True)

        self.source_mac_address_arp_layout_6.addWidget(self.source_mac_address_arp_6)

        self.source_mac_address_arp_input_6 = IPAddressInput(self.scrollAreaWidgetContents_5)
        self.source_mac_address_arp_input_6.setObjectName(u"source_mac_address_arp_input_6")
        sizePolicy.setHeightForWidth(self.source_mac_address_arp_input_6.sizePolicy().hasHeightForWidth())
        self.source_mac_address_arp_input_6.setSizePolicy(sizePolicy)
        self.source_mac_address_arp_input_6.setMinimumSize(QSize(0, 50))
        self.source_mac_address_arp_input_6.setMaximumSize(QSize(250, 16777215))

        self.source_mac_address_arp_layout_6.addWidget(self.source_mac_address_arp_input_6)


        self.verticalLayout_7.addLayout(self.source_mac_address_arp_layout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 12)
        self.protocol_types_configuration_pages.addWidget(self.dns_page)

        self.protocol_details_container.addWidget(self.protocol_types_configuration_pages)


        self.left_side.addLayout(self.protocol_details_container)

        self.left_side.setStretch(0, 1)
        self.left_side.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.left_side)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

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
        self.packets_to_send_scroll_container.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, 0, 429, 625))
        self.scroll_area_contents.setStyleSheet(u"background-color: rgba(82, 88, 104, 1)")
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
        self.right_side.setStretch(1, 11)

        self.horizontalLayout_2.addLayout(self.right_side)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(3, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

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

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.send_packets_button = QPushButton(self.centralwidget)
        self.send_packets_button.setObjectName(u"send_packets_button")
        sizePolicy1.setHeightForWidth(self.send_packets_button.sizePolicy().hasHeightForWidth())
        self.send_packets_button.setSizePolicy(sizePolicy1)
        self.send_packets_button.setMaximumSize(QSize(16777215, 100))
        self.send_packets_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.send_packets_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)

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
        self.source_ip_address_input.setText("")
        self.destination_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Destination IP Address", None))
        self.time_to_live_ip_label.setText(QCoreApplication.translate("MainWindow", u"Time To Live", None))
        self.protocol_ip_label.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        self.flags_ip_label.setText(QCoreApplication.translate("MainWindow", u"Flags", None))
        self.fragmentation_offset_ip_label.setText(QCoreApplication.translate("MainWindow", u"Fragmentation Offset", None))
        self.identification_ip_label.setText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.ip_payload_label.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.number_ip_label.setText(QCoreApplication.translate("MainWindow", u"How many of this packet?", None))
        self.number_ip_input.setInputMask("")
        self.source_mac_address_arp_10.setText(QCoreApplication.translate("MainWindow", u"ARP Configuration", None))
        self.source_mac_address_arp_8.setText(QCoreApplication.translate("MainWindow", u"Source MAC Address", None))
        self.hardware_address_type_arp_label.setText(QCoreApplication.translate("MainWindow", u"Hardware Address Type", None))
        self.hardware_address_length_arp_label.setText(QCoreApplication.translate("MainWindow", u"Hardware Address Length", None))
        self.protocol_address_type_arp_label.setText(QCoreApplication.translate("MainWindow", u"Protocol Address Type", None))
        self.protocol_address_length_arp_label.setText(QCoreApplication.translate("MainWindow", u"Protocol Address Length", None))
        self.destination_mac_address_arp_label.setText(QCoreApplication.translate("MainWindow", u"Destination MAC Address", None))
        self.operation_code_arp_label.setText(QCoreApplication.translate("MainWindow", u"Operation Code", None))
        self.number_arp_label.setText(QCoreApplication.translate("MainWindow", u"How many packets?", None))
        self.source_mac_address_arp_13.setText(QCoreApplication.translate("MainWindow", u"DNS Configuration", None))
        self.source_mac_address_arp_14.setText(QCoreApplication.translate("MainWindow", u"Source MAC Address", None))
        self.source_mac_address_arp_6.setText(QCoreApplication.translate("MainWindow", u"Hardware Address Type", None))
        self.packets_to_send_title.setText(QCoreApplication.translate("MainWindow", u"Packets To Send", None))
        self.add_packet_button.setText(QCoreApplication.translate("MainWindow", u"Add Packets", None))
        self.send_packets_button.setText(QCoreApplication.translate("MainWindow", u"Send packets", None))
        self.menuPacket_Generation.setTitle(QCoreApplication.translate("MainWindow", u"Packet Generation", None))
        self.menuSend_Summary.setTitle(QCoreApplication.translate("MainWindow", u"Send Summary", None))
    # retranslateUi

