# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jan 31 20:15:52 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1276, 746)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(25)
        self.verticalLayout_6.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.condList = QtGui.QTableWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.condList.sizePolicy().hasHeightForWidth())
        self.condList.setSizePolicy(sizePolicy)
        self.condList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.condList.setAlternatingRowColors(True)
        self.condList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.condList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.condList.setShowGrid(False)
        self.condList.setObjectName(_fromUtf8("condList"))
        self.condList.setColumnCount(2)
        self.condList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.condList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.condList.setHorizontalHeaderItem(1, item)
        self.condList.horizontalHeader().setDefaultSectionSize(40)
        self.condList.horizontalHeader().setStretchLastSection(True)
        self.condList.verticalHeader().setVisible(False)
        self.condList.verticalHeader().setDefaultSectionSize(20)
        self.condList.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_6.addWidget(self.condList)
        self.condButton = QtGui.QPushButton(self.tab_4)
        self.condButton.setObjectName(_fromUtf8("condButton"))
        self.verticalLayout_6.addWidget(self.condButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.firstAx = None
        self.condWidget = ConditionsPlotWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.condWidget.sizePolicy().hasHeightForWidth())
        self.condWidget.setSizePolicy(sizePolicy)
        self.condWidget.setObjectName(_fromUtf8("condWidget"))
        self.horizontalLayout_5.addWidget(self.condWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.speciesList = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.speciesList.sizePolicy().hasHeightForWidth())
        self.speciesList.setSizePolicy(sizePolicy)
        self.speciesList.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.speciesList.setAlternatingRowColors(True)
        self.speciesList.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.speciesList.setShowGrid(False)
        self.speciesList.setObjectName(_fromUtf8("speciesList"))
        self.speciesList.setColumnCount(2)
        self.speciesList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.speciesList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.speciesList.setHorizontalHeaderItem(1, item)
        self.speciesList.horizontalHeader().setDefaultSectionSize(40)
        self.speciesList.horizontalHeader().setStretchLastSection(True)
        self.speciesList.verticalHeader().setVisible(False)
        self.speciesList.verticalHeader().setDefaultSectionSize(20)
        self.speciesList.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_3.addWidget(self.speciesList)
        self.plotButton = QtGui.QPushButton(self.tab)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.verticalLayout_3.addWidget(self.plotButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.densWidget = DensityPlotWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.densWidget.sizePolicy().hasHeightForWidth())
        self.densWidget.setSizePolicy(sizePolicy)
        self.densWidget.setObjectName(_fromUtf8("densWidget"))
        self.horizontalLayout_2.addWidget(self.densWidget)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.reactList = QtGui.QTableWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.reactList.sizePolicy().hasHeightForWidth())
        self.reactList.setSizePolicy(sizePolicy)
        self.reactList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.reactList.setAlternatingRowColors(True)
        self.reactList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.reactList.setShowGrid(False)
        self.reactList.setObjectName(_fromUtf8("reactList"))
        self.reactList.setColumnCount(2)
        self.reactList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.reactList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.reactList.setHorizontalHeaderItem(1, item)
        self.reactList.horizontalHeader().setDefaultSectionSize(40)
        self.reactList.horizontalHeader().setSortIndicatorShown(True)
        self.reactList.horizontalHeader().setStretchLastSection(True)
        self.reactList.verticalHeader().setVisible(False)
        self.reactList.verticalHeader().setDefaultSectionSize(20)
        self.reactList.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_4.addWidget(self.reactList)
        self.reactButton = QtGui.QPushButton(self.tab_3)
        self.reactButton.setObjectName(_fromUtf8("reactButton"))
        self.verticalLayout_4.addWidget(self.reactButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.reactWidget = RatePlotWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.reactWidget.sizePolicy().hasHeightForWidth())
        self.reactWidget.setSizePolicy(sizePolicy)
        self.reactWidget.setObjectName(_fromUtf8("reactWidget"))
        self.horizontalLayout_4.addWidget(self.reactWidget)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.speciesSourceList = QtGui.QTableWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.speciesSourceList.sizePolicy().hasHeightForWidth())
        self.speciesSourceList.setSizePolicy(sizePolicy)
        self.speciesSourceList.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.speciesSourceList.setAlternatingRowColors(True)
        self.speciesSourceList.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.speciesSourceList.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.speciesSourceList.setShowGrid(False)
        self.speciesSourceList.setObjectName(_fromUtf8("speciesSourceList"))
        self.speciesSourceList.setColumnCount(2)
        self.speciesSourceList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.speciesSourceList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.speciesSourceList.setHorizontalHeaderItem(1, item)
        self.speciesSourceList.horizontalHeader().setDefaultSectionSize(40)
        self.speciesSourceList.horizontalHeader().setStretchLastSection(True)
        self.speciesSourceList.verticalHeader().setVisible(False)
        self.speciesSourceList.verticalHeader().setDefaultSectionSize(20)
        self.speciesSourceList.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_2.addWidget(self.speciesSourceList)
        self.Combo_filter = QtGui.QComboBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Combo_filter.sizePolicy().hasHeightForWidth())
        self.Combo_filter.setSizePolicy(sizePolicy)
        self.Combo_filter.setObjectName(_fromUtf8("Combo_filter"))
        self.Combo_filter.addItem(_fromUtf8(""))
        self.Combo_filter.addItem(_fromUtf8(""))
        self.Combo_filter.addItem(_fromUtf8(""))
        self.Combo_filter.addItem(_fromUtf8(""))
        self.Combo_filter.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.Combo_filter)
        self.sourceButton = QtGui.QPushButton(self.tab_2)
        self.sourceButton.setObjectName(_fromUtf8("sourceButton"))
        self.verticalLayout_2.addWidget(self.sourceButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.sourceWidget = SourcePlotWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sourceWidget.sizePolicy().hasHeightForWidth())
        self.sourceWidget.setSizePolicy(sizePolicy)
        self.sourceWidget.setObjectName(_fromUtf8("sourceWidget"))
        self.horizontalLayout_3.addWidget(self.sourceWidget)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLog_scale_in_time = QtGui.QAction(MainWindow)
        self.actionLog_scale_in_time.setCheckable(True)
        self.actionLog_scale_in_time.setObjectName(
            _fromUtf8("actionLog_scale_in_time"))
        self.actionDatacursor = QtGui.QAction(MainWindow)
        self.actionDatacursor.setCheckable(True)
        self.actionDatacursor.setObjectName(_fromUtf8("actionDatacursor"))
        self.actionExport_data = QtGui.QAction(MainWindow)
        self.actionExport_data.setObjectName(_fromUtf8("actionExport_data"))
        self.actionStart_a_simulation = QtGui.QAction(MainWindow)
        self.actionStart_a_simulation.setObjectName(
            _fromUtf8("actionStart_a_simulation"))
        self.actionImport_from_directory = QtGui.QAction(MainWindow)
        self.actionImport_from_directory.setObjectName(
            _fromUtf8("actionImport_from_directory"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionFilter_small_rates = QtGui.QAction(MainWindow)
        self.actionFilter_small_rates.setCheckable(True)
        self.actionFilter_small_rates.setChecked(True)
        self.actionFilter_small_rates.setObjectName(
            _fromUtf8("actionFilter_small_rates"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImport_from_directory)
        self.menuFile.addAction(self.actionExport_data)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionLog_scale_in_time)
        self.menuOptions.addAction(self.actionDatacursor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QtPlaskin", None))
        self.condList.setSortingEnabled(True)
        item = self.condList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#", None))
        item = self.condList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Condition", None))
        self.condButton.setText(_translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), _translate("MainWindow", "Overview", None))
        self.speciesList.setSortingEnabled(True)
        item = self.speciesList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#", None))
        item = self.speciesList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Species", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Densities", None))
        self.reactList.setSortingEnabled(True)
        item = self.reactList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#", None))
        item = self.reactList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reaction", None))
        self.reactButton.setText(_translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("MainWindow", "Reactions", None))
        self.speciesSourceList.setSortingEnabled(True)
        item = self.speciesSourceList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#", None))
        item = self.speciesSourceList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Species", None))
        self.Combo_filter.setItemText(0, _translate(
            "MainWindow", "Filter at 10%", None))
        self.Combo_filter.setItemText(
            1, _translate("MainWindow", "Filter at 1%", None))
        self.Combo_filter.setItemText(2, _translate(
            "MainWindow", "Filter at 0.1%", None))
        self.Combo_filter.setItemText(3, _translate(
            "MainWindow", "Filter at 0.01%", None))
        self.Combo_filter.setItemText(
            4, _translate("MainWindow", "Show all", None))
        self.sourceButton.setText(_translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Sensitivity analysis", None))
        self.label.setText(_translate(
            "MainWindow", "QtPlaskin - (c) Alejandro Luque, Instituto de Astrofísica de Andalucía (IAA), CSIC, 2011", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menuOptions.setTitle(_translate("MainWindow", "&Options", None))
        self.actionOpen.setText(_translate("MainWindow", "&Open...", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionLog_scale_in_time.setText(
            _translate("MainWindow", "Log scale in time", None))
        self.actionDatacursor.setText(_translate(
            "MainWindow", "Use Datacursor", None))
        self.actionExport_data.setText(_translate(
            "MainWindow", "Export data...", None))
        self.actionStart_a_simulation.setText(_translate(
            "MainWindow", "Start a simulation...", None))
        self.actionImport_from_directory.setText(_translate(
            "MainWindow", "Import from directory...", None))
        self.actionImport_from_directory.setShortcut(
            _translate("MainWindow", "Ctrl+I", None))
        self.actionSave.setText(_translate("MainWindow", "Save...", None))
        self.actionUpdate.setText(_translate("MainWindow", "Update", None))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionFilter_small_rates.setText(
            _translate("MainWindow", "Filter small rates", None))
        self.actionFilter_small_rates.setToolTip(_translate(
            "MainWindow", "When checked, some rates are not displayed in the sensitivity analisys to avoid cluttering", None))

from qtplaskin.mplwidget import RatePlotWidget, SourcePlotWidget, ConditionsPlotWidget, DensityPlotWidget
