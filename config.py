from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QGridLayout, QDialogButtonBox, QVBoxLayout, QSpinBox, QCheckBox
from aqt import  mw, qconnect

CONFIG_REQUIRED_CORRECT_ANSWERS = 'required_correct_answers'
CONFIG_SHOW_TOAST = 'show_toast'

class LeechBalancerConfig:
    def __init__(self):
        self.config = mw.addonManager.getConfig(__name__)
        self.dialog = QDialog(mw)
        self.init_menu()

    def init_menu(self):
      self.dialog.setWindowTitle("Leech Balancer")

      grid = QGridLayout()

      show_toast_label = QLabel("Show toast")
      show_toast = QCheckBox()
      show_toast.setChecked(self.config.get(CONFIG_SHOW_TOAST, True))
      grid.addWidget(show_toast_label, 0, 0)
      grid.addWidget(show_toast, 0, 1)

      required_correct_answers_label = QLabel("Required correct answers")
      required_correct_answers = QSpinBox()
      required_correct_answers.setMinimumWidth(200)
      required_correct_answers.setMinimum(1)
      required_correct_answers.setValue(self.config.get(CONFIG_REQUIRED_CORRECT_ANSWERS, 3))

      grid.addWidget(required_correct_answers_label, 1, 0)
      grid.addWidget(required_correct_answers, 1, 1)

      ok = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
      def save_config():
        self.config[CONFIG_REQUIRED_CORRECT_ANSWERS] = required_correct_answers.value()
        self.config[CONFIG_SHOW_TOAST] = show_toast.isChecked()
        mw.addonManager.writeConfig(__name__, self.config)
        self.dialog.close()

      ok.clicked.connect(save_config)

      cancel = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
      cancel.clicked.connect(self.dialog.close)

      buttons_layout = QHBoxLayout()
      buttons_layout.addStretch(1)
      buttons_layout.addWidget(ok)
      buttons_layout.addWidget(cancel)

      layout = QVBoxLayout()
      layout.addLayout(grid)
      layout.addLayout(buttons_layout)

      self.dialog.setLayout(layout)
    
    def open(self):
        self.dialog.exec()

def init_config():
    print('Setting up Leech Balancer config....')

    config = LeechBalancerConfig()
    menu_item = QAction("Leech Balancer Config", mw)
    qconnect(menu_item.triggered, config.open)
    mw.form.menuTools.addAction(menu_item)
