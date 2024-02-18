"""Controller for model and view."""


class CalculatorController:
    """
    Controller class for managing interactions between the calculator model and view.

    Attributes:
        model: The calculator model instance responsible
            for performing calculations.
        view: The calculator view instance responsible
            for displaying the user interface.
    """
    def __init__(self, cal_model, cal_view):
        """Initializes the CalculatorController with the provided calculator model and view."""
        self.model = cal_model
        self.view = cal_view

    def click_handler(self, event):
        """for update the calculator model accordingly when user pressed button or combobox"""
        self.model.update_expression(event)

    def run(self):
        """run the calculator programme"""
        self.view.mainloop()
