from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QTextEdit
from PySide6.QtCore import QTimer
from utils import *


class MessageWindow(QWidget):
    def __init__(self, window_name, my_name):
        super().__init__()
        self.new_message = None
        self.message_from = None

        self.partner = None
        self.my_name = my_name
        # Create UI elements
        self.setWindowTitle(window_name)
        self.message_label = QLabel("Messages:")
        self.message_text = QTextEdit()
        self.bit_message_label = QLabel("Sent bit messages:")
        self.bit_message_text = QTextEdit()
        self.send_label = QLabel("Send:")
        self.send_text = QLineEdit()
        self.send_button = QPushButton("Send")

        # Set up layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.message_text)
        self.layout.addWidget(self.bit_message_label)
        self.layout.addWidget(self.bit_message_text)
        self.layout.addWidget(self.send_label)
        self.layout.addWidget(self.send_text)

        # Add send button to layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.send_button)
        self.layout.addLayout(hbox)

        # Connect send button to function
        self.send_button.clicked.connect(self.send_message)

        # Set layout
        self.setLayout(self.layout)

        # Initialize the QTimer object and set the interval to 1 second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        # Connect the timeout signal of the QTimer object to the function that checks for data
        self.timer.timeout.connect(self.check_incoming)
        # Start the timer
        self.timer.start()

    def send_message(self):
        # append message to my window
        message = self.send_text.text()
        self.send_text.clear()
        self.message_text.append(self.my_name + ': ' + message)
        # code message
        message = txt2frame(message)
        name2send = txt2frame(self.my_name)
        # append message bit message to my window
        self.bit_message_text.append("Sent bit name:\n" + str(name2send)[1:-1])
        self.bit_message_text.append("Sent bit message:\n" + str(message)[1:-1])
        # send message
        self.partner.new_message = message
        self.partner.message_from = name2send

    def check_incoming(self):
        if self.new_message is not None:
            name2display = frames2txt(self.message_from)
            message2display = frames2txt(self.new_message)
            message2display = swearword_check(message2display)
            self.message_text.append(name2display + ': ' + message2display)
            self.new_message = None
            self.message_from = None
