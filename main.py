from PySide6.QtWidgets import QApplication
from main_window import MessageWindow
import sys


if __name__ == '__main__':
    # Create QApplication
    app = QApplication(sys.argv)

    # Create MessageWindow and show
    window_1 = MessageWindow('window 1', 'Bob')
    window_1.show()

    window_2 = MessageWindow('window 2', 'Fred')
    window_2.show()

    window_1.partner = window_2
    window_2.partner = window_1

    # Run the event loop
    sys.exit(app.exec())
