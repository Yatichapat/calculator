import tkinter as tk
from tkinter import ttk
from math import exp, log, log10, log2, sqrt
from collections import deque


class CalculatorModel:
    def __init__(self, max_length=3):
        self.current_express = ""
        self.cal_history = deque(maxlen=max_length)
        self.function_name = {'sqrt': 4, 'log2': 5, 'log10': 6, 'ln': 2, 'log': 3}

    def update_display(self, key_pressed):
        if key_pressed == 'DEL':
            for func, length in self.function_name.items():
                if self.current_express.endswith(func):
                    self.current_express = self.current_express[:-length]
                    break
            else:
                if len(self.current_express) > 0:
                    self.current_express = self.current_express[:-1]

        elif key_pressed == 'CLR':
            self.current_express = ""

        elif key_pressed == "=":
            self.evaluate_num()

        elif key_pressed in {'log', 'exp', 'sqrt', 'log2', 'log10', 'ln'}:
            if self.current_express and self.current_express[-1] == '(':
                self.current_express += key_pressed
            else:
                self.current_express += key_pressed + '('

        else:
            self.current_express += key_pressed

    def evaluate_num(self):
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

    def get_history(self):
        return self.cal_history


