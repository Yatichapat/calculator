"""Main for calculator application"""
from cal_view import CalculatorView
from cal_model import CalculatorModel
from cal_controller import CalculatorController


if __name__ == '__main__':
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.update_display = controller.click_handler
    controller.run()
