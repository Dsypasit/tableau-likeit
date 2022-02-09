from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

from io import StringIO


class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)
        self.windows = []

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
        chart.save(output, "html", **kwargs)
        self.setHtml(output.getvalue())


if __name__ == "__main__":
    import sys

    import altair as alt
    from vega_datasets import data

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()

    cars = data.cars()

    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=alt.X("Miles_per_Gallon", bin=True), y="count()",)
        .properties(title="A bar chart")
        .configure_title(anchor="start")
    )

    view = WebEngineView()
    view.updateChart(chart)
    w.setCentralWidget(view)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())