from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from io import StringIO

import sys

import altair as alt
from vega_datasets import data
import altair_viewer

class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    # Disabling MaxRowsError
    alt.data_transformers.disable_max_rows()
    altair_viewer._global_viewer._use_bundled_js = False
    alt.data_transformers.enable('data_server')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)
        self.windows = []
        self.setZoomFactor(1.24) # 0.25 to 5

    @QtCore.pyqtSlot(QtWebEngineWidgets.QWebEngineDownloadItem)
    def onDownloadRequested(self, download):
        if (
            download.state()
            == QtWebEngineWidgets.QWebEngineDownloadItem.DownloadRequested
        ):
            path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, self.tr("Save as"), download.path()
            )
            if path:
                download.setPath(path)
                download.accept()

    def createWindow(self, type_):
        if type_ == QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
            window = QtWidgets.QMainWindow(self)
            view = QtWebEngineWidgets.QWebEngineView(window)
            window.resize(640, 480)
            window.setCentralWidget(view)
            window.show()
            return view

    def updateChart(self, chart, **kwargs):
        output = StringIO()
        chart.save(output,'html', **kwargs, embed_options={'renderer':'svg'})
        self.setHtml(output.getvalue())