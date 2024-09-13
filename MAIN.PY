class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.new_tab()
        
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        # Navigation buttons, as before...
        # URL bar, as before...

        # Create a "New Tab" button in the navbar
        new_tab_button = QAction('New Tab', self)
        new_tab_button.triggered.connect(self.new_tab)
        self.navbar.addAction(new_tab_button)

    # Method to open a new tab
    def new_tab(self, qurl=None):
        if qurl is None:
            qurl = QUrl("http://www.google.com")

        browser = QWebEngineView()
        browser.setUrl(qurl)

        index = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(index)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_tab_title(qurl, browser))

    # Method to update the title of the tab
    def update_tab_title(self, qurl, browser):
        index = self.tabs.indexOf(browser)
        self.tabs.setTabText(index, browser.page().title())

    # Method to close the current tab
    def close_current_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
