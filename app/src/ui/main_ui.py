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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from widgets.arp_configuration import ARPConfigurationWidget
from widgets.console_output import ConsoleOutput
from widgets.dns_configuration import DNSConfigurationWidget
from widgets.ip_4_address_input import IPAddressInput
from widgets.ip_packet_configuration import IPConfigurationWidget
from widgets.number_line_edit import NumberLineEdit
from widgets.protocol_selection import ProtocolSelection

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 880)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
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
"QLineEdit, QRadioButton {\n"
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
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"#tabWidget {\n"
"	background:transparent;\n"
"}\n"
"\n"
"QTabWidget::pane { border: 0; }")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.CreatingAndSending = QWidget()
        self.CreatingAndSending.setObjectName(u"CreatingAndSending")
        self.verticalLayout_7 = QVBoxLayout(self.CreatingAndSending)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.left_side = QVBoxLayout()
        self.left_side.setObjectName(u"left_side")
        self.left_side.setContentsMargins(-1, -1, -1, 0)
        self.protocol_selection_container = QVBoxLayout()
        self.protocol_selection_container.setObjectName(u"protocol_selection_container")
        self.protocol_selection_title = QLabel(self.CreatingAndSending)
        self.protocol_selection_title.setObjectName(u"protocol_selection_title")
        font1 = QFont()
        font1.setPointSize(24)
        self.protocol_selection_title.setFont(font1)

        self.protocol_selection_container.addWidget(self.protocol_selection_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.protocol_label = QLabel(self.CreatingAndSending)
        self.protocol_label.setObjectName(u"protocol_label")

        self.horizontalLayout.addWidget(self.protocol_label)

        self.protocol_input = ProtocolSelection(self.CreatingAndSending)
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
        self.protocol_types_configuration_pages = QStackedWidget(self.CreatingAndSending)
        self.protocol_types_configuration_pages.setObjectName(u"protocol_types_configuration_pages")
        self.ip_page = IPConfigurationWidget()
        self.ip_page.setObjectName(u"ip_page")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(20)
        self.ip_page.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.ip_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.protocol_selection_title_3 = QLabel(self.ip_page)
        self.protocol_selection_title_3.setObjectName(u"protocol_selection_title_3")
        sizePolicy.setHeightForWidth(self.protocol_selection_title_3.sizePolicy().hasHeightForWidth())
        self.protocol_selection_title_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(20)
        self.protocol_selection_title_3.setFont(font3)

        self.verticalLayout.addWidget(self.protocol_selection_title_3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

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
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 401, 634))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.ip_types_radios = QHBoxLayout()
        self.ip_types_radios.setSpacing(0)
        self.ip_types_radios.setObjectName(u"ip_types_radios")
        self.ip_types_radios.setContentsMargins(-1, 0, -1, -1)
        self.icmp_radio = QRadioButton(self.scrollAreaWidgetContents_6)
        self.icmp_radio.setObjectName(u"icmp_radio")

        self.ip_types_radios.addWidget(self.icmp_radio)

        self.tcp_radio = QRadioButton(self.scrollAreaWidgetContents_6)
        self.tcp_radio.setObjectName(u"tcp_radio")
        self.tcp_radio.setChecked(True)

        self.ip_types_radios.addWidget(self.tcp_radio)

        self.udp_radio = QRadioButton(self.scrollAreaWidgetContents_6)
        self.udp_radio.setObjectName(u"udp_radio")

        self.ip_types_radios.addWidget(self.udp_radio)


        self.verticalLayout_9.addLayout(self.ip_types_radios)

        self.ip_types_stacked_widget = QStackedWidget(self.scrollAreaWidgetContents_6)
        self.ip_types_stacked_widget.setObjectName(u"ip_types_stacked_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ip_types_stacked_widget.sizePolicy().hasHeightForWidth())
        self.ip_types_stacked_widget.setSizePolicy(sizePolicy1)
        self.ip_types_stacked_widget.setStyleSheet(u"\n"
"#ip_types_stacked_widget {	\n"
"background-color: rgba(82, 88, 104, 1);\n"
"}")
        self.tcp = QWidget()
        self.tcp.setObjectName(u"tcp")
        self.tcp.setAutoFillBackground(False)
        self.tcp.setStyleSheet(u"#tcp{	\n"
"background-color: rgba(82, 88, 104, 1);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.tcp)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tcp_types_grid = QGridLayout()
        self.tcp_types_grid.setSpacing(0)
        self.tcp_types_grid.setObjectName(u"tcp_types_grid")
        self.tcp_types_grid.setContentsMargins(-1, -1, -1, 0)
        self.tcp_syn_radio = QRadioButton(self.tcp)
        self.tcp_syn_radio.setObjectName(u"tcp_syn_radio")

        self.tcp_types_grid.addWidget(self.tcp_syn_radio, 0, 0, 1, 1)

        self.tcp_fin_radio = QRadioButton(self.tcp)
        self.tcp_fin_radio.setObjectName(u"tcp_fin_radio")

        self.tcp_types_grid.addWidget(self.tcp_fin_radio, 3, 0, 1, 1)

        self.tcp_finack_radio = QRadioButton(self.tcp)
        self.tcp_finack_radio.setObjectName(u"tcp_finack_radio")

        self.tcp_types_grid.addWidget(self.tcp_finack_radio, 3, 1, 1, 1)

        self.tcp_rst_radio = QRadioButton(self.tcp)
        self.tcp_rst_radio.setObjectName(u"tcp_rst_radio")

        self.tcp_types_grid.addWidget(self.tcp_rst_radio, 2, 1, 1, 1)

        self.tcp_synack_radio = QRadioButton(self.tcp)
        self.tcp_synack_radio.setObjectName(u"tcp_synack_radio")

        self.tcp_types_grid.addWidget(self.tcp_synack_radio, 0, 1, 1, 1)

        self.tcp_psh_radio = QRadioButton(self.tcp)
        self.tcp_psh_radio.setObjectName(u"tcp_psh_radio")

        self.tcp_types_grid.addWidget(self.tcp_psh_radio, 2, 0, 1, 1)

        self.tcp_ack_radio = QRadioButton(self.tcp)
        self.tcp_ack_radio.setObjectName(u"tcp_ack_radio")

        self.tcp_types_grid.addWidget(self.tcp_ack_radio, 0, 4, 1, 1)

        self.tcp_urg_radio = QRadioButton(self.tcp)
        self.tcp_urg_radio.setObjectName(u"tcp_urg_radio")

        self.tcp_types_grid.addWidget(self.tcp_urg_radio, 2, 4, 1, 1)


        self.verticalLayout_5.addLayout(self.tcp_types_grid)

        self.tcp_source_port = QHBoxLayout()
        self.tcp_source_port.setSpacing(6)
        self.tcp_source_port.setObjectName(u"tcp_source_port")
        self.tcp_source_port_label = QLabel(self.tcp)
        self.tcp_source_port_label.setObjectName(u"tcp_source_port_label")
        self.tcp_source_port_label.setMinimumSize(QSize(200, 50))
        self.tcp_source_port_label.setMaximumSize(QSize(200, 50))
        font4 = QFont()
        font4.setPointSize(14)
        self.tcp_source_port_label.setFont(font4)
        self.tcp_source_port_label.setWordWrap(True)

        self.tcp_source_port.addWidget(self.tcp_source_port_label)

        self.tcp_source_port_input = QLineEdit(self.tcp)
        self.tcp_source_port_input.setObjectName(u"tcp_source_port_input")
        sizePolicy.setHeightForWidth(self.tcp_source_port_input.sizePolicy().hasHeightForWidth())
        self.tcp_source_port_input.setSizePolicy(sizePolicy)
        self.tcp_source_port_input.setMinimumSize(QSize(0, 50))
        self.tcp_source_port_input.setMaximumSize(QSize(250, 50))
        self.tcp_source_port_input.setStyleSheet(u"")

        self.tcp_source_port.addWidget(self.tcp_source_port_input)


        self.verticalLayout_5.addLayout(self.tcp_source_port)

        self.tcp_destination_port = QHBoxLayout()
        self.tcp_destination_port.setSpacing(6)
        self.tcp_destination_port.setObjectName(u"tcp_destination_port")
        self.tcp_destination_port.setContentsMargins(-1, 0, -1, -1)
        self.tcp_destination_port_label = QLabel(self.tcp)
        self.tcp_destination_port_label.setObjectName(u"tcp_destination_port_label")
        self.tcp_destination_port_label.setMinimumSize(QSize(200, 50))
        self.tcp_destination_port_label.setMaximumSize(QSize(200, 50))
        self.tcp_destination_port_label.setFont(font4)
        self.tcp_destination_port_label.setWordWrap(True)

        self.tcp_destination_port.addWidget(self.tcp_destination_port_label)

        self.tcp_destination_port_input = QLineEdit(self.tcp)
        self.tcp_destination_port_input.setObjectName(u"tcp_destination_port_input")
        sizePolicy.setHeightForWidth(self.tcp_destination_port_input.sizePolicy().hasHeightForWidth())
        self.tcp_destination_port_input.setSizePolicy(sizePolicy)
        self.tcp_destination_port_input.setMinimumSize(QSize(0, 50))
        self.tcp_destination_port_input.setMaximumSize(QSize(250, 50))
        self.tcp_destination_port_input.setStyleSheet(u"")

        self.tcp_destination_port.addWidget(self.tcp_destination_port_input)


        self.verticalLayout_5.addLayout(self.tcp_destination_port)

        self.ip_types_stacked_widget.addWidget(self.tcp)
        self.udp = QWidget()
        self.udp.setObjectName(u"udp")
        sizePolicy.setHeightForWidth(self.udp.sizePolicy().hasHeightForWidth())
        self.udp.setSizePolicy(sizePolicy)
        self.udp.setMinimumSize(QSize(0, 200))
        self.udp.setMaximumSize(QSize(16777215, 400))
        self.udp.setStyleSheet(u"#udp {\n"
"	background-color: rgba(82, 88, 104, 1);\n"
"\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.udp)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.udp_destination_port = QHBoxLayout()
        self.udp_destination_port.setSpacing(6)
        self.udp_destination_port.setObjectName(u"udp_destination_port")
        self.udp_destination_port.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.udp_destination_port_label = QLabel(self.udp)
        self.udp_destination_port_label.setObjectName(u"udp_destination_port_label")
        self.udp_destination_port_label.setMinimumSize(QSize(200, 50))
        self.udp_destination_port_label.setMaximumSize(QSize(200, 50))
        self.udp_destination_port_label.setFont(font4)
        self.udp_destination_port_label.setWordWrap(True)

        self.udp_destination_port.addWidget(self.udp_destination_port_label)

        self.udp_destination_port_input = QLineEdit(self.udp)
        self.udp_destination_port_input.setObjectName(u"udp_destination_port_input")
        sizePolicy1.setHeightForWidth(self.udp_destination_port_input.sizePolicy().hasHeightForWidth())
        self.udp_destination_port_input.setSizePolicy(sizePolicy1)
        self.udp_destination_port_input.setMinimumSize(QSize(0, 50))
        self.udp_destination_port_input.setMaximumSize(QSize(250, 50))
        self.udp_destination_port_input.setStyleSheet(u"")

        self.udp_destination_port.addWidget(self.udp_destination_port_input)


        self.verticalLayout_10.addLayout(self.udp_destination_port)

        self.udp_source_port = QHBoxLayout()
        self.udp_source_port.setSpacing(6)
        self.udp_source_port.setObjectName(u"udp_source_port")
        self.udp_source_port.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.udp_source_port_label = QLabel(self.udp)
        self.udp_source_port_label.setObjectName(u"udp_source_port_label")
        self.udp_source_port_label.setMinimumSize(QSize(200, 50))
        self.udp_source_port_label.setMaximumSize(QSize(200, 50))
        self.udp_source_port_label.setFont(font4)
        self.udp_source_port_label.setWordWrap(True)

        self.udp_source_port.addWidget(self.udp_source_port_label)

        self.udp_source_port_input = QLineEdit(self.udp)
        self.udp_source_port_input.setObjectName(u"udp_source_port_input")
        sizePolicy.setHeightForWidth(self.udp_source_port_input.sizePolicy().hasHeightForWidth())
        self.udp_source_port_input.setSizePolicy(sizePolicy)
        self.udp_source_port_input.setMinimumSize(QSize(0, 50))
        self.udp_source_port_input.setMaximumSize(QSize(250, 50))
        self.udp_source_port_input.setStyleSheet(u"")

        self.udp_source_port.addWidget(self.udp_source_port_input)


        self.verticalLayout_10.addLayout(self.udp_source_port)

        self.ip_types_stacked_widget.addWidget(self.udp)
        self.icmp = QWidget()
        self.icmp.setObjectName(u"icmp")
        self.ip_types_stacked_widget.addWidget(self.icmp)

        self.verticalLayout_9.addWidget(self.ip_types_stacked_widget)

        self.source_ip_address_layout = QHBoxLayout()
        self.source_ip_address_layout.setObjectName(u"source_ip_address_layout")
        self.source_ip_address_label = QLabel(self.scrollAreaWidgetContents_6)
        self.source_ip_address_label.setObjectName(u"source_ip_address_label")
        self.source_ip_address_label.setMinimumSize(QSize(200, 50))
        self.source_ip_address_label.setMaximumSize(QSize(200, 50))
        self.source_ip_address_label.setFont(font4)
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
        self.destination_ip_address_label.setFont(font4)
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
        self.time_to_live_ip_label.setFont(font4)
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

        self.ip_payload_layout = QHBoxLayout()
        self.ip_payload_layout.setSpacing(6)
        self.ip_payload_layout.setObjectName(u"ip_payload_layout")
        self.ip_payload_label = QLabel(self.scrollAreaWidgetContents_6)
        self.ip_payload_label.setObjectName(u"ip_payload_label")
        self.ip_payload_label.setMinimumSize(QSize(200, 50))
        self.ip_payload_label.setMaximumSize(QSize(200, 50))
        self.ip_payload_label.setFont(font4)
        self.ip_payload_label.setWordWrap(True)

        self.ip_payload_layout.addWidget(self.ip_payload_label)

        self.ip_payload_input = QLineEdit(self.scrollAreaWidgetContents_6)
        self.ip_payload_input.setObjectName(u"ip_payload_input")
        sizePolicy.setHeightForWidth(self.ip_payload_input.sizePolicy().hasHeightForWidth())
        self.ip_payload_input.setSizePolicy(sizePolicy)
        self.ip_payload_input.setMinimumSize(QSize(0, 50))
        self.ip_payload_input.setMaximumSize(QSize(250, 50))
        self.ip_payload_input.setStyleSheet(u"")

        self.ip_payload_layout.addWidget(self.ip_payload_input)


        self.verticalLayout_9.addLayout(self.ip_payload_layout)

        self.number_ip_layout = QHBoxLayout()
        self.number_ip_layout.setObjectName(u"number_ip_layout")
        self.number_ip_label = QLabel(self.scrollAreaWidgetContents_6)
        self.number_ip_label.setObjectName(u"number_ip_label")
        self.number_ip_label.setMinimumSize(QSize(200, 50))
        self.number_ip_label.setMaximumSize(QSize(200, 50))
        self.number_ip_label.setFont(font4)
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
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 18)
        self.protocol_types_configuration_pages.addWidget(self.ip_page)
        self.arp_page = ARPConfigurationWidget()
        self.arp_page.setObjectName(u"arp_page")
        self.verticalLayout_3 = QVBoxLayout(self.arp_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.source_mac_address_arp_10 = QLabel(self.arp_page)
        self.source_mac_address_arp_10.setObjectName(u"source_mac_address_arp_10")
        self.source_mac_address_arp_10.setFont(font4)

        self.verticalLayout_3.addWidget(self.source_mac_address_arp_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.source_mac_address_arp_layout_10 = QHBoxLayout()
        self.source_mac_address_arp_layout_10.setObjectName(u"source_mac_address_arp_layout_10")
        self.scrollArea = QScrollArea(self.arp_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(500, 16777215))
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
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 415, 539))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.arp_type_radios = QHBoxLayout()
        self.arp_type_radios.setSpacing(0)
        self.arp_type_radios.setObjectName(u"arp_type_radios")
        self.arp_type_radios.setContentsMargins(-1, 0, -1, -1)
        self.arp_who_has_radio = QRadioButton(self.scrollAreaWidgetContents_4)
        self.arp_who_has_radio.setObjectName(u"arp_who_has_radio")
        sizePolicy.setHeightForWidth(self.arp_who_has_radio.sizePolicy().hasHeightForWidth())
        self.arp_who_has_radio.setSizePolicy(sizePolicy)
        self.arp_who_has_radio.setMinimumSize(QSize(0, 50))
        self.arp_who_has_radio.setMaximumSize(QSize(11000, 50))
        self.arp_who_has_radio.setChecked(True)

        self.arp_type_radios.addWidget(self.arp_who_has_radio)

        self.arp_is_at_radio = QRadioButton(self.scrollAreaWidgetContents_4)
        self.arp_is_at_radio.setObjectName(u"arp_is_at_radio")
        sizePolicy.setHeightForWidth(self.arp_is_at_radio.sizePolicy().hasHeightForWidth())
        self.arp_is_at_radio.setSizePolicy(sizePolicy)
        self.arp_is_at_radio.setMinimumSize(QSize(0, 50))
        self.arp_is_at_radio.setMaximumSize(QSize(10000, 50))

        self.arp_type_radios.addWidget(self.arp_is_at_radio)

        self.arp_type_radios.setStretch(0, 1)
        self.arp_type_radios.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.arp_type_radios)

        self.destination_ip_address_arp_layout_8 = QHBoxLayout()
        self.destination_ip_address_arp_layout_8.setObjectName(u"destination_ip_address_arp_layout_8")
        self.destination_ip_address_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.destination_ip_address_arp_label.setObjectName(u"destination_ip_address_arp_label")
        self.destination_ip_address_arp_label.setMinimumSize(QSize(200, 50))
        self.destination_ip_address_arp_label.setMaximumSize(QSize(50, 50))
        self.destination_ip_address_arp_label.setFont(font4)
        self.destination_ip_address_arp_label.setWordWrap(True)

        self.destination_ip_address_arp_layout_8.addWidget(self.destination_ip_address_arp_label)

        self.destination_ip_address_arp_input = IPAddressInput(self.scrollAreaWidgetContents_4)
        self.destination_ip_address_arp_input.setObjectName(u"destination_ip_address_arp_input")
        sizePolicy.setHeightForWidth(self.destination_ip_address_arp_input.sizePolicy().hasHeightForWidth())
        self.destination_ip_address_arp_input.setSizePolicy(sizePolicy)
        self.destination_ip_address_arp_input.setMinimumSize(QSize(0, 50))
        self.destination_ip_address_arp_input.setMaximumSize(QSize(250, 50))

        self.destination_ip_address_arp_layout_8.addWidget(self.destination_ip_address_arp_input)


        self.verticalLayout_6.addLayout(self.destination_ip_address_arp_layout_8)

        self.number_arp_layout = QHBoxLayout()
        self.number_arp_layout.setObjectName(u"number_arp_layout")
        self.number_arp_label = QLabel(self.scrollAreaWidgetContents_4)
        self.number_arp_label.setObjectName(u"number_arp_label")
        self.number_arp_label.setMinimumSize(QSize(200, 50))
        self.number_arp_label.setMaximumSize(QSize(50, 16777215))
        self.number_arp_label.setFont(font4)
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

        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.source_mac_address_arp_layout_10.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.source_mac_address_arp_layout_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 18)
        self.protocol_types_configuration_pages.addWidget(self.arp_page)
        self.dns_page = DNSConfigurationWidget()
        self.dns_page.setObjectName(u"dns_page")
        self.dns_page.setToolTipDuration(12)
        self.dns_page.setAutoFillBackground(False)
        self.dns_page.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.dns_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.source_mac_address_arp_13 = QLabel(self.dns_page)
        self.source_mac_address_arp_13.setObjectName(u"source_mac_address_arp_13")
        self.source_mac_address_arp_13.setFont(font4)

        self.verticalLayout_8.addWidget(self.source_mac_address_arp_13)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 418, 542))
        self.scrollAreaWidgetContents_5.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_5.setStyleSheet(u"QHBoxLayout {\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dns_source_ip_address = QHBoxLayout()
        self.dns_source_ip_address.setObjectName(u"dns_source_ip_address")
        self.dns_source_ip_address_label = QLabel(self.scrollAreaWidgetContents_5)
        self.dns_source_ip_address_label.setObjectName(u"dns_source_ip_address_label")
        self.dns_source_ip_address_label.setMaximumSize(QSize(200, 16777215))
        self.dns_source_ip_address_label.setFont(font4)
        self.dns_source_ip_address_label.setWordWrap(True)

        self.dns_source_ip_address.addWidget(self.dns_source_ip_address_label)

        self.dns_source_ip_address_input = IPAddressInput(self.scrollAreaWidgetContents_5)
        self.dns_source_ip_address_input.setObjectName(u"dns_source_ip_address_input")
        sizePolicy.setHeightForWidth(self.dns_source_ip_address_input.sizePolicy().hasHeightForWidth())
        self.dns_source_ip_address_input.setSizePolicy(sizePolicy)
        self.dns_source_ip_address_input.setMinimumSize(QSize(0, 50))
        self.dns_source_ip_address_input.setMaximumSize(QSize(250, 16777215))

        self.dns_source_ip_address.addWidget(self.dns_source_ip_address_input)


        self.verticalLayout_4.addLayout(self.dns_source_ip_address)

        self.dns_query_name = QHBoxLayout()
        self.dns_query_name.setObjectName(u"dns_query_name")
        self.dns_query_name_label = QLabel(self.scrollAreaWidgetContents_5)
        self.dns_query_name_label.setObjectName(u"dns_query_name_label")
        self.dns_query_name_label.setMaximumSize(QSize(200, 16777215))
        self.dns_query_name_label.setFont(font4)
        self.dns_query_name_label.setWordWrap(True)

        self.dns_query_name.addWidget(self.dns_query_name_label)

        self.dns_query_name_input = IPAddressInput(self.scrollAreaWidgetContents_5)
        self.dns_query_name_input.setObjectName(u"dns_query_name_input")
        sizePolicy.setHeightForWidth(self.dns_query_name_input.sizePolicy().hasHeightForWidth())
        self.dns_query_name_input.setSizePolicy(sizePolicy)
        self.dns_query_name_input.setMinimumSize(QSize(0, 50))
        self.dns_query_name_input.setMaximumSize(QSize(250, 16777215))

        self.dns_query_name.addWidget(self.dns_query_name_input)


        self.verticalLayout_4.addLayout(self.dns_query_name)

        self.dns_packet_number = QHBoxLayout()
        self.dns_packet_number.setObjectName(u"dns_packet_number")
        self.dns_packet_number_label = QLabel(self.scrollAreaWidgetContents_5)
        self.dns_packet_number_label.setObjectName(u"dns_packet_number_label")
        self.dns_packet_number_label.setMaximumSize(QSize(200, 16777215))
        self.dns_packet_number_label.setFont(font4)
        self.dns_packet_number_label.setWordWrap(True)

        self.dns_packet_number.addWidget(self.dns_packet_number_label)

        self.dns_packet_number_input = NumberLineEdit(self.scrollAreaWidgetContents_5)
        self.dns_packet_number_input.setObjectName(u"dns_packet_number_input")
        sizePolicy.setHeightForWidth(self.dns_packet_number_input.sizePolicy().hasHeightForWidth())
        self.dns_packet_number_input.setSizePolicy(sizePolicy)
        self.dns_packet_number_input.setMinimumSize(QSize(0, 50))
        self.dns_packet_number_input.setMaximumSize(QSize(250, 16777215))

        self.dns_packet_number.addWidget(self.dns_packet_number_input)


        self.verticalLayout_4.addLayout(self.dns_packet_number)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 18)
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
        self.packets_to_send_title = QLabel(self.CreatingAndSending)
        self.packets_to_send_title.setObjectName(u"packets_to_send_title")
        self.packets_to_send_title.setFont(font1)

        self.right_side.addWidget(self.packets_to_send_title)

        self.packets_to_send_scroll_container = QScrollArea(self.CreatingAndSending)
        self.packets_to_send_scroll_container.setObjectName(u"packets_to_send_scroll_container")
        sizePolicy.setHeightForWidth(self.packets_to_send_scroll_container.sizePolicy().hasHeightForWidth())
        self.packets_to_send_scroll_container.setSizePolicy(sizePolicy)
        self.packets_to_send_scroll_container.setMinimumSize(QSize(0, 0))
        self.packets_to_send_scroll_container.setMaximumSize(QSize(16777215, 16777215))
        self.packets_to_send_scroll_container.setWidgetResizable(True)
        self.packets_to_send_scroll_container.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, 0, 419, 702))
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

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.add_packet_button = QPushButton(self.CreatingAndSending)
        self.add_packet_button.setObjectName(u"add_packet_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_packet_button.sizePolicy().hasHeightForWidth())
        self.add_packet_button.setSizePolicy(sizePolicy2)
        self.add_packet_button.setMaximumSize(QSize(16777215, 100))
        self.add_packet_button.setFont(font3)

        self.horizontalLayout_3.addWidget(self.add_packet_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.send_packets_button = QPushButton(self.CreatingAndSending)
        self.send_packets_button.setObjectName(u"send_packets_button")
        sizePolicy2.setHeightForWidth(self.send_packets_button.sizePolicy().hasHeightForWidth())
        self.send_packets_button.setSizePolicy(sizePolicy2)
        self.send_packets_button.setMaximumSize(QSize(16777215, 100))
        self.send_packets_button.setFont(font3)

        self.horizontalLayout_3.addWidget(self.send_packets_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.CreatingAndSending, "")
        self.Summary = QWidget()
        self.Summary.setObjectName(u"Summary")
        self.Summary.setStyleSheet(u"QLabel\n"
" {\n"
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
        self.verticalLayout_13 = QVBoxLayout(self.Summary)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.duration_packet_generation_label = QLabel(self.Summary)
        self.duration_packet_generation_label.setObjectName(u"duration_packet_generation_label")

        self.horizontalLayout_7.addWidget(self.duration_packet_generation_label)

        self.duration_packet_generation_value = QLabel(self.Summary)
        self.duration_packet_generation_value.setObjectName(u"duration_packet_generation_value")

        self.horizontalLayout_7.addWidget(self.duration_packet_generation_value)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.export_label = QLabel(self.Summary)
        self.export_label.setObjectName(u"export_label")

        self.horizontalLayout_8.addWidget(self.export_label)

        self.download_pcap_file_button = QPushButton(self.Summary)
        self.download_pcap_file_button.setObjectName(u"download_pcap_file_button")
        sizePolicy2.setHeightForWidth(self.download_pcap_file_button.sizePolicy().hasHeightForWidth())
        self.download_pcap_file_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.download_pcap_file_button)

        self.export_to_wireshark_button = QPushButton(self.Summary)
        self.export_to_wireshark_button.setObjectName(u"export_to_wireshark_button")
        sizePolicy2.setHeightForWidth(self.export_to_wireshark_button.sizePolicy().hasHeightForWidth())
        self.export_to_wireshark_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.export_to_wireshark_button)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.Summary)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.total_number_of_packets = QLabel(self.Summary)
        self.total_number_of_packets.setObjectName(u"total_number_of_packets")

        self.horizontalLayout_4.addWidget(self.total_number_of_packets)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)

        self.tabWidget_2 = QTabWidget(self.Summary)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.output = QWidget()
        self.output.setObjectName(u"output")
        self.verticalLayout_14 = QVBoxLayout(self.output)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.console_output_container = QScrollArea(self.output)
        self.console_output_container.setObjectName(u"console_output_container")
        sizePolicy.setHeightForWidth(self.console_output_container.sizePolicy().hasHeightForWidth())
        self.console_output_container.setSizePolicy(sizePolicy)
        self.console_output_container.setMinimumSize(QSize(0, 0))
        self.console_output_container.setMaximumSize(QSize(16777215, 16777215))
        self.console_output_container.setWidgetResizable(True)
        self.console_output_container.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scroll_area_contents_2 = QWidget()
        self.scroll_area_contents_2.setObjectName(u"scroll_area_contents_2")
        self.scroll_area_contents_2.setGeometry(QRect(0, 0, 990, 426))
        self.scroll_area_contents_2.setStyleSheet(u"background-color: rgba(82, 88, 104, 1)")
        self.verticalLayout_12 = QVBoxLayout(self.scroll_area_contents_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.console_output = QVBoxLayout()
        self.console_output.setSpacing(10)
        self.console_output.setObjectName(u"console_output")
        self.console_output.setContentsMargins(-1, -1, -1, 0)
        self.console_output_label = ConsoleOutput(self.scroll_area_contents_2)
        self.console_output_label.setObjectName(u"console_output_label")
        self.console_output_label.setStyleSheet(u"QLabel\n"
" {\n"
"            position: absolute;\n"
"            padding: 10px;\n"
"            font-family: 'Inter';\n"
"            font-style: normal;\n"
"            font-weight: 700;\n"
"            font-size: 16px;\n"
"            line-height: 19px;\n"
"            text-align: center;\n"
"            color: #FFFFFF;\n"
"\n"
"}\n"
"")
        self.console_output_label.setWordWrap(True)

        self.console_output.addWidget(self.console_output_label)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.console_output.addItem(self.verticalSpacer_11)


        self.verticalLayout_12.addLayout(self.console_output)

        self.console_output_container.setWidget(self.scroll_area_contents_2)

        self.verticalLayout_14.addWidget(self.console_output_container)

        self.tabWidget_2.addTab(self.output, "")
        self.packets = QWidget()
        self.packets.setObjectName(u"packets")
        self.verticalLayout_16 = QVBoxLayout(self.packets)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.packets_container = QScrollArea(self.packets)
        self.packets_container.setObjectName(u"packets_container")
        sizePolicy.setHeightForWidth(self.packets_container.sizePolicy().hasHeightForWidth())
        self.packets_container.setSizePolicy(sizePolicy)
        self.packets_container.setMinimumSize(QSize(0, 0))
        self.packets_container.setMaximumSize(QSize(16777215, 16777215))
        self.packets_container.setWidgetResizable(True)
        self.packets_container.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scroll_area_contents_3 = QWidget()
        self.scroll_area_contents_3.setObjectName(u"scroll_area_contents_3")
        self.scroll_area_contents_3.setGeometry(QRect(0, 0, 972, 416))
        self.scroll_area_contents_3.setStyleSheet(u"background-color: rgba(82, 88, 104, 1)")
        self.verticalLayout_15 = QVBoxLayout(self.scroll_area_contents_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.packets_list = QVBoxLayout()
        self.packets_list.setSpacing(10)
        self.packets_list.setObjectName(u"packets_list")
        self.packets_list.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.packets_list.addItem(self.verticalSpacer_12)


        self.verticalLayout_15.addLayout(self.packets_list)

        self.packets_container.setWidget(self.scroll_area_contents_3)

        self.verticalLayout_16.addWidget(self.packets_container)

        self.tabWidget_2.addTab(self.packets, "")

        self.verticalLayout_13.addWidget(self.tabWidget_2)

        self.verticalLayout_13.setStretch(0, 3)
        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_13.setStretch(2, 5)
        self.tabWidget.addTab(self.Summary, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.protocol_types_configuration_pages.setCurrentIndex(1)
        self.ip_types_stacked_widget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


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
        self.icmp_radio.setText(QCoreApplication.translate("MainWindow", u"ICMP", None))
        self.tcp_radio.setText(QCoreApplication.translate("MainWindow", u"TCP", None))
        self.udp_radio.setText(QCoreApplication.translate("MainWindow", u"UDP", None))
        self.tcp_syn_radio.setText(QCoreApplication.translate("MainWindow", u"SYN", None))
        self.tcp_fin_radio.setText(QCoreApplication.translate("MainWindow", u"FIN", None))
        self.tcp_finack_radio.setText(QCoreApplication.translate("MainWindow", u"FIN-ACK", None))
        self.tcp_rst_radio.setText(QCoreApplication.translate("MainWindow", u"RST", None))
        self.tcp_synack_radio.setText(QCoreApplication.translate("MainWindow", u"SYN-ACK", None))
        self.tcp_psh_radio.setText(QCoreApplication.translate("MainWindow", u"PSH", None))
        self.tcp_ack_radio.setText(QCoreApplication.translate("MainWindow", u"ACK", None))
        self.tcp_urg_radio.setText(QCoreApplication.translate("MainWindow", u"URG", None))
        self.tcp_source_port_label.setText(QCoreApplication.translate("MainWindow", u"Source Port", None))
        self.tcp_destination_port_label.setText(QCoreApplication.translate("MainWindow", u"Destination Port", None))
        self.udp_destination_port_label.setText(QCoreApplication.translate("MainWindow", u"Source Port", None))
        self.udp_source_port_label.setText(QCoreApplication.translate("MainWindow", u"Destination Port", None))
        self.source_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Source IP Address", None))
        self.source_ip_address_input.setText("")
        self.destination_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Destination IP Address", None))
        self.time_to_live_ip_label.setText(QCoreApplication.translate("MainWindow", u"Time To Live", None))
        self.ip_payload_label.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.number_ip_label.setText(QCoreApplication.translate("MainWindow", u"How many of this packet?", None))
        self.number_ip_input.setInputMask("")
        self.source_mac_address_arp_10.setText(QCoreApplication.translate("MainWindow", u"ARP Configuration", None))
        self.arp_who_has_radio.setText(QCoreApplication.translate("MainWindow", u"Who has?", None))
        self.arp_is_at_radio.setText(QCoreApplication.translate("MainWindow", u"Is at?", None))
        self.destination_ip_address_arp_label.setText(QCoreApplication.translate("MainWindow", u"Target's IP Address", None))
        self.number_arp_label.setText(QCoreApplication.translate("MainWindow", u"How many?", None))
        self.source_mac_address_arp_13.setText(QCoreApplication.translate("MainWindow", u"DNS Configuration", None))
        self.dns_source_ip_address_label.setText(QCoreApplication.translate("MainWindow", u"Source IP Address", None))
        self.dns_query_name_label.setText(QCoreApplication.translate("MainWindow", u"Query Name", None))
        self.dns_packet_number_label.setText(QCoreApplication.translate("MainWindow", u"Number of Packets?", None))
        self.packets_to_send_title.setText(QCoreApplication.translate("MainWindow", u"Packets To Send", None))
        self.add_packet_button.setText(QCoreApplication.translate("MainWindow", u"Add Packets", None))
        self.send_packets_button.setText(QCoreApplication.translate("MainWindow", u"Send packets", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CreatingAndSending), QCoreApplication.translate("MainWindow", u"Creating and Sending", None))
        self.duration_packet_generation_label.setText(QCoreApplication.translate("MainWindow", u"Duration of Packet Generation", None))
        self.duration_packet_generation_value.setText(QCoreApplication.translate("MainWindow", u"300ms", None))
        self.export_label.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.download_pcap_file_button.setText(QCoreApplication.translate("MainWindow", u"Download Pcap File", None))
        self.export_to_wireshark_button.setText(QCoreApplication.translate("MainWindow", u"Export To Wireshark", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Number of Packets Sent", None))
        self.total_number_of_packets.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.console_output_label.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.packets), QCoreApplication.translate("MainWindow", u"Packets", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Summary), QCoreApplication.translate("MainWindow", u"Summary", None))
    # retranslateUi

