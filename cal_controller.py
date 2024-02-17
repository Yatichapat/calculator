"""Display the calculator user interface."""
from cal_view import CalculatorView
from cal_model import CalculatorModel
import tkinter as tk
from tkinter import ttk

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def click_handler(self, event):
        self.model.update_expression(event)
        # self.view.insert(tk.END, self.model.current_express)
        # print(click_button['text'])

    def run(self):
        self.view.mainloop()


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.update_display = controller.click_handler
    controller.run()

