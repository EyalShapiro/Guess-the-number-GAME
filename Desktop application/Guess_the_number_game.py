import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)
import random


class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Number Guessing Game")
        self.setGeometry(100, 100, 300, 200)
        self.num_to_guess = random.randint(1, 10)
        self.attempts_left = 3

        layout = QVBoxLayout()

        self.instructions_label = QLabel(
            "You have three attempts to guess the number. The number is between 1-10"
        )
        layout.addWidget(self.instructions_label)

        self.input_label = QLabel("Enter your guess:")
        layout.addWidget(self.input_label)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.check_guess)
        layout.addWidget(self.guess_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        with open("style.qss", "r") as f:  # Apply styles
            _style = f.read()
            self.setStyleSheet(_style)

    def check_guess(self):

        guess = int(self.input_box.text())
        if guess == self.num_to_guess:
            self.result_label.setText(
                f"Hurray!! You guessed the number right ({self.num_to_guess})"
            )
            self.guess_button.setEnabled(False)
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.result_label.setText(
                    f"Sorry, you've run out of attempts. The number was {self.num_to_guess}"
                )
                self.guess_button.setEnabled(False)
            else:
                self.result_label.setText(
                    f"Your guess is incorrect. You have {self.attempts_left} attempts left."
                )


def main():
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
