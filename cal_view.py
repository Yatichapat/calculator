import tkinter as tk
from tkinter import ttk
from cal_model import CalculatorModel


class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.model = CalculatorModel()
        self.init_components(columns=3)

    @property
    def frame(self):
        return self

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        self.display1 = tk.Entry(self, justify='right', width=10, background='white', font=('Arial', 35),
                                 foreground='black')
        self.display1.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
        self.display1.bind("<KeyPress>", lambda event: "break")

        self.function_combo = ttk.Combobox(self, values=["exp", "ln", "log", "log10", "log2", "sqrt"],
                                           font=('Arial', 15), state='readonly')
        self.function_combo.grid(row=2, column=0, columnspan=1, sticky=tk.NSEW)
        self.function_combo.bind("<<ComboboxSelected>>", self.update_function_display)

        label_function = tk.Label(self, text=': choose function', foreground='grey')
        label_function.grid(row=2, column=1)

        self.history_display = tk.Text(self, height=3, width=10, background='white', font=('Arial', 15),
                                       foreground='grey')
        self.history_display.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
        self.history_display.bind("<KeyPress>", lambda event: "break")

        keypad = self.make_keypad(columns)
        operator = self.make_operator_pad()

        keypad.grid(row=3, column=0, sticky=tk.NSEW, padx=2, pady=2)
        operator.grid(row=3, column=1, sticky=tk.NSEW, padx=2, pady=2)

        for button in keypad.winfo_children():
            button.bind("<Button-1>", self.update_display)

        for button in operator.winfo_children():
            button.bind("<Button-1>", self.update_display)

        self.set_resizable()

    def make_keypad(self, columns) -> tk.Frame:
        keys = Keypad(self, ['CLR', 'DEL', 'mod', '(', ')', '**', '7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '='], columns=columns) #['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']
        return keys

    def make_operator_pad(self) -> tk.Frame:
        operator = Keypad(self, ['/', '*', '-', '+'])
        return operator

    def update_display(self, event):
        click_button = event.widget['text']
        self.model.update_display(click_button)
        print(click_button)
        self.display1.delete(0, tk.END)
        self.display1.insert(tk.END, self.model.current_express)
        if self.model.current_express == "Invalid":
            self.display1.configure(foreground='red')
        else:
            self.display1.configure(foreground='black')
        self.display_history()

    def update_function_display(self, event):
        select_function = self.function_combo.get()
        self.model.update_display(select_function)
        self.display1.delete(0, tk.END)
        self.display1.insert(tk.END, self.model.current_express)

    def display_history(self):
        self.history_display.delete(1.0, tk.END)
        for express, result in self.model.get_history():
            self.history_display.insert(tk.END, f"{express} = {result}\n")

    def set_resizable(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


class Keypad(tk.Frame):
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)

        # keynames and columns
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns):
        self.make_keypad(columns)
        self.make_operator()

    def make_keypad(self, columns):
        frame = tk.Frame
        for i in range(len(self.keynames)):
            column = i % columns
            row = i // columns
            button = tk.Button(self, text=str(self.keynames[i]), width=5, font=5, foreground='black',
                               background='lightgrey')
            button.grid(row=row, sticky=tk.NSEW, column=column, padx=2, pady=2)
            self.grid_rowconfigure(i // columns, weight=1)
            self.grid_columnconfigure(i % columns, weight=1)
        return frame

    def make_operator(self) -> tk.Frame:
        frame = tk.Frame(self)
        row = 0
        column = 0

        for each_key in self.keynames:
            button_op = tk.Button(frame, text=each_key, width=3, font=5, foreground='black', background='lightgrey')
            button_op.grid(row=row, column=column, sticky=tk.NSEW, padx=2.5, pady=2.5)

            frame.grid_rowconfigure(row, weight=1)
            frame.grid_columnconfigure(column, weight=1)

            row += 1
        return frame

    def bind(self, sequence=None, func=None, add=None):
        for button in self.winfo_children():
            button.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for set_value in self.winfo_children():
            if isinstance(set_value, tk.Button):
                set_value[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        for change in self.winfo_children():
            if isinstance(change, tk.Button):
                if key in change.keys():
                    return change[key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """

        for child in self.frame.winfo_children():
            child.configure(**kwargs)

    @property
    def frame(self):
        return super()

