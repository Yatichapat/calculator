import tkinter as tk
from tkinter import ttk
from math import exp, log, log10, log2, sqrt
from collections import deque


class CalculatorModel:
    def __init__(self, max_length=3):
        self.current_express = ""
        self.cal_history = deque(maxlen=max_length)

    def update_display(self, key_pressed):
        if key_pressed == 'DEL':
            if self.current_express.endswith(('sqrt', 'log2')):
                self.current_express = self.current_express[:-4]
            elif self.current_express.endswith('log10'):
                self.current_express = self.current_express[:-5]
            elif len(self.current_express) > 0:
                self.current_express = self.current_express[:-1]
        elif key_pressed == 'CLR':
            self.current_express = ""

        elif key_pressed == "=":
            self.evaluate_num()

        elif key_pressed in {'exp', 'sqrt', 'log2', 'log10'}:
            if self.current_express and self.current_express[-1] in {'+', '-', '*', '/'}:
                self.current_express += '*'
            elif self.current_express and self.current_express[-1] == '(':
                self.current_express += key_pressed
            else:
                self.current_express += key_pressed + '('

        else:
            self.current_express += key_pressed

    def evaluate_num(self):
        try:
            if '^' in self.current_express:
                base, expo = self.current_express.split('^')
                result = float(base) ** float(expo)

            elif 'sqrt(' in self.current_express:
                root = float(self.current_express.split('sqrt(')[1].rstrip(')'))
                result = sqrt(root)

            elif 'log2(' in self.current_express:
                root = float(self.current_express.split('log2(')[1].rstrip(')'))
                result = log2(root)

            elif 'log10(' in self.current_express:
                root = float(self.current_express.split('log10(')[1].rstrip(')'))
                result = log10(root)

            elif 'exp(' in self.current_express:
                root = float(self.current_express.split('exp(')[1].rstrip(')'))
                result = exp(root)

            else:
                result = eval(self.current_express)
            self.cal_history.append((self.current_express, result))
            self.current_express = str(result)
        except:
            self.current_express = ''
            self.current_express = "Invalid"

    def get_history(self):
        return self.cal_history


