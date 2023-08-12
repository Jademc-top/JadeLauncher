# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import beijin_rc
import beijin_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(814, 539)
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.launcher_settings = QPushButton(self.centralwidget)
        self.launcher_settings.setObjectName(u"launcher_settings")
        self.launcher_settings.setGeometry(QRect(0, 300, 51, 51))
        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(0, 180, 51, 51))
        self.help = QPushButton(self.centralwidget)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(0, 240, 51, 51))
        self.more = QPushButton(self.centralwidget)
        self.more.setObjectName(u"more")
        self.more.setGeometry(QRect(0, 120, 51, 51))
        self.launcher_start = QPushButton(self.centralwidget)
        self.launcher_start.setObjectName(u"launcher_start")
        self.launcher_start.setGeometry(QRect(0, 60, 51, 51))
        self.game_start = QPushButton(self.centralwidget)
        self.game_start.setObjectName(u"game_start")
        self.game_start.setGeometry(QRect(490, 260, 211, 61))
        self.game_settings = QPushButton(self.centralwidget)
        self.game_settings.setObjectName(u"game_settings")
        self.game_settings.setGeometry(QRect(0, 360, 51, 51))
        self.game_version = QPushButton(self.centralwidget)
        self.game_version.setObjectName(u"game_version")
        self.game_version.setGeometry(QRect(490, 330, 211, 61))
        self.login_player_info = QTextEdit(self.centralwidget)
        self.login_player_info.setObjectName(u"login_player_info")
        self.login_player_info.setGeometry(QRect(520, 210, 141, 31))
        self.backdrop = QListView(self.centralwidget)
        self.backdrop.setObjectName(u"backdrop")
        self.backdrop.setGeometry(QRect(0, 0, 871, 581))
        self.backdrop.setMaximumSize(QSize(871, 581))
        self.backdrop.setStyleSheet(u"background-image:url(:/2.png)")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(490, 410, 211, 31))
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setToolTipDuration(-1)
        self.textBrowser.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.backdrop.raise_()
        self.launcher_settings.raise_()
        self.download.raise_()
        self.help.raise_()
        self.more.raise_()
        self.launcher_start.raise_()
        self.game_start.raise_()
        self.game_settings.raise_()
        self.game_version.raise_()
        self.login_player_info.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.launcher_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.more.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.launcher_start.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.game_start.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6e38\u620f", None))
        self.game_settings.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u8bbe\u7f6e", None))
        self.game_version.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u9009\u62e9", None))
        self.login_player_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u767b\u5f55\u73a9\u5bb6:</span><span style=\" font-size:12pt; font-weight:600;\">im1340</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u6e38\u620f\u7248\u672c\uff1a1.20.1</p></body></html>", None))
    # retranslateUi

