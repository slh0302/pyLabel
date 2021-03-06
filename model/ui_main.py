# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './basic.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.drawLabel import drawLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(630, 0, 161, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 8, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startPushButton.sizePolicy().hasHeightForWidth())
        self.startPushButton.setSizePolicy(sizePolicy)
        self.startPushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.startPushButton.setObjectName("startPushButton")
        self.verticalLayout.addWidget(self.startPushButton)
        self.redrawPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redrawPushButton.sizePolicy().hasHeightForWidth())
        self.redrawPushButton.setSizePolicy(sizePolicy)
        self.redrawPushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.redrawPushButton.setObjectName("redrawPushButton")
        self.verticalLayout.addWidget(self.redrawPushButton)
        self.pausPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pausPushButton.sizePolicy().hasHeightForWidth())
        self.pausPushButton.setSizePolicy(sizePolicy)
        self.pausPushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.pausPushButton.setObjectName("pausPushButton")
        self.verticalLayout.addWidget(self.pausPushButton)
        self.stoPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stoPushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.stoPushButton.setObjectName("stoPushButton")
        self.verticalLayout.addWidget(self.stoPushButton)
        self.FramesSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FramesSpinBox.sizePolicy().hasHeightForWidth())
        self.FramesSpinBox.setSizePolicy(sizePolicy)
        self.FramesSpinBox.setMaximumSize(QtCore.QSize(160, 16777215))
        self.FramesSpinBox.setMinimum(1)
        self.FramesSpinBox.setMaximum(10)
        self.FramesSpinBox.setObjectName("FramesSpinBox")
        self.verticalLayout.addWidget(self.FramesSpinBox)
        self.prePushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.prePushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.prePushButton.setObjectName("prePushButton")
        self.verticalLayout.addWidget(self.prePushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nextPushButton.setMaximumSize(QtCore.QSize(160, 25))
        self.nextPushButton.setObjectName("nextPushButton")
        self.verticalLayout.addWidget(self.nextPushButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(160, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.displayLabel = drawLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayLabel.sizePolicy().hasHeightForWidth())
        self.displayLabel.setSizePolicy(sizePolicy)
        self.displayLabel.setText("")
        self.displayLabel.setObjectName("displayLabel")
        self.verticalLayout_2.addWidget(self.displayLabel)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 520, 781, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuDoc = QtWidgets.QMenu(self.menubar)
        self.menuDoc.setObjectName("menuDoc")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_video = QtWidgets.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionSave_video = QtWidgets.QAction(MainWindow)
        self.actionSave_video.setObjectName("actionSave_video")
        self.actionTrain_Faster_RCNN = QtWidgets.QAction(MainWindow)
        self.actionTrain_Faster_RCNN.setObjectName("actionTrain_Faster_RCNN")
        self.actionWriter_slh = QtWidgets.QAction(MainWindow)
        self.actionWriter_slh.setObjectName("actionWriter_slh")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFiles.addAction(self.actionOpen_video)
        self.menuFiles.addAction(self.actionSave_video)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionExit)
        self.menuTool.addAction(self.actionTrain_Faster_RCNN)
        self.menuDoc.addAction(self.actionWriter_slh)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuDoc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tracking tools"))
        self.startPushButton.setText(_translate("MainWindow", "Start"))
        self.redrawPushButton.setText(_translate("MainWindow", "Re-Draw box"))
        self.pausPushButton.setText(_translate("MainWindow", "Pause"))
        self.stoPushButton.setText(_translate("MainWindow", "Stop"))
        self.prePushButton.setText(_translate("MainWindow", "Pre Frames"))
        self.nextPushButton.setText(_translate("MainWindow", "Next Frames"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOG Output:</p></body></html>"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuTool.setTitle(_translate("MainWindow", "Tools"))
        self.menuDoc.setTitle(_translate("MainWindow", "Doc"))
        self.actionOpen_video.setText(_translate("MainWindow", "Open video"))
        self.actionSave_video.setText(_translate("MainWindow", "Save video"))
        self.actionTrain_Faster_RCNN.setText(_translate("MainWindow", "Train Faster-RCNN"))
        self.actionWriter_slh.setText(_translate("MainWindow", "Author: slh"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
