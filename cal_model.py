"""Model for Calculator"""
from math import exp, log, log10, log2, sqrt
from collections import deque
import winsound


class CalculatorModel:
    """A model class for a simple calculator.
        This class handles the logic of the calculator, including updating the current
        expression, evaluating expressions, and maintaining a history of calculations.
    """
    def __init__(self):
        """Initialize the CalculatorModel."""
        self.current_express = ""
        self.cal_history = deque(maxlen=3)
        self.function_name = {'sqrt': 4, 'log2': 5, 'log10': 6, 'ln': 2, 'log': 3}

    def update_display(self, key_pressed):
        """Update the current expression based on the key pressed by user"""
        if key_pressed == 'DEL':
            self.delete_handle()
        elif key_pressed == 'CLR':
            self.current_express = ""
        elif key_pressed == "=":
            self.evaluate_num()
        elif key_pressed in self.function_name:
            self.function_handle(key_pressed)
        elif key_pressed == 'mod':
            self.current_express += '%'
        else:
            self.current_express += key_pressed

    def delete_handle(self):
        """Handle the deletion in the current expression."""
        for func, length in self.function_name.items():
            if self.current_express.endswith(func):
                self.current_express = self.current_express[:-length]
                break
        else:
            if len(self.current_express) > 0:
                self.current_express = self.current_express[:-1]

    def function_handle(self, function):
        """Handle the insertion of function into the current expression."""
        if self.current_express.endswith(('+', '-', '*', '/')):
            self.current_express += function + '('

        elif not self.current_express and function in self.function_name.keys():
            self.current_express += function + '('

        else:
            self.current_express = function + '(' + self.current_express + ')'

    def evaluate_num(self):
        """Evaluate the current expression and update the history"""
        try:
            math_function = {
                'sqrt': sqrt,
                'log10': log10,
                'log2': log2,
                'exp': exp,
                'ln': log,
                'log': log
            }
            result = eval(self.current_express, math_function)
            self.cal_history.append((self.current_express, result))
            self.current_express = str(result)
        except:

            self.current_express = ''
            self.current_express = "Invalid"
            winsound.Beep(1000, 500)

    def get_history(self):
        """receive the calculation history"""
        return self.cal_history
