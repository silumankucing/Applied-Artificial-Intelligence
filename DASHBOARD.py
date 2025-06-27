import sys
import pandas as pd
import matplotlib.pyplot as plt
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSizePolicy
)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
import io

class Dashboard(QWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.numeric_cols = df.select_dtypes(include='number').columns.tolist()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Global Economy Indicators Dashboard")
        layout = QVBoxLayout()

        self.label = QLabel("Select Indicator:")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(self.numeric_cols)
        self.combo.currentTextChanged.connect(self.update_plot)
        layout.addWidget(self.combo)

        self.plot_label = QLabel()
        self.plot_label.setAlignment(Qt.AlignCenter)
        self.plot_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.plot_label)

        self.setLayout(layout)
        self.update_plot(self.numeric_cols[0] if self.numeric_cols else "")

    def update_plot(self, selected_indicator):
        if not selected_indicator:
            self.plot_label.clear()
            return
        plt.figure(figsize=(10, 6))
        plt.bar(self.df[self.df.columns[0]], self.df[selected_indicator])
        plt.xlabel(self.df.columns[0])
        plt.ylabel(selected_indicator)
        plt.title(f"{selected_indicator} by {self.df.columns[0]}")
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())
        self.plot_label.setPixmap(pixmap)

if __name__ == '__main__':
    df = pd.read_csv('Global Economy Indicators.csv')
    app = QApplication(sys.argv)
    dashboard = Dashboard(df)
    dashboard.resize(900, 700)
    dashboard.show()
    sys.exit(app.exec_())