import tkinter as tk
from tkinter import ttk


class CalculatorModel:
    def __init__(self):
        self.current_express = ""
        self.cal_history = []

    def update_display(self, key_pressed):
        if key_pressed == 'DEL':
            self.current_express = self.current_express[:-1]

        elif key_pressed == 'CLR':
            self.current_express = ""

        elif key_pressed == "=":
            self.evaluate_num()
        else:
            self.current_express += key_pressed

    def evaluate_num(self):
        try:
            result = eval(self.current_express)
            self.cal_history.append((self.current_express, result))
            self.current_express = str(result)
        except:
            print("Invalid expression:", Exception)

    def get_history(self):
        return self.cal_history


